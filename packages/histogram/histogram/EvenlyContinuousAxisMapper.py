#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


## \namespace histogram::EvenlyContinuousAxisMapper
##
## provides an axis mapper that maps value to axis index for continous axis
##
## The name is weird. The real meaning of that name is a mapper of a continuous
## axis which is represent by a sequence of evenly-spaced numbers


from AxisMapper import AxisMapper

class EvenlyContinuousAxisMapper(AxisMapper):

    """
    map a value in an continuous Axis to a index.

    The axis is represented by an evenly-spaced numbers (bin boundaries)
    """

    def __init__(self, minBinBoundaries=None, binSize=None, nBinBoundaries=None,
                 binBoundaries = None):
        if binBoundaries is not None :
            assertEvenlySpaced( binBoundaries )
            bb = binBoundaries
            minBinBoundaries = bb[0]
            if len(bb) < 2 : raise "Too few bin boundaries: %s" % len(bb)
            binSize = bb[1] - bb[0]
            nBinBoundaries = len(bb)
        self._minBB = minBinBoundaries
        self._binSize = binSize
        self._nBB = nBinBoundaries
        self._maxBB = minBinBoundaries + (nBinBoundaries-1)*binSize
        return
    

    def __call__(self, value):
        if value < self._minBB or value >= self._maxBB:
            raise IndexError, "%s out of bounds (%s,%s)" % (
                value, self._minBB, self._maxBB)
        from math import floor
        return int ( floor ( (value-self._minBB)/self._binSize) ) 
        

    pass # end of EvenlyContinuousAxisMapper


class NotEvenlySpaced( Exception ): pass

def assertEvenlySpaced ( bb ):
    if len(bb) < 2: raise "Too few bin boundaries: %s" % len(bb)
    d0 = bb[1] - bb[0]
    for i in range( 1, len(bb) - 1 ):
        d = bb[i+1] - bb[i]
        if abs((d-d0)/d0) > 1e-8: raise NotEvenlySpaced, "%s is not a evenly spaced array" % (bb,)
        continue
    return
