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


def getOnlyEntry( h5filename ):
    from hdf5fs.h5fs import H5fs
    fs = H5fs( h5filename, 'r' )
    root = fs.open('/')
    entries = root.read()
    if len(entries)>1:
        msg = "Hdf5 file %s has multiple entries: %s. Please specify"\
              "the entry you want to open." % (
            h5filename, entries )
        raise RuntimeError, msg
    if len(entries)==0:
        msg = "Hdf5 file %s has no entry." % h5filename
        raise RuntimeError, msg
    
    entry = entries[0]
    return entry


# version
__id__ = "$Id$"

# End of file 
