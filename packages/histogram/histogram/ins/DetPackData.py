#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from TOFPixelData import TOFPixelData
from stdVector.Slice import Slice
from histogram.StdvectorDataset import Dataset
import stdVector

import journal
debug = journal.debug("histogram.DetPackData")

from histogram.Histogram import Histogram


class DetPackData( Histogram):

    def extractPixelData( self, pixel, detectorIndex, position,
                          pixelVector=None, errorVector=None):

        #this implementation directly calls stdVector to achieve faster speed
        #it is better to just use Histogram's slicing method
        pixelID = pixel.pixelID()

        mainDataStore = self.data().storage()
        mainErrorStore = self.errors().storage()

        dims = self._shape
        numDets = dims[0]; numPix = dims[1]; numTOF = dims[2]

        detectorOffset = detectorIndex % numDets
        debug.log("numDets = %s, detectorIndex=%s" % (numDets, detectorIndex))

        start = (detectorOffset*numPix + pixelID)*numTOF
        size = numTOF
        stride = 1
        debug.log("Will read %s starting at %s" % (size, start))
        pixSlice = Slice( start, size, stride)

        pixelVector = stdVector.extractSlice( pixSlice, mainDataStore,
                                              pixelVector)
        intensityDS = Dataset( "pixel %s data"%pixelID, "Counts", shape=[size],
                               storage=pixelVector)
        errorVector = stdVector.extractSlice( pixSlice, mainErrorStore,
                                              errorVector)
        errorDS = Dataset( "pixel %s errors"%pixelID, "Counts",
                           shape=[size], storage=errorVector)
        tofAxis = self.axisFromId( 3)
        
        pixelData = TOFPixelData( intensityDS, errorDS, "Counts", tofAxis,
                                  "microseconds", position, pixel)

        return pixelData


    def detectorAxis( self):
        """detectors() -> detector axis"""
        return self.axisFromId(1)


    def pixelAxis( self):
        """pixelAxis() -> pixel axis"""
        return self.axisFromId(2)

    
    def tofAxis( self):
        """tof() -> time-of-flight axis"""
        return self.axisFromId(3)


    def __init__( self, detectorAxis, pixelAxis, tofAxis, data, errors,
                  name=""):
        Histogram.__init__( self, name, data, errors,
                            axes=[detectorAxis, pixelAxis, tofAxis])

        return 
        
        

# version
__id__ = "$Id$"

# End of file
