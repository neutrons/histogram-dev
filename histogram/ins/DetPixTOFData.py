#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from TOFPixelData import TOFPixelData
import stdVector
from stdVector.Slice import Slice
from ndarray.StdVectorNdArray import arrayFromVector
from histogram.NdArrayDataset import Dataset

from histogram.Histogram import Histogram


class DetPixTOFData( Histogram):

    def __init__( self, detectorAxis, pixelAxis, tofAxis, data, errors,
                  detectorMap, name="I(det,pix,tof)"):
        Histogram.__init__( self, name, data, errors,
                            axes=[detectorAxis, pixelAxis, tofAxis])

        self._detectorMap = detectorMap
        self._mainDataStore = self.data().storage()
        self._mainErrorStore = self.errors().storage()
        self._tofAxis = self.axisFromId( 3)
        return 
        

    def extractPixelData( self, pixel, detectorID, 
                          pixelVector=None, errorVector=None, reversed=False):
        #This implementation directly calls stdVector to achieve
        #faster speed. Should use Histogram's sliciing method.

        pixelID = pixel.pixelID()

        mainDataStore = self._mainDataStore
        mainErrorStore = self._mainErrorStore
        
        numDets, numPix, numTOF = self._shape

        # convert detectorID to detector index
        detectorIndex = self._detectorMap[ detectorID]

        #start = 1000000
        if not reversed:
            start = (detectorIndex*numPix + pixelID)*numTOF
        else:
            start = ( pixelID*numDets + detectorIndex)*numTOF
            pass
        #size = numTOF
        #stride = 1
        pixSlice = Slice( start, numTOF, 1) 

        pixelVector = stdVector.extractSlice( pixSlice, mainDataStore, pixelVector)
        #intensityDS = Dataset( "pixel %s data"%pixelID, "Counts", shape=[numTOF],
        intensityDS = Dataset(
            "pixel data", "Counts",
            shape=[numTOF], storage=pixelVector)
        
        errorVector = stdVector.extractSlice( pixSlice, mainErrorStore,
                                              errorVector)
        #errorDS = Dataset( "pixel %s errors"%pixelID, "Counts",
        errorDS = Dataset(
            "pixel errors", "Counts",
            shape=[numTOF], storage=errorVector)
        
        pixelData = TOFPixelData(
            intensityDS, errorDS, "Counts", self._tofAxis,
            "microseconds", pixel)
        #"microseconds", position, pixel)
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


        

# version
__id__ = "$Id$"

# End of file
