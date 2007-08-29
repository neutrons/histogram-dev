#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

#
#from reduction import reduction

#from stdVector.Slice import Slice

from histogram.Histogram import Histogram
from histogram.SlicingInfo import SlicingInfo, all

class SQEData( Histogram):
    """Data as a function of scattering angle and energy"""

    

    def addEnergySlice( self, energy, energyQData):
        """addEnergySlice( energy, energyQData) -> None
        add a constant energy slice into S(Q,E) histogram"""
        self[ all, energy ] += energyQData
        return
        

    def oldaddEnergySlice( self, energy, energyQData):
        """addEnergySlice( energy, energyQData) -> None
        add a constant energy slice into S(Q,E) histogram"""
        # map energy to index
        energyList = self.energy().storage().asList()
        from math import floor
        de = energyList[1] - energyList[0]
        eIndex = int( floor( (energy - energyList[0])/de) )

        numEnergies = len(energyList) - 1
        numQ = len( self.q().storage().asList()) - 1

        start = eIndex
        size = numQ
        stride = numEnergies
        
        eslice = Slice( start, size, stride)
        sourceVector = energyQData.data().storage()
        sourceErrorVector = energyQData.errors().storage()
        
        # accumulate data
        reduction.accumulate( self.data().storage().handle(),
                              sourceVector.handle(),
                              sourceVector.datatype(),
                              eslice.handle())

        # accumulate errors
        reduction.accumulate( self.errors().storage().handle(),
                              sourceErrorVector.handle(),
                              sourceErrorVector.datatype(),
                              eslice.handle())
        return
    
    def energy( self):
        """energy axis for this monitor/measurement"""
        return self._axisCont.datasetFromId( 2)


    def energyUnit( self):
        """unit for energy"""
        return self._energyUnit


    def q( self):
        """q axis for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def qUnit( self):
        """unit for q"""
        return self._qUnit


    def __init__( self, intensity, intensityError, intensityUnit,
                  q, qUnit, energy, energyUnit, name="SQEData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[ q, energy])

        self._intensityUnit = intensityUnit
        self._energyUnit = energyUnit
        self._qUnit = qUnit

        return


# version
__id__ = "$Id$"

# End of file
