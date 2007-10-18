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

def load( filename, pathinfile ):
    from nx5.renderers import *
    g = graphFromHDF5File( filename, pathinfile )
    dataExtractor( filename ).render( g )
    from Parser import Parser
    h = Parser().parse( g )
    return h


def dump( histogram, filename, pathinfile, mode = 'w' ):
    from Renderer import Renderer

    g = Renderer().render(histogram)

    from nx5.renderers import *
    pathinfile = pathinfile.split( '/' )
    p = pathinfile + [histogram.name()]
    p = '/'.join( p )
    if not p.startswith('/'): p = '/' + p
    setPath(g, p)
    #printGraph( g )

    writeGraph( g, filename, mode )
    return


# version
__id__ = "$Id$"

# End of file 
