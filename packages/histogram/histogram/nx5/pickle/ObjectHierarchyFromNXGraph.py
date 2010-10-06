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




from nx5.nexml.elements.Dataset import Dataset
from nx5.nexml.elements.Group import Group
from nx5.nexml.elements.Nexus import Nexus
from storage import storage_type_name
from types import *
import sys


class Renderer:

    def __init__(self):
        return


    def render(self, nxgraph):
        return nxgraph.identify(self)


    def onNexus(self, node):
        children = node.children()
        return children[0].identify(self)
    

    def onGroup(self, node):
        if node.className() == "NXroot" : return self.onNexus( node )
        klass = self.findClass(node.className())
        name = node.name()
        branch = klass( name )

        children = list(node.children())
        children.sort( compareIndex )
        for child in children:
            branch.addLeaf( child.identify( self ) )
            continue
        
        return branch


    def onDataset(self, node):
        className = node.className()
        if className == storage_type_name:
            return self.findClass( 'Builtin' )( node.name(), node.storage() )

        if className == "EmptyString":
            #special treatment of empty string
            #please refer to NXGraphFromObjectHierarchy
            className = "String"
            data = ''
        else:
            storage = node.storage()
            data = self.dispatch[ className ]( self, storage )
            pass
        
        klass = self.findClass(className)
        name = node.name()
        leaf = klass(name, data)
        return leaf


    dispatch = {}
    
    def onString(self, storage): return storage.asList()
    dispatch[ 'Global' ] = dispatch['Link'] = dispatch['String'] = onString


    def onBuiltin(self, storage): return storage.asList()[0]
    dispatch['Bool'] = dispatch[ 'Integer' ] = dispatch['Long'] = dispatch['Float'] = onBuiltin


    def onNone(self, storage): return None
    dispatch['NoneType'] = onNone


    def findClass(self, name):
        if name in ['NoneType', 'String', 'Integer', 'Float', 'Long', 'Bool']: name = 'Builtin'
        module = "object_hierarchy.%s" % name
        m = __import__( module, globals() )
        return getattr( getattr(m, name), name )

    pass # end of Renderer



#helpers

def _index(node): return int(node.getAttribute( 'sortIndex' ) )

def compareIndex( node1, node2 ):
    if node1 == node2: return 0
    return _index(node1) - _index(node2)


import os
path = os.path.split(__file__)[0]


def test():
    from object_hierarchy.ObjectHierarchyFromObject import Renderer as O2OH, testobject
    obj = testobject()
    oh = O2OH().render( obj )

    from NXGraphFromObjectHierarchy import Renderer as OH2NXG
    nxg = OH2NXG().render( oh )

    from nx5.renderers.HDFPrinter import HDFPrinter
    HDFPrinter().render( nxg )

    oh = Renderer().render( nxg )
    from object_hierarchy.Printer import Printer as OHPrinter
    print '\n'.join(OHPrinter().render( oh ))
    return



if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
