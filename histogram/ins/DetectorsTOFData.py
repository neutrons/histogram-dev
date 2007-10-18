#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from histogram.Histogram import Histogram

class DetectorsTOFData( Histogram):

    def tof( self):
        """tof() -> time-of-flight axis"""
        return self.axisFromId(2)


    def detectors( self):
        """detectors() -> detector axis"""
        return self.axisFromId(1)


    def __init__( self, detectorAxis, tofAxis, data, errors, name=""):
        Histogram.__init__( self, name, data, errors, axes=[detectorAxis, tofAxis])

        return 
        
        

# version
__id__ = "$Id$"

# End of file
