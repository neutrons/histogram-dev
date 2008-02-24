#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from histogram.Histogram import Histogram

class VanadiumData( Histogram):


    def detectorAxis( self):
        """detectors for this measurement"""
        return self._axisCont.datasetFromId( 1)


    def detectorsUnit( self):
        """unit for detectors"""
        return self._detectorsUnit


    def tofAxis( self):
        """tof for this measurement"""
        return self._axisCont.datasetFromId( 2)


    def tofUnit( self):
        """unit for tof"""
        return self._tofUnit


    def __init__( self, intensity, intensityError, intensityUnit, tof, tofUnit,
                  detectorIDs, detectorIDsunit, name="vanadiumData"):
        
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[detectorIDs, tof])

        self._intensityUnit = intensityUnit
        self._tofUnit = tofUnit
        self._detectorsUnit = detectorIDsunit
        
        return
    



# version
__id__ = "$Id$"

# End of file
