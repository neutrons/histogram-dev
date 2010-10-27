#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def getOnlyEntry( h5filename ):
    from h5py import File
    fs = File(h5filename, 'r')
    histogramNames = list(fs)
    if len(histogramNames)>1:
        msg = "Hdf5 file %s has multiple entries: %s. Please specify"\
              "the entry you want to open." % (
            h5filename, histogramNames )
        raise RuntimeError, msg
    if len(histogramNames)==0:
        msg = "Hdf5 file %s has no entry." % h5filename
        raise RuntimeError, msg
    
    entry = histogramNames[0]
    return entry


# version
__id__ = "$Id$"

# End of file 
