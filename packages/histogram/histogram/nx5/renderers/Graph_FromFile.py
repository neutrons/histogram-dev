#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from nx5.nexml.elements.Group import Group
from nx5.nexml.elements.Dataset import Dataset
from nx5.nexml.elements import Instrument, DetectorPack, DetectorArray, LPSD,\
     LPSDPixel, Moderator, Monitor

import journal
debug = journal.debug( "nx5.renderers.Graph_FromFile")
debug2 = journal.debug( "nx5.refcount")

import sys

class Renderer( object):
    """Make an object graph given an HDF5 fs object"""


    def render( self, fs, filename, path = '/'):

        debug2.log("reference count of fs.h5ref: %s" %
                   sys.getrefcount( fs.h5ref))
        # for convenience
        self._file = fs
        debug2.log("reference count of fs.h5ref: %s" %
                   sys.getrefcount( fs.h5ref))

        debug.log("Rendering %s" % filename)

        name = path.split('/')[-1]
        if len(name)==0: name = filename
        root = Group( name, 'NXroot', None, '')
        root._pathstr = path

        self.__graph( root)
        debug.log("Rendering complete")

        # clean
        self._file = None
        debug2.log("reference count of fs.h5ref: %s" %
                   sys.getrefcount( fs.h5ref))
        
        return root
    

    def __graph(self, vgroup):
        """_graph( group) -> None
        Graph a group. """
        
        self.__expandGroup( vgroup)

        return None


    def __expandGroup( self, group):
        """Recurse down a level, graph what's there
        """
        path = group.path()
        if not path: path = '/'

        debug.log( "expanding group " + group.name() + " " + 
                   group.className() + " " + group.path())

        directory = self._file.open( path)

        debug.log("opened %s" % path)

        subgroups, children, sorted = self.__listDir( directory)

        group.update( children, subgroups, sorted = sorted)

        for subgroup in subgroups:
            self.__graph( subgroup)
        return
    

    def __listDir( self, directory):
        """
        """
        subgroups = []; children = {}; sorted = []

        debug.log("reading directory")
        
        items = directory.read()

        debug.log("directory read, items are: %s" % items)
        
        for item in items:
            path = ''
            if directory.path == '/':
                path = '/'+item
            else:
                path = '/'.join( (directory.path, item))
            debug.log("about to stat %s" % path)
            stat = self._file.stat( path)
            debug.log("stat['type'] = %s" % stat['type'])
            
            if   stat['type'] == 'directory':
                node = self.__makeGroup( item, path)
                subgroups.append( node)
                
            elif stat['type'] == 'file':
                try:
                    node = self.__makeDataset( item, path)
                except Exception, msg:
                    debug.log( "failed to create dataset from %s, %s: Unknown data type.\nException raised: %s,%s" % (item, path, msg.__class__.__name__, msg) )
                    node = None
                    pass

            else:
                node = None
                debug.log("Unrecognized type")
                
            if node:
                children[ node.name()] = node
                sorted.append( node.name() )
                
        debug.log("finis")
        return subgroups, children, sorted


    def __listAttributes( self, attributee):
        """Returns a dictionary of the attributes for something with a listattr
        method."""

        attributes = {}

        atts = attributee.listattr()
##         debug.log("attributes: %s" % str(["%s" % att.name() for att in atts]))

        for att in atts:
##             debug.log("looking at attribute '%s'" % att.name())
            attributes[att.name()] = att.value()
##             debug.log( "attributes[%s] = %s" % (att.name(), att.value()))
        return attributes

    
    def __makeDataset( self, name, path):
        
        from array_kluge import types as aktypes

        f = self._file.open( path)
        attrs = self.__listAttributes( f)
        className = ''
        if 'NX_class' in attrs.keys():
            className = attrs['NX_class']
        elif 'class' in attrs.keys():
            className = attrs['class']

        datatype = self.__getType( f)
        
        if datatype != aktypes['char']:
            dimensions = f.getSpace().info()['dims']
        else:
            dimensions = (f.getType().info()['size'],)
        
        dataset = Dataset( name, className, None, path, dimensions, datatype)
        dataset.setAttributes( attrs)                   

        return dataset

        
    def __makeGroup( self, name, path):

        subdir = self._file.open( path)
##         debug.log("subdirectorty opened")
        attrs  = self.__listAttributes( subdir)
##         debug.log("group attributes: %s" % attrs)
        className = ''

        keys = attrs.keys()
        if 'NX_class' in keys:
            className = attrs['NX_class']
        elif 'class' in keys:
            className = attrs['class']
##         else:
##             debug.line("did not find class in directory attributes")
##             debug.log("Directory attribute keys: %s" % keys)

        knownClasses = ['Instrument', 'DetectorArray', 'DetectorPack', 'LPSD',
                        'LPSDPixel', 'Moderator', 'Monitor']

        if className in knownClasses:
            if className == 'Instrument':
                group = Instrument.Instrument( name, className, None, path)
            elif className == 'DetectorArray':
                group = DetectorArray.DetectorArray( name, className, None,
                                                     path)
            elif className == 'DetectorPack':
                group = DetectorPack.DetectorPack( name, className, None, path)
            elif className == 'LPSD':
                debug.log("className = 'LPSD'")
                group = LPSD.LPSD( name, className, None, path)
            elif className == 'LPSDPixel':
                group = LPSDPixel.LPSDPixel( name, className, None, path)
            elif className == 'Moderator':
                group = Moderator.Moderator( name, className, None, path)
            elif className == 'Monitor':
                group = Monitor.Monitor( name, className, None, path)
        else:
            debug.log( "making group with name %s, path %s" % (name,path))
            group  = Group( name, className, None, path)
            debug.log("new group's name is %s" % group.name())
        # ensure we don't trample name, etc.
        usedKeys = ['name', 'NX_class', 'class']
        newAttrs = {}
        for key in attrs.keys():
            if key not in usedKeys:
                newAttrs[ key] = attrs[key]
        group.setAttributes( newAttrs)
        debug.log("new group's className is %s" % group.__class__.__name__)

        return group    
   

    def __getType(self, filey):
        """Determine the correct typecode for object in fs"""
        from hdf5fs.typeUtils import getNativeTypeCode as getCode
        typeinfo = filey.getType().info()
        return getCode(typeinfo)
    

# version
__id__ = "$Id: Graph_FromFile.py 136 2007-10-05 12:54:52Z linjiao $"

# End of file
