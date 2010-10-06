#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved


## \namespace stdVector::Slice
##
## provides interface to std::slice c++ class
##


from CObject import CObject 
import stdVector

class Slice( CObject):
    """Interface to std C++ slice object"""

    def size( self):
        return stdVector.slice_size( self._handle)


    def start( self):
        return stdVector.slice_start( self._handle)


    def stride( self):
        return stdVector.slice_stride( self._handle)


    def __init__( self, start, size, stride):
        handle = stdVector.slice_ctor3( start, size, stride)
        CObject.__init__( self, handle, "Slice")
        return

    def magicNumber( self):
        return stdVector.slice_magicNumber()
    

# version
__id__ = "$Id: Slice.py 134 2006-10-09 15:21:57Z linjiao $"

# End of file
