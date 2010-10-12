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


import nodes
from ndarray.NumpyNdArray import NdArray

class Parser:
    
    # maybe add compression keywords here...and any other "fetch" keywords
    def __init__( self, fs = None):
        return

    def parse( self, fs ):
    #def parse( self, graph ):
        #return graph.identify(self)
        return self.onHistogram(fs)
    
    def onHistogram(self, fs):
        # first get histogram
        histogramNames = list(fs)
        if len(histogramNames)>1:
            raise Exception, "This file contains more than one histogram"
        histogramName = histogramNames[0]
        histogramGrp = fs[histogramName]
        
        #members = dict(histogramGrp)
        # first get the axes
        try:
            #axes = members.pop('grid')
            axes = histogramGrp['grid']
        except:
            raise ValueError, "This histogram does not contain a 'grid' node"
        from histogram.Axis import Axis
        axisList = []
        for axisName in axes:
            axisList.append(Axis(axisName, unit = axes[axisName].attrs['unit'],
                                 storage = NdArray( 'double', axes[axisName]['bin boundaries'][:]),
                                 centers = NdArray( 'double', axes[axisName]['bin centers'][:]),))
        
        # assume everything else is a dataset group
        try:
            rawdata = histogramGrp['data']
        except:
            rawdata = None
        #get length and size
        lengths = rawdata.shape
        size=1
        for length in lengths:
            size*=length
        #remove unit
        attrs = rawdata.attrs
        unit = attrs.pop('unit')
        #get rest of attributes--TODO
        attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
        dataStore = NdArray(rawdata.dtype, size, 1.0)
        dataStore.setShape(lengths)
        from histogram.NdArrayDataset import Dataset
        data = Dataset('data', unit, attributes, lengths, dataStore)
            
        try: 
            errors = histogramGrp['errors']
        except:
            errors=None

        from histogram import histogram, arange
        h = histogram(histogramName, axisList, data = data, errors = errors)
        
#        errors = None
#        for e in histogram.children():
#            name = e.name()
#            # !!!!!!!!!!!!!!!!!!!!!!!!!
#            # this is a hack
#            if name.startswith('sum of '):
#                name = name.split()[2]
#            # !!!!!!!!!!!!!!!!!!!!!!!!!
#            exec '%s = e.identify(self)' % name
#        try:
#            axes = grid
#        except:
#            raise ValueError, "This graph does not contain 'grid' node: %s" %(
#                histogram.name() )
#        try:
#            data
#        except:
#            raise ValueError, "This graph does not contain 'data' node: %s" %(
#                histogram.name() )
#        name = histogram.name()
#        return nodes.histogram( name, axes, data = data, errors = errors )
        return h

    def onDataset(self, dataset):
        name = dataset.name()
        shape = dataset.dimensions()
        path = dataset.path()
        datasource = nodes.h5DataSource(
            shape, path, self._selector, self._reader )
        ret = nodes.ndArray(name, shape, datasource )
        return ret

    def onAxis(self, axis):
        for e in axis.children():
            name = e.name()
            v = e.identify(self)
            exec '%s=v' % name.replace(' ', '_')
        name = axis.name()
        unit = axis.getAttribute( 'unit' )
        type = axis.getAttribute( 'type' )
        attrs = axis.attributes()
        ret = nodes.axis( name, unit, type, bin_centers, bin_boundaries, attrs)
        return ret
    
    onNXroot = onHistogram # hack
    
    def onGroup(self, group):
        
        klass = group.className()

        try:
            handler = getattr( self, 'on%s' % klass )
        except AttributeError :
            raise NotImplementedError, "handler for %s" % klass
        
        return handler( group )

    def onGrid(self, grid):
        #for now, grid is a directory of axes

        #number of axes
        n = len( grid.children() )

        #container of results
        ret = [None for i in range(n)]
        
        for axisNode in grid.children():
            #index keep axis in the right order
            index = axisNode.getAttribute( 'index' )
            axis = axisNode.identify(self)
            ret[index] = axis
            continue

        for axis in ret: assert axis is not None

        return ret 

    def onValueNdArray(self, valueArray):
        valuearray = valueArray.getChild('storage').identify(self)
        name = valueArray.name()
        unit = valueArray.getAttribute( 'unit' )
        return nodes.physicalValueNdArray( name, unit, valuearray )

def test():
#    from nxk5.renderers import graphFromHDF5File, printGraph
#    g = graphFromHDF5File( 'test1.h5', '/h' )
#    printGraph( g )
    from h5py import File
    filename = 'test1.h5'
    fs = File( filename, 'r' )
    h = Parser().parse( fs )

    print h


if __name__ == '__main__': test()

            
    


# version
__id__ = "$Id$"

# End of file 
