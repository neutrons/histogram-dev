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

def load( filename, pathinfile=None, fs = None, **kwds ):
    '''load( hdf_filename, path_in_hdf_file ): load histogram from a hdf file

    hdf_filename:
      The hdf filename where the histogram is saved. This version only supports hdf5
    path_in_hdf_file:
      The path inside the hdf file where the histogram is located.

    return:
      The histogram loaded.
    '''
    if pathinfile is None:
        import os
        filename, pathinfile = os.path.split( filename )
    from nx5.renderers import graphFromHDF5File
    try:
        g = graphFromHDF5File( filename, pathinfile, fs = fs )
    except IOError, msg:
        raise IOError, "unable to load histogram. filename=%s, "\
              "pathinfile=%s, kwds=%s" % (
            filename, pathinfile, kwds)
    from Parser import Parser
    h = Parser(filename, fs = fs).parse( g )
    return h.fetch(**kwds)


def dump( histogram, filename = None, pathinfile = '/', mode = 'w', fs = None, compression = 0):
    '''dump( histogram, hdf_filename, path_in_hdf_file, mode ) -> save histogram into a hdf file.

    histogram:
      The histogram to be written
    hdf_filename:
      The hdf filename in which the histogram will be saved
    path_in_hdf_file:
      The path inside the hdf file where the histogram is located.
    mode:
      The mode to be used to write to the hdf file.
      'c': create new hdf file. If hdf file of the same name exists, this command will fail.
      'w': write to existing hdf file. If the path_in_hdf_file already exists in the hdf file, this command will fail.
    compression:
      The compression ratio. If it is 0, no compression will be done.
      The valid values are integers from 0 to 9 (inclusive).
    '''
    from Renderer import Renderer

    g = Renderer(compression).render(histogram)

    from nx5.renderers import setPath, writeGraph, printGraph
    pathinfile = pathinfile.split( '/' )
    p = pathinfile + [histogram.name()]
    p = '/'.join( p )
    if not p.startswith('/'): p = '/' + p
    setPath(g, p)
    #printGraph( g )

    writeGraph(g, filename, mode=mode, fs=fs)
    return


# version
__id__ = "$Id$"

# End of file 
