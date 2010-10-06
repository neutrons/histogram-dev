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


def load( filename, root = '/'):
    return default_unpickler.load( filename, root )


class UnPickler:

    def __init__(self, file2nxGraph = None, data_extractor = None,
                 nxGraph2objectHierarchy = None, objectHierarchy2object = None):
        if not file2nxGraph:
            from nx5.renderers.Graph_FromFile import Renderer
            file2nxGraph = Renderer()
            pass
        if not data_extractor:
            from nx5.renderers.DataExtractor import Renderer
            data_extractor = Renderer
            pass
        if not nxGraph2objectHierarchy:
            from ObjectHierarchyFromNXGraph import Renderer
            nxGraph2objectHierarchy = Renderer()
            pass
        if not objectHierarchy2object:
            from object_hierarchy.ObjectFromObjectHierarchy import Renderer
            objectHierarchy2object = Renderer()
            pass
        self.file2nxGraph = file2nxGraph
        self.data_extractor = data_extractor
        self.nxGraph2objectHierarchy = nxGraph2objectHierarchy
        self.objectHierarchy2object = objectHierarchy2object
        return
            

    def load( self, filename, root = '/'):
        fs = self._fs( filename )
        
        nxg = self.file2nxGraph.render( fs, filename, root )

        #printer.render( nxg )

        self.data_extractor(filename).render( nxg )
        
        #printer.render( nxg )
        
        objh = self.nxGraph2objectHierarchy.render( nxg )

        return self.objectHierarchy2object.render( objh )


    def _fs(self, filename):
        from hdf5fs.h5fs import H5fs
        mode = 'r'
        return H5fs( filename, mode)        

    pass # end of UnPickler


default_unpickler = UnPickler()

## from nx5.renderers.HDFPrinter import HDFPrinter
## printer = HDFPrinter()

def test():
    import journal
##     journal.debug( 'nx5.pickle' ).activate()
##     journal.debug( 'nx5.nexml' ).activate()
##     journal.debug( 'nx5.renderers.Graph_FromFile' ).activate()
    from object_hierarchy.ObjectHierarchyFromObject import testobject
    obj = testobject()
    import os
    os.remove( 'test.h5' )
    from Pickler import dump
    dump( obj, 'test.h5' )
    print UnPickler().load( 'test.h5' )
    return


if __name__ == '__main__': test()



# version
__id__ = "$Id$"

# End of file 
