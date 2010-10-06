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


def dump(obj, filename, mode = 'c', root = '/'):
    default_pickler.dump( obj, filename, mode, root )
    return


from nx5.renderers.SetPath import Renderer as SetPath

class Pickler:

    def __init__(self, obj2objHierarchy = None, objHierarchy2nxGraph = None,
                 nxGraph2file_factory = None):
        if not obj2objHierarchy:
            from object_hierarchy.ObjectHierarchyFromObject import Renderer 
            obj2objHierarchy = Renderer()
            pass
        if not objHierarchy2nxGraph:
            from NXGraphFromObjectHierarchy import Renderer
            objHierarchy2nxGraph = Renderer()
            pass
        if not nxGraph2file_factory:
            from nx5.renderers.File_FromGraph import Renderer
            nxGraph2file_factory = Renderer
            pass
        self.obj2objHierarchy = obj2objHierarchy
        self.objHierarchy2nxGraph = objHierarchy2nxGraph
        self.nxGraph2file_factory = nxGraph2file_factory
        self.setPath = SetPath()
        return
            

    def dump( self, obj, filename, mode = 'c', root = '/'):
        nxg = self.objHierarchy2nxGraph.render( self.obj2objHierarchy.render( obj ) )
        self.setPath.render( nxg, root )
        #printer.render( nxg )
        self.nxGraph2file_factory( filename, mode ).render( nxg )
        return


    pass # end of Pickler



default_pickler = Pickler()


## from nx5.renderers.HDFPrinter import HDFPrinter
## printer = HDFPrinter ()


def test():
    from object_hierarchy.ObjectHierarchyFromObject import testobject
    obj = testobject()
    Pickler().dump( obj, 'test.h5' )
    return


if __name__ == '__main__': test()



# version
__id__ = "$Id$"

# End of file 
