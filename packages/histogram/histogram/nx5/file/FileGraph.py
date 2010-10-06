#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.file.FileGraph")

from nx5.nexml.elements.Group import Group

class FileGraph( object):
    """Holds object graph that represents the structure of an HDF5 file"""


    def addNode( self, node):
        """Add new node to node at path.
        Inputs:
            path: string, path sep is '/'
            node: node (nexml.elements.NexusElement subclass instance)
                  to add to graph
        Output: None
        Exceptions:
            ValueError (if no such path in graph)
            TypeError (if path corresponds to non-Group)
        """

        path = node.path()

        parentPath = self.__extractParentPath( path)

        debug.log("parent path is %s" % parentPath)
        
        parentNode = self.pathToNode( parentPath)

        if parentNode is None:
            # no such path in graph:
            raise ValueError, "%s not a path in graph" % path

        if parentNode.isGroup():
            parentNode.addChild( node)
        else:
            raise TypeError, "Cannot add node to non-Group"

        return          


    def pathToNode( self, path):
        """Get the node corresponding to path request. Raises ValueError
        if no such path in the graph"""
        node = self.__pathToNode( path)
        if node is None:
            raise ValueError, "so such path '%s' in graph" % path
        return node
        

    def root( self):
        return self._root


    def __init__( self, root):
        self._root = root
        return


    # _____________________ end of public interface ___________________


    def __extractParentPath( self, path):
        """extract parent path from path"""
        pathEls = path.split('/')
        pathEls.pop()
        parentPath = '/'.join( pathEls)
        return parentPath


    def __pathToNode( self, path, start = None):
        """Find node in graph corresponding to path, starting at root node
        or at user specified start"""
        
        pathEls = path.split('/')

        debug.log("path to convert: %s" % path)
        
        while '' in pathEls:
            pathEls.remove('')

        debug.log("path elements: %s" % str(pathEls))

        if start is None:
            currentGroup = self._root
        else:
            currentGroup = start

        node = currentGroup
        debug.log("current group: %s, %s" % (node.name(), node.className()))
            
        for i, element in enumerate( pathEls):
            if element:
                debug.log("path element: %s" % element)
                node = currentGroup.getChild( element)
                if node is None:
                    debug.log("Node is None. Current group's children: %s" %
                              ["%s" % child.name() for child in currentGroup.children()])
                else:
                    debug.log("new node: %s, %s" % (node.name(), node.className()))
                if i < len( pathEls) - 1:
                    if issubclass( node.__class__, Group):
                        # recurse
                        currentGroup = node
                    else:
                        # reached end of branch before end of path
                        node = None
        return node
                    
                    
# version
__id__ = "$Id: FileGraph.py 93 2005-07-28 17:09:01Z tim $"

# End of file
