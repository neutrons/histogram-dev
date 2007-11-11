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

def load( filename, pathinfile=None, **kwds ):
    if pathinfile is None:
        import os
        filename, pathinfile = os.path.split( filename )
    from nx5.renderers import *
    g = graphFromHDF5File( filename, pathinfile )
    from Parser import Parser
    h = Parser(filename).parse( g )
    return h.fetch(**kwds)


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
