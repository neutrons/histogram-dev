#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from histogram.Histogram import Histogram

class SPhiEData( Histogram):
    """Data as a function of scattering angle and energy"""
    
    def energy( self):
        """tof for this monitor/measurement"""
        return self._axisCont.datasetFromId( 2)


    def energyUnit( self):
        """unit for tof"""
        return self._energyUnit


    def q( self):
        """tof for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def qUnit( self):
        """unit for tof"""
        return self._phiUnit


    def __init__( self, intensity, intensityError, intensityUnit,
                  q, qUnit, energy, energyUnit, name="SQEData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[ q, energy])

        self._intensityUnit = intensityUnit
        self._energyUnit = energyUnit
        self._qUnit = qUnit
        self._position = position
        self._pixel = pixel

        return




# version
__id__ = "$Id$"

# End of file
