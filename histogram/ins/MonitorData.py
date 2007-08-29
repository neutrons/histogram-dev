#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from histogram.Histogram import Histogram

class MonitorData( Histogram):
    """store/serve monitor intensity and tof info"""


    def cartesianPosition( self):
        """position of this monitor in cartesian coordinates"""
        return self._cartesianPosition
    

    def position( self):
        """position of this monitor"""
        return self._position


    def tof( self):
        """tof for this monitor/measurement"""
        return self._axisCont.datasetFromId( 1)


    def tofUnit( self):
        """unit for tof"""
        return self._tofUnit


    def __init__( self, intensity, intensityError, intensityUnit, tof, tofUnit,
                  position, cartesianPosition, monitor, name="monitorData"):
        
        Histogram.__init__( self, name=name, data=intensity,
                            errors=intensityError,
                            axes=[tof])

        self._intensityUnit = intensityUnit
        self._tofUnit = tofUnit
        self._position = position
        self._cartesianPosition = cartesianPosition
        self._monitor = monitor
        
        return
    

# version
__id__ = "$Id$"

# End of file
