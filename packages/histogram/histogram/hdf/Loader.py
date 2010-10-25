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


# render a graph consisting nodes in the "nodes" subpackage out of
# the graph of a hdf5 file.

#import nodes
from ndarray.NumpyNdArray import NdArray
from histogram.NdArrayDataset import Dataset
import numpy as np
#from histogram.Axis import Axis
from histogram import axis
from ndarray.NumpyNdArray import getNumpyArray_aktypecode

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
            boundaries =  NdArray( getNumpyArray_aktypecode(binBoundaries), binBoundaries)
            centers = NdArray( getNumpyArray_aktypecode(binCenters), binCenters)
            axesHash[axes[axisName].attrs['index']] = axis(
                axisName, unit = unit,
                boundaries = boundaries, centers = centers,
                )
            
        #reorder the axes
        axisList=[]
        for i in range(len(axesHash)):
            axisList.append(axesHash[i])

        if kwds:
            return self.onHistogramSlice(axisList, **kwds)

        # take care of datasets
        data = self.onDataset(histogramGrp, 'data')
        errors = self.onDataset(histogramGrp, 'errors')
        from histogram import histogram
        h = histogram(self.histogramName, axisList, 
                      data = data, errors = errors,
                      unit = data.unit())
        return h


    def onHistogramSlice(self, axisList, **kwds):
        return


    def onDataset(self, histogramGrp, type):
        try:
            dataGroup = histogramGrp[type]
            if 'storage' in list(dataGroup): # this uses the 'storage' convention
                rawdata = dataGroup['storage']
            else:
                #case when dataGroup *is* the dataset
                rawdata = dataGroup
            unit = self.onUnit(dataGroup.attrs['unit'])
            #get length and size
            lengths = rawdata.shape
            size=1
            for length in lengths:
                size*=length
                
        except:
            rawdata = None

        #get rest of attributes--TODO
        attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
        dataStore = NdArray(getNumpyArray_aktypecode(rawdata), size, 1.0)
        dataStore.setShape(lengths)
        data = Dataset('data', unit, attributes, lengths, dataStore)
        return data
#        name = dataset.name()
#        shape = dataset.dimensions()
#        path = dataset.path()
#        datasource = nodes.h5DataSource(
#            shape, path, self._selector, self._reader )
#        ret = nodes.ndArray(name, shape, datasource )
#        return ret
#
#    def onAxis(self, axis):
#        for e in axis.children():
#            name = e.name()
#            v = e.identify(self)
#            exec '%s=v' % name.replace(' ', '_')
#        name = axis.name()
#        unit = axis.getAttribute( 'unit' )
#        type = axis.getAttribute( 'type' )
#        attrs = axis.attributes()
#        ret = nodes.axis( name, unit, type, bin_centers, bin_boundaries, attrs)
#        return ret
    
    
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
