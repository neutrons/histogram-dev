#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                          Jiao Lin,  J Brandon Keith
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import numpy as np
from ndarray.NumpyNdArray import NdArray, getNumpyArray_aktypecode as getDataType, arrayFromNumpyArray
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
            axisnode = axes[axisName]
            axis = self.onAxis(axisnode)
            axesHash[axisnode.attrs['index']] = axis
            continue
            
        # reorder the axes
        axisList=[]
        for i in range(len(axesHash)):
            axisList.append(axesHash[i])

        # if slicing is requested
        if kwds:
            # do slice
            h = self.onHistogramSlice(histogramGrp, axisList, **kwds)

        else:
            # datasets
            data = self.onDataset(histogramGrp, 'data')
            errors = self.onDataset(histogramGrp, 'errors')

            # create histogram
            from histogram import histogram
            h = histogram(self.histogramName, axisList, 
                          data = data, errors = errors,
                          unit = data.unit())
            
        # meta data
        metadata = self._getAttrs(histogramGrp)
        for k, v in metadata.iteritems():
            h.setAttribute(k,v)
            continue
        
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


    def onAxis(self, axisnode):
        binBoundaries = axisnode['bin boundaries']
        binCenters = axisnode['bin centers']
        unit = self.onUnit(axisnode.attrs['unit'])
        type = self._str(axisnode.attrs['type'])
        name = self._str(axisnode.attrs['name'])
        attrs = self._getAttrs(axisnode)
        
        from histogram import paxis, IDaxis
        if type == 'continuous':
            boundaries =  NdArray( getDataType(binBoundaries), binBoundaries)
            rt = paxis(name, unit, boundaries = boundaries, attributes=attrs)
        elif type == 'discrete':
            centers = NdArray( getDataType(binCenters), binCenters)
            rt = IDaxis( name, centers, attributes=attrs )
        else:
            raise NotImplementedError

        # meta data
        metadata = self._getAttrs(axisnode)
        for k, v in metadata.iteritems():
            rt.setAttribute(k,v)
            continue
        return rt

        
    def onDataset(self, histogramGrp, name, slice=None):
        dataGroup = histogramGrp[name]
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
        attributes = {
            'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
        datatype = getDataType(rawdata)
        
        # rawdata = np.array(rawdata, copy=1)
        dataStore = arrayFromNumpyArray(rawdata, datatype)

        dataStore.setShape(lengths)
        data = Dataset(name, unit, attributes, lengths, dataStore)
        return data
    
    
    def onUnit(self, unit):
        if isinstance(unit, int) or isinstance(unit, float) or isinstance(unit, long):
            return unit
        # ndarray of chars
        from numpy import ndarray
        if isinstance(unit, ndarray):
            return unit.tostring()
        if isinstance(unit, str):
            return unit
        raise NotImplementedError, 'type: %s, str: %s' % (
            unit.__class__,str(unit))

    
    def _getAttrs(self, node, skip = None):
        if skip is None:
            from _reserved_attrs import keys as skip
        d = {}
        for key in node.attrs.iterkeys():
            if key in skip: continue
            d[key] = node.attrs[key]
            continue
        return d


    def _str(self, candidate):
        if isinstance(candidate, basestring):
            return candidate
        if isinstance(candidate, np.ndarray):
            return candidate.tostring()
        raise NotImplementedError, str(candidate)


    def _guessHistogramName(self):
        fs = self.fs
        names = list(fs)
        if len(names)>1:
            raise RuntimeError, "This file contains more than one histogram"
        return names[0]


# version
__id__ = "$Id$"

# End of file 
