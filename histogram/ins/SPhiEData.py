#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from stdVector.Slice import Slice
import stdVector
from histogram.NdArrayDataset import Dataset

from histogram.Histogram import Histogram

class SPhiEData( Histogram):

    """Data as a function of scattering angle and energy"""

    def extractEnergySlice( self, energy, dataVector=None, errorVector=None):
        """extractEnergySlice( energy, dataVector=None, errorVector=None) ->
        EnergyPhiData
        extract a constant energy slice"""
        
        # map energy to index
        energyList = self.energy().storage().asList()
        from math import floor
        de = energyList[1] - energyList[0]
        eIndex = int( floor( (energy - energyList[0])/de) )

        numEnergies = len(energyList) - 1
        numPhi = len( self.phi().storage().asList()) - 1

        start = eIndex
        size = numPhi
        stride = numEnergies
        
        eslice = Slice( start, size, stride)

        dataVector = stdVector.extractSlice( eslice, self.data().storage(),
                                             dataVector)
        intensityDS = Dataset( "energy %s data"%energy, "Counts", shape=[size],
                               storage=dataVector)
        
        errorVector = stdVector.extractSlice( eslice, self.errors().storage(),
                                              errorVector)
        errorDS = Dataset( "energy %s errors"%energy, "Counts",
                           shape=[size], storage=errorVector)

        from EnergyPhiData import EnergyPhiData
        ephiData = EnergyPhiData( intensityDS, errorDS, "counts",
                                  self.phi(), "degrees", energy)
        
        return ephiData
    
    
    def energy( self):
        """energy transfer axis for this monitor/measurement"""
        return self._axisCont.datasetFromId( 2)


    def energyUnit( self):
        """unit for energy"""
        return self._energyUnit


    def phi( self):
        """phi axis for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def phiUnit( self):
        """unit for phi"""
        return self._phiUnit


    def __init__( self, intensity, intensityError, intensityUnit,
                  phi, phiUnit, energy, energyUnit, name="SPhiEData"):
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[ phi, energy])

        self._intensityUnit = intensityUnit
        self._energyUnit = energyUnit
        self._phiUnit = phiUnit

        return




# version
__id__ = "$Id$"

# End of file
