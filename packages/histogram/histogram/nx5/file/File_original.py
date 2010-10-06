#!/usr/bin/env python
# (c) Copyright 2005 T. M. Kelley, California Institute of Technology

import hdf5fs.h5fs as H5fs
import hdf5fs.h5space as space
from nx5.nexml.elements.Group import Group
from nx5.nexml.elements.Dataset import Dataset

import journal
debug = journal.debug( "nx5.File")

class File(object):
    """File( filename)
    """

    def XMLstring( self):
        return  '\n'.join( self._XMLrep)

    def root(self): return self._root


    def insert(self, dataset, stream, *args, **kwds):
        """insert( dataset, stream [, starts, sizes][, targetType=typename])
        Insert a nexus slab into a stream.
        dataset: a nexus.nexml.elements.Dataset object.
        stream: a PyCObject/void ptr to buffer for stream
        starts: list of indices at which to start reading
            (length must be same as dataset rank)
        sizes: how many elements to read in each dimension
            (length must be same as dataset rank)
        targetType: type you'd like results cast to (shd match stream!),
                    only works within class--i.e. 32 bit floats to 64 bit,
                    but not int to float. Should be a name like "double", "int"
        """
        
        # Make sure this dataset belongs to this file?
        # "stream" should be a PyCObject with a void pointer
        # to a buffer for the data from the file.
        path = dataset.NXpath().asString()
        f = self._file.open( path)

        # work around for mystery bug (??)
        import hdf5fs.h5type as h5type
        if dataset.datatype() == 5:
            mytype = h5type.H5type( "float")
        elif dataset.datatype() == 25:
            mytype = h5type.H5type( "unsigned int")
        else:
            mytype = f.getType()

        if len(args) == 0:
            f.read( stream, mytype)
            
        elif len(args) == 2:
            starts = args[0]; sizes  = args[1]; sz = 1
            for size in sizes:
                sz *= size
            
            memspace = space.H5space( (sz,))
            fspace = space.H5space( f.getSpace().info()['dims'])
            fspace.selectHyperslab( "set", starts, sizes)

            f.read( stream, mytype, memspace, fspace)
        elif len(args) == 3:
            raise NotImplementedError, "Not yet able to handle advanced reads"
        else:
            raise NotImplementedError, "Not yet able to handle advanced reads"
        return 


    def reader(self):
        import Reader
        reader = Reader.Reader(self)
        return reader


    def _graph(self, vgroup = None):
        """_graph( group = None) -> None
        Graph a group. Defaults to file root."""

        if vgroup is None: vgroup = self._root
        
        self._expandGroup( vgroup)

        return None


    def _expandGroup( self, group):
        """Recurse down a level to 
        """
        path = group.path()
        if not path: path = '/'

        debug.log( "expanding group " + group.name() + " " + \
                   group.className() + " " + group.path())

        directory = self._file.open( path)

        subgroups, children = self._listDir( directory)

        group.update( children, subgroups)

        for subgroup in subgroups:
            self._graph( subgroup)
        return
    

    def _listDir( self, directory):
        """
        """
        subgroups = []; children = {}

        items = directory.read()

        for item in items:
            path = '/'.join( (directory.path, item))
            stat = self._file.stat( path)

            if   stat['type'] == 'directory':
                node = self._makeGroup( item, path)
                subgroups.append( node)
                
            elif stat['type'] == 'file':
                node = self._makeDataset( item, path)

            else:
                node = None
                debug.log("Unrecognized type")
                
            if node:
                children[ node.name()] = node

        return subgroups, children


    def _listAttributes( self, attributee):
        """Returns a dictionary of the attributes for something with a listattr
        method."""

        attributes = {}

        atts = attributee.listattr()

        for att in atts:
            attributes[att.name()] = att.value()
                
        return attributes


    def __init__(self, filename, mode = 'r'):
        """NexusFile( filename)
        Exceptions: IOError"""

        debug.log("filename: %s" % filename)
        
        _checkFileValid(filename)

        debug.log("Attempting to open file")

        try:
            f = H5fs.H5fs( filename, mode)
        except IOError, msg:
            print "File unable to initialize properly:", msg
            raise

        debug.log("nexus file opened")

        self._filename = filename
        self._file = f
        self._root = Group( filename, 'NXroot', None, '')

        debug.log("Getting root attributes")

        rootDir = self._file.open( '/')
        rootAtts = self._listAttributes( rootDir)
        self._root.setAttributes( rootAtts)

        debug.log("Graphing structure")
       
        self._graph()      # use default self._root

        # create XML rep.
        from nx5.renderers.XML_FromDB import Renderer
        from pyre.weaver import Weaver
        wvr = Weaver.Weaver()
        # now need to put the component through its lifecycle
        wvr._defaults(); wvr._configure(); wvr._init()
        wvr.renderer = Renderer()

        debug.log("About to render XML structure")
        
        self._XMLrep = wvr.render( self.root())

        return


    def _makeDataset( self, name, path):
        from array_kluge import types as aktypes
        f = self._file.open( path)
        attrs = self._listAttributes( f)
        className = ''
        if 'NX_class' in attrs.keys():
            className = attrs['NX_class']

        datatype = self._getType( f)
        
        if datatype != aktypes['char']:
            dimensions = f.getSpace().info()['dims']
        else:
            dimensions = (f.getType().info()['size'],)
        
        dataset = Dataset( name, className, None, path, dimensions, datatype)
        dataset.setAttributes( attrs)                   

        return dataset


    def _getType(self, filey):
        from array_kluge import types as aktypes

        typeinfo = filey.getType().info()

        typecode = 0
        
        if typeinfo['class'] == 'float':
            if typeinfo['size'] == 32: typecode = aktypes['float'] 
            elif typeinfo['size'] == 64: typecode = aktypes['double'] 
            else:
                raise TypeError, "Unknown type length: %s" % str( typeinfo)

        elif typeinfo['class'] == 'integer':
            typestr = ''
            # determine length...
            if typeinfo['size'] == 8: typestr = 'short short'
            elif typeinfo['size'] == 16: typestr = 'short'
            elif typeinfo['size'] == 32: typestr = 'long'
            elif typeinfo['size'] == 64: typestr = 'long'
            else:
                raise TypeError, "Unknown type length: %s" % str(typeinfo)
            # ... and whether it's signed
            if typeinfo['signed'] == 0: typecode = aktypes['u' + typestr]
            elif typeinfo['signed'] == 1: typecode = aktypes[typestr]
            else:
                raise TypeError, "Unknown type signed: %s"%str(typeinfo)
        elif typeinfo['class'] == 'string':
            typecode = aktypes['char']

        else:
            errstr = "Unknown representation: %s" % str(typeinfo)
            raise TypeError, errstr
        
        return typecode
    

        
    def _makeGroup( self, name, path):

        subdir = self._file.open( path)
        attrs  = self._listAttributes( subdir)
        className = ''
        if 'NX_class' in attrs.keys():
            className = attrs['NX_class']

        group  = Group( name, className, None, path)
        group.setAttributes( attrs)

        return group    
   

#helper
def _checkFileValid(filename):
    import os
    if os.path.isfile(filename): return
    else:
        errstr = 'Invalid file name "%s"'%filename 
        raise IOError,errstr
    
# version
__id__ = "$Id: File_original.py 30 2005-03-26 00:58:16Z tim $"

# End of file
