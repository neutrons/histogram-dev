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


def axis(*args, **kwds):
    from Axis import Axis
    return Axis( *args, **kwds )


def grid(*args, **kwds):
    from Grid import Grid
    return Grid( *args, **kwds )


def histogram(*args, **kwds):
    from Histogram import Histogram
    return Histogram( *args, **kwds )


def ndArray(*args, **kwds):
    from NdArray import NdArray
    return NdArray( *args, **kwds )


def h5DataSource(*args, **kwds):
    from H5DataSource import H5DataSource
    return H5DataSource( *args, **kwds )


def physicalValueNdArray(*args, **kwds):
    from PhysicalValueNdArray import PhysicalValueNdArray
    return PhysicalValueNdArray( *args, **kwds )



# version
__id__ = "$Id$"

# End of file 
