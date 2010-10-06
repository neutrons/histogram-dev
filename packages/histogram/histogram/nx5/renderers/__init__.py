#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved




def graphFromObjectOfStaticStructure( obj, template ):
    from GraphFromObjectOfStaticStructure import Renderer
    graph = Renderer(template).render( obj )
    return graph

def printGraph(graph):
    from HDFPrinter import HDFPrinter
    HDFPrinter().render( graph )
    return

def setPath(graph, *args, **kwds):
    from SetPath import Renderer
    Renderer().render( graph, *args, **kwds )
    return

def writeGraph(graph, filename, *args, **kwds):
    from File_FromGraph import Renderer
    Renderer( filename, *args, **kwds ).render(graph)
    return

def graphFromHDF5File( filename, path = '/', fs = None):
    if fs is None:
        from hdf5fs.h5fs import H5fs
        mode = 'r'
        fs = H5fs( filename, mode)

    from nx5.renderers.Graph_FromFile import Renderer
    renderer = Renderer()

    graph = renderer.render( fs, filename, path)

    return graph


def dataExtractor( filename ):
    from DataExtractor import Renderer
    return Renderer( filename )


# version
__id__ = "$Id: __init__.py 143 2009-01-05 00:05:03Z linjiao $"

# End of file
