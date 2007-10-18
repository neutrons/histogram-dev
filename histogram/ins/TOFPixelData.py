#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from histogram.Histogram import Histogram

class TOFPixelData( Histogram):
    
    def pixel( self):
        """id of pixel which took these data"""
        return self._pixel


##     def position( self):
##         """position of this pixel"""
##         return self._position
    
    
    def tof( self):
        """tof for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def tofUnit( self):
        """unit for tof"""
        return self._tofUnit


    def __init__( self, intensity, intensityError, intensityUnit, tof, tofUnit,
                  pixel, name="pixelData"):
                  #position, pixel, name="pixelData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[tof])

        self._intensityUnit = intensityUnit
        self._tofUnit = tofUnit
        #self._position = position
        self._pixel = pixel

        return


# version
__id__ = "$Id$"

# End of file
