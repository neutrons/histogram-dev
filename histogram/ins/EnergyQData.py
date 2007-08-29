#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved
from histogram.Histogram import Histogram

class EnergyQData( Histogram):
    """Constant-E Slice from an S(q, E) histogram"""

    def energy( self):
        """energy of this slice"""
        return self._energy

    
    def q( self):
        """q for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def qUnit( self):
        """unit for q"""
        return self._qUnit


    def __init__( self, intensity, intensityError, intensityUnit, q,
                  qUnit, energy, name="energyData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[q])

        self._intensityUnit = intensityUnit
        self._qUnit = qUnit
        self._energy = energy

        return




# version
__id__ = "$Id$"

# End of file
