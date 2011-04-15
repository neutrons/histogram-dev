#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# this sub package depends on h5py, so we test it first
try:
    import h5py
except ImportError:
    raise RuntimeError, "Please install h5py"


import os
def load( filename, pathinfile=None, fs = None, **kwds ):
    '''load(filename, path_in_hdf_file ): load histogram from a hdf file

    filename:
      The hdf filename where the histogram is saved
      This version only supports hdf5
    path_in_hdf_file:
      The path inside the hdf file where the histogram is located.

    return:
      The histogram loaded.
    '''
    # if pathinfile is not specified explicity
    if pathinfile is None:
        # it could be that there is only one entry 
        # in the histogram file, let us try that
        if os.path.exists(filename):
            from utils import getOnlyEntry
            try:
                pathinfile = getOnlyEntry(filename)
            except:
                msg = (
                    "Cannot guess the entry of the histogram in %s."
                    "Please explicitly specify the entry "
                    "by keyword 'pathinfile'"
                    ) % filename
                raise ValueError, msg
        # or it could be the first argument is an url
        # that has both the file path and the entry name
        else:
            # this is obsolete. in the future we should have
            # a dedicated "url" parameter
            import warnings
            warnings.warn("filename as url is deprecated")
            url = filename
            filename, pathinfile = os.path.split(url)
            if not os.path.exists(filename):
                msg = "invalid histogram url: %s" % url
                raise ValueError, url
            
    if fs is None:
        from h5py import File
        try:
            fs = File( filename, 'r')
        except IOError, msg:
            raise IOError, "unable to load histogram. filename=%s, "\
                "pathinfile=%s, kwds=%s" % (filename, pathinfile, kwds)
    from Loader import Loader
    loader = Loader(fs, pathinfile)
    return loader.load(**kwds)


def dump( histogram, filename = None, pathinfile = '/', 
          mode = 'c', fs = None, compression = 'lzf'):
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
    #g = graphFromHDF5File( filename, pathinfile, fs = fs )
    pathinfile = pathinfile.split( '/' )
    p = pathinfile + [histogram.name()]
    p = '/'.join( p )
    if not p.startswith('/'): 
        p = '/' + p
    writeCodes = {'c':'w','w':'a'}
    if fs is None:
        from h5py import File
        fs = File(filename, writeCodes[mode])
        Renderer(fs, compression).render(histogram)
        fs.close()
    else:
        Renderer(fs, compression).render(histogram)


# version
__id__ = "$Id$"

# End of file 
