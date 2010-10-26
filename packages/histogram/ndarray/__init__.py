#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

## \mainpage ndarray
## ndarray is a layer of python classes between histogram and arrays (or vectors).
##
## histogram needs ways to store data. In python, numpy is a good way to handle
## large multi-dimensional arrays. But we don't want to tie ourselves to
## a pariticular python array package. This ndarray package keeps track of
## what histogram needs from the array and creates an abstract base class
## NdArray.NdArray.
##
## Currently there are two implementations for NdArray.NdArray:
##
##   - NumpyNdArray.NdArray
##
## NumpyNdArray.NdArray is a wrapper of numpy.ndarray
##



# version
__id__ = "$Id$"

# End of file 
