#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from HDFVisitor import HDFVisitor
from h5py import File
#from hdf5fs.h5fs import H5fs
#from hdf5fs.h5space import H5space
#from hdf5fs.h5type import H5type
#from hdf5fs.typeUtils import nx2c, py2nx
from array_kluge import pylist2vptr as p2v

import journal
debug = journal.debug("nx5.renderers")


DEFAULT_CHUNK_SIZE = 10

class Renderer( HDFVisitor):
    """Visitor that constructs an HDF5 file as it is escorted around a
    file DB object"""
    

    def __init__( self, filename, mode = 'w', force = False, fs = None,
                  writeData = True, datasetWriter = None):
        """Renderer( filename, mode = 'w', force = False, fs = None,
                     writeData=True, dataWriter=None)
        Create new File_FromGraph renderer.
        Inputs:
            filename
            mode: 'w' to write on existing file, 'c' to create/truncate-existing
            force: if mode is 'c', will not truncate existing file unless force
                   is set to True
            fs: pass existing filesystem interface to use that rather than
                create new one.
            writeData: whether to write data (default True)
            dataWriter: object that knows how write a buffer to hdf.
        Output: new Renderer
        Exceptions: IOError (if asked to truncate existing file)"""

        if mode == 'c' and force == False:
            self.__checkFilename( filename)
        self._filename = filename
                    
        if fs is None:
            fs = File( filename, mode)
            
        self._fs = fs
        self._writeData = writeData

#        if datasetWriter is None:
#            import nx5.file
#            datasetWriter = nx5.file.writer()
#        self._dsetWriter = datasetWriter

        return


    def render( self, doc):
        debug.log("rendering %s" % doc)
        return doc.identify( self)
    

    def onGroup( self, group):
        subdir = None
        try:
            if group.path() != '/':
                subdir = self.__makeDir( group)
            else:
                debug.log("group.path is '%s'" % group.path())
                subdir = self._fs.open('/')
        except SystemError, msg:
            debug.log( str(msg))
            debug.log( "group name: %s, class name: %s, path: %s" % \
                       (group.name(), group.className(), group.path()))
##             print msg
##             print group.name(), group.className(), group.path()
            raise
            
        self.__assignAttributes( subdir, group)

        # descend
        for child in group.children():
            child.identify( self)
        
        return


    def onDataset( self, dataset):
        """onDataset( dataset) -> None
        render a nexml dataset node to an hdf5fs "file" (dataset)"""
        newfile = self.__makeFile( dataset)
        self.__assignAttributes( newfile, dataset)
        if self._writeData is True and dataset.storage() is not None:
            self.__writeData( dataset)
        return


    def __assignAttributes(self, target, source):
        try:
            return self.__assignAttributes_imp( target, source )
        except Exception , err:
            raise err.__class__, "Unable to assign attributes to %s" % (
                source.name(), )
        raise "Should not reach here"


    def __assignAttributes_imp( self, target, source):
        attrs = dict(source.attributes())
        keys = attrs.keys()
        if 'name' not in keys:
            attrs['name'] = source.name()
        if 'class' not in keys:
            attrs['class'] = source.className()
            
        for name, value in attrs.items():
            ## debug.log("attribute name: %s, value: '%s'" % (name, value))
            # make buffer, load value into buffer

            # TO DO: have this work done by hdf5fs.attr.Attribute

            try:
                attrNXType = py2nx[ str(value.__class__.__name__)]
            except KeyError:
                value = "%r" % value
                attrNXType = py2nx[ str(value.__class__.__name__)]
            if attrNXType == 4:
                vallist = list(value)
                buff = p2v( vallist, attrNXType)
                if len( vallist) != 0:
                    dims = [len( list(value))]
                else:
                    dims = None
            else:
                buff = p2v( [value], attrNXType)
                dims = None
            attrtype = self.__makeType( attrNXType)
            attrspace = self.__makeSpace( dims)
            target.setattr( name, buff, attrtype, attrspace)
        return


    def __checkFilename( self, filename):
        import os
        if os.path.isfile( filename):
            raise IOError, "file %s already exists" % filename
        return


    def __makeDir( self, group):
        path = group.path()
        self._fs.mkdir( path)
        subdir = self._fs.open( path)
        return subdir


    def __makeFile(self, dataset):
        try: return self.__makeFile_imp( dataset )
        except Exception, err:
            d = dataset.storage().asList()
            msg = "Unable to 'makeFile' for %s"\
                  "(datatype=%s, dimensions=%s, data=%s): %s" % (
                dataset.name(), dataset.datatype(), dataset.dimensions(),
                d, err)
            raise err.__class__, msg


    def __makeFile_imp( self, dataset):
        path = dataset.path()
        thetype = self.__makeType( dataset.datatype())
        thespace = self.__makeSpace( dataset.dimensions())
        compression, chunksize = self.__getCompressionParameters(dataset)
        newfile = self._fs.open(
            path, thetype, thespace,
            compression=compression, chunksize=chunksize)
        return newfile


    def __getCompressionParameters(self, dataset):
        try:
            compression = dataset.compression
        except AttributeError:
            return 0, 0
        level = compression.level
        chunksize = compression.chunksize
        if not chunksize:
            dims = dataset.dimensions()
            chunksize = min( dims + [DEFAULT_CHUNK_SIZE] )
        return level, chunksize
        

    def __makeSpace( self, dimensions):

        try:
            space = H5space( tuple(dimensions))
        except TypeError:
            space = H5space()
        except Exception, msg:
            raise IOError, "Unable to create data space with dimensions=%s: %s, %s" % ( dimensions, msg.__class__, msg )
        return space 


    def __makeType( self, datatype):
        typestr = nx2c[ datatype]
        thetype = H5type( typestr)
        return thetype

    
    def __writeData( self, dataset):
        """__writeData( fileobj, dataset) -> None
        write the data associated with a nexml dataset to the file's dataset.
        Inputs:
            dataset: nexml dataset object with non-null storage member.
        Output:
            None
        Exceptions: FIX ME: find out
        Notes: (1) Uses whatever datasetWriter the user registered with the
        renderer at construction. The consistency of the storage member and
        the datasetWriter is not currently checked."""
        from nx5.file.Selector import Selector
        selector = Selector( self._filename, self._fs)
        selector.select( dataset.path())
        self._dsetWriter.write( selector, dataset.storage())

        return


# version
__id__ = "$Id: File_FromGraph.py 143 2009-01-05 00:05:03Z linjiao $"

# End of file
