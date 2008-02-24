#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved
from histogram.Histogram import Histogram

class EnergyPixelData( Histogram):
    """A pixel's data, with energy bin boundaries"""

    def pixel( self):
        """id of pixel which took these data"""
        return self._pixel


    def position( self):
        """position of this pixel"""
        return self._position
    
    
    def energy( self):
        """energy for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def energyUnit( self):
        """unit for energy"""
        return self._energyUnit


    def __init__( self, intensity, intensityError, intensityUnit, energy,
                  energyUnit, position, pixel, name="pixelData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[energy])

        self._intensityUnit = intensityUnit
        self._energyUnit = energyUnit
        self._position = position
        self._pixel = pixel

        return




# version
__id__ = "$Id$"

# End of file
