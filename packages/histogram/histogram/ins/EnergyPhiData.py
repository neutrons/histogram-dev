#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved
from histogram.Histogram import Histogram

class EnergyPhiData( Histogram):
    """Constant-E Slice from an S(phi, E) histogram"""

    def energy( self):
        """energy of this slice"""
        return self._energy

    
    def phi( self):
        """phi for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def phiUnit( self):
        """unit for phi"""
        return self._phiUnit


    def __init__( self, intensity, intensityError, intensityUnit, phi,
                  phiUnit, energy, name="energyData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[phi])

        self._intensityUnit = intensityUnit
        self._phiUnit = phiUnit
        self._energy = energy

        return




# version
__id__ = "$Id$"

# End of file
