#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from nx5.renderers.HDFVisitor import HDFVisitor

import journal
debug = journal.debug("nx5.renderers.SetPath")


class Renderer( HDFVisitor):
    
    """set path of each node"""


    def __init__( self):
        self._curPath = None
        return


    def render( self, doc, rootpath = None):
        if rootpath is None: rootpath = doc.path()
        else: doc._pathstr = rootpath
        
        if rootpath == '': doc._pathstr = rootpath = '/'
        
        self._curPath = '/'.join( rootpath.split('/')[:-1])
        return doc.identify( self)
    

    def onGroup(self, group):
        #save path
        _save = self._curPath
        self._updatePath( group )
        # descend
        for child in group.children():
            child.identify( self)
            pass
        #restore
        self._curPath = _save
        return


    def onDataset( self, dataset):
        #save path
        _save = self._curPath
        self._updatePath(dataset)
        #restore
        self._curPath = _save
        return


    def _updatePath( self, node):
        curPath = self._curPath
        from string import join
        path = node.path()
        if path is None or path == '': path = node.name()
        last = path.split('/')[-1]
        self._curPath = '/'.join( [curPath, last] ).replace('//', '/')
        node._pathstr = self._curPath



# version
__id__ = "$Id$"

# End of file 
