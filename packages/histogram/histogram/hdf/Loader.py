#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import numpy as np
from ndarray.NumpyNdArray import NdArray, getNumpyArray_aktypecode as getDataType, arrayFromNumpyArray
from histogram import axis
from histogram.NdArrayDataset import Dataset


class Loader:
    
    def __init__( self, fs, pathinfile='/'):
        self.fs = fs
        self.pathinfile = pathinfile
        self.histogramName = pathinfile.split('/')[-1] or self._guessHistogramName()
        return
    
    
    def load( self, **kwds):
        return self.onHistogram(**kwds)
    
    
    def onHistogram(self, **kwds):
        fs = self.fs
        pathinfile = self.pathinfile
        histogramGrp = fs[pathinfile]
        try:
            axes = histogramGrp['grid']
        except:
            raise ValueError, "This histogram does not contain a 'grid' node"
        axesHash = {}
        for axisName in axes:
            binBoundaries = axes[axisName]['bin boundaries']
            binCenters = axes[axisName]['bin centers']
            unit = self.onUnit(axes[axisName].attrs['unit'])
            boundaries =  NdArray( getDataType(binBoundaries), binBoundaries)
            centers = NdArray( getDataType(binCenters), binCenters)
            axesHash[axes[axisName].attrs['index']] = axis(
                axisName, unit = unit,
                boundaries = boundaries, centers = centers,
                )
            
        # reorder the axes
        axisList=[]
        for i in range(len(axesHash)):
            axisList.append(axesHash[i])

        # if slicing is requested
        if kwds:
            # do slice
            return self.onHistogramSlice(histogramGrp, axisList, **kwds)

        # datasets
        data = self.onDataset(histogramGrp, 'data')
        errors = self.onDataset(histogramGrp, 'errors')

        # create histogram
        from histogram import histogram
        h = histogram(self.histogramName, axisList, 
                      data = data, errors = errors,
                      unit = data.unit())
        return h


    def onHistogramSlice(self, h5group, axes, **kwds):
        from histogram.Histogram import _slicingInfosFromDictionary
        slicingInfos = _slicingInfosFromDictionary( kwds, axes)
        indexSlices = [
            slice( *axis.slicingInfo2IndexSlice( si ) )
            for axis, si in zip( axes, slicingInfos ) ]
        indexSlices = tuple(indexSlices)
        
        # slice the axes
        axes = [axis[si] for axis, si in zip(axes, slicingInfos) ]
        
        # datasets
        data = self.onDataset(h5group, 'data', slice=indexSlices)
        errors = self.onDataset(h5group, 'errors', slice=indexSlices)

        # create histogram
        from histogram import histogram
        h = histogram(self.histogramName, axes, 
                      data = data, errors = errors,
                      unit = data.unit())
        return h


    def onDataset(self, histogramGrp, type, slice=None):
        dataGroup = histogramGrp[type]
        if 'storage' in list(dataGroup): # this uses the 'storage' convention
            rawdata = dataGroup['storage']
        else:
            #case when dataGroup *is* the dataset
            rawdata = dataGroup
        if slice:
            rawdata = rawdata[slice]
        else:
            rawdata = rawdata[:]
        unit = self.onUnit(dataGroup.attrs['unit'])
        #get length and size
        lengths = rawdata.shape
        size=1
        for length in lengths:
            size*=length

        #get rest of attributes--TODO
        attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
        datatype = getDataType(rawdata)
        dataStore = arrayFromNumpyArray(rawdata, datatype)

        dataStore.setShape(lengths)
        data = Dataset('data', unit, attributes, lengths, dataStore)
        return data
    
    
    def onUnit(self, unit):
        if isinstance(unit, int) or isinstance(unit, float):
            return unit
        return unit.tostring()

    
    def _guessHistogramName(self):
        fs = self.fs
        names = list(fs)
        if len(names)>1:
            raise RuntimeError, "This file contains more than one histogram"
        return names[0]


# version
__id__ = "$Id$"

# End of file 
