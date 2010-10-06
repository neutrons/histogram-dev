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


## Convert an "object hierarchy" to a HDF graph
##
## This module is one step in pickling python objects to HDF files.
##
##   python object --> object hierearchy --> hdf graph --> hdf file
##
## This module is for the 2nd arrow.
##
## One thing that is tricky is about c arrays or vectors.
## They corresponds to Dataset in HDF file format.
## We would like to convert them directly to Dataset instead of using
## "state" discovered by __getstate__ or __dict__.
##
## Instances of those array types and vector types should be
## directly converted to Dataset node, with node._storage = array/vector


from nx5.nexml.elements.Dataset import Dataset
from nx5.nexml.elements.Group import Group
from nx5.nexml.elements.Nexus import Nexus


from storage import builtin2storage, storage_nexml, storage_type, storage_type_name

from nx5.renderers.GraphFromObjectOfStaticStructure import Renderer as SimpleObject2Graph
from types import *
from object_hierarchy.Instance import Instance


class Renderer:

    def __init__(self):
        return


    def render(self, objHierarchy):
        self._sortIndex = 0
        g = objHierarchy.identify(self)
        root = Nexus( objHierarchy.name, 'NXroot', None, '' )
        root.addChild( g )
        from nx5.renderers.SetPath import Renderer as SetPath
        SetPath().render( root )
        return root


    def onBranch(self, node):
        if isinstance( node, Instance ) and type(node.instance) == storage_type:
            klass = storage_type_name
            return self.onStorage( node.name, klass, node.instance )

        nexml = os.path.join( nexmlpath, "group.nexml" )
        g = self._renderGraph( node, nexml )
        for i, leaf in enumerate(node.leaves):
            self._sortIndex = i # have to some how remember the sequence
            node = leaf.identify(self)
            g.addChild( node )
            continue
        return g


    onInstance = onConstruction = onTuple = onList = onDict = onBranch


    def onStringLeaf(self, leaf):
        klass = leaf.__class__.__name__
        return self.onStorage( leaf.name, klass, builtin2storage( 'string', leaf.data ) )


    onGlobal = onLink = onStringLeaf


    def onBuiltin(self, b):
        return self.dispatch( type(b.data) )(self, b)


    _handlers = {}
    def dispatch(self, t):
        return self._handlers[ t ]


    def onNone(self, node):
        klass = "NoneType"
        return self.onStorage( node.name, klass, builtin2storage( 'string', "None" ) )
    _handlers[ NoneType ] = onNone


    def onString(self, node):
        klass = "String"
        if node.data == '':
            # hdf5 does not like empty dataset
            klass = "EmptyString"
            node.data = ' '
        return self.onStorage( node.name, klass, builtin2storage( 'string', node.data ) )
    _handlers[ StringType ] = onString


    def onInteger(self, node):
        klass = "Integer"
        return self.onStorage( node.name, klass, builtin2storage( 'int', node.data ) )
    _handlers[ IntType ] = onInteger


    def onBool(self, node):
        klass = "Bool"
        return self.onStorage( node.name, klass, builtin2storage( 'int', node.data ) )
    _handlers[ bool ] = onBool


    def onLong(self, node):
        klass = "Long"
        return self.onStorage( node.name, klass, builtin2storage( 'long', node.data ) )
    _handlers[ LongType ] = onLong


    def onFloat(self, node):
        klass = "Float"
        return self.onStorage( node.name, klass, builtin2storage( 'float', node.data ) )
    _handlers[ FloatType ] = onFloat



    def onStorage(self, name, klass, storage):
        storage.name = name
        storage.klass = klass
        return self._renderGraph( storage, storage_nexml )
        

    def _renderGraph( self, obj, template_file):
        f = template_file
        obj._sortIndex = self._sortIndex
        return SimpleObject2Graph( f ).render( obj ).children()[0]


    pass # end of Renderer



#helpers

import os
from nexmlpath import nexmlpath


def test():
    from object_hierarchy.ObjectHierarchyFromObject import Renderer as O2OH, testobject
    a = testobject()
    graph = O2OH().render( a )
    
    hdfg = Renderer().render( graph )

    from nx5.renderers.HDFPrinter import HDFPrinter
    HDFPrinter().render( hdfg )
    return



if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
