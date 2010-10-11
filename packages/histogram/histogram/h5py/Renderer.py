#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


#render a histogram to a nx5 graph


#import journal
#jrnltag = 'histogram.hdf.Renderer'
#debug = journal.debug( jrnltag )

#import nx5.nexml.elements as nx5elements


class Renderer(object):


    def __init__(self, compressionType='lzf', compressionLevel=4):
        self.compressionType = compressionType


    def render(self, fs, histogram):
        self.onHistogram(fs, histogram)


    def onHistogram(self, fs, histogram):
        name = histogram.name()
        histogramGrp = fs.create_group( name)
        #node = nx5elements.group( name, 'Histogram', None, None)

        axesGrp = histogramGrp.create_group('grid')
        #axesNode = nx5elements.group( 'grid', 'Grid', None, None)
        #node.addChild( axesNode )
        for i, axis in enumerate(histogram.axes()):
            self.onAxis( axesGrp, axis, i )
            #axesNode.addChild( axisNode )
            #continue
        
        data = histogram.data()
        errs = histogram.errors()
        
        self.onDataset(histogramGrp, data)
        self.onDataset(histogramGrp, errs)
#        datanode = self.onDataset(histogramGrp, data)
#        errsnode = self.onDataset(histogramGrp, errs)

#        node.addChild( datanode )
#        node.addChild( errsnode )
#        return node
        fs.close()


    def onDataset(self, histogramGrp, dataset):
        
#        node = nx5elements.group(
#            dataset.name(), 'ValueNdArray', None, None)
        data = dataset.storage().as_('NumpyNdArray').asNumarray()
        histogramDset = histogramGrp.create_dataset(dataset.name(), data = data, 
                                                    compression=self.compressionType,)
        unit = dataset.unit()
#        node.setAttributes(
#            {'unit': unit,
#             }
#            )
        histogramDset.attrs['unit'] = unit
        
#        arrnode = self.onVector(
#            dataset.storage().as_('StdVectorNdArray'),
#            'storage', 'NdArray', dataset.shape() )
#        if self._compression_level:
#            arrnode.setCompression(self._compression_level)
#        node.addChild( arrnode )
#
#        return node

    def onAxis(self, axesGrp, axis, index):
        #index: index of this axis in the axis array
        #we need to index that so that axis can be loaded
        #sequentially.
        
        mapper = axis._mapper
        type = types[mapper.__class__]

        name = axis.name()
        unit = axis.unit()
        
        #node = nx5elements.group(name, 'Axis', None, None)
        axisGrp = axesGrp.create_group(name)

        # attributes of axis
        attrs = {}
        attrnames = axis.listAttributes()
        for name in attrnames:
            axisGrp.attrs[name] = str(axis.attribute(name))
            attrs[name] = str(axis.attribute(name))

        #
#        attrs.update(
#            { 'type': type, 'unit': unit, 'index': index }
#            )
#        node.setAttributes( attrs )
        axisGrp.attrs['type'] = type
        axisGrp.attrs['unit'] = unit.value
        axisGrp.attrs['index'] = index

        bbs = axis.binBoundaries()
#        bbsnode = self.onVector(
#            bbs.as_('StdVectorNdArray'),
#            'bin boundaries', 'NdArray', [ bbs.size() ] )
#
#        node.addChild( bbsnode )
        axisGrp.create_dataset('bin boundaries', 
                               data = bbs.as_('NumpyNdArray'))

        bcs = axis.binCenters()
#        from ndarray.StdVectorNdArray import NdArray as StdVectorNdArray
#        bcsnode = self.onVector(
#            StdVectorNdArray(bbs.datatype(), bcs),
#            'bin centers', 'NdArray', [ len(bcs) ] )
#        debug.log( 'bcs=%s' % (bcs,) )
#        node.addChild( bcsnode )
        from ndarray.NumpyNdArray import NdArray
        axisGrp.create_dataset('bin centers', data = NdArray(bbs.datatype(), bcs))
#        return node
    
            
#    def onVector(self, vector, name, klass, dimensions):
#        
#        def __init__(self, name, className, nxpath, pathstr, dimensions, datatype,
#                 storage = None):
#        """Dataset( name, className, nxpath, pathstr, dimensions, datatype,
#                 storage = None) -> new nexml Dataset
#        Create node to represent dataset.
#        Inputs:
#            name: name of dataset (string)
#            className: class (string, probably best left empty)
#            nxPath: NXPath instance (set to None unless using nexml searcher)
#            pathstr: string representing this node's path, use '/' as
#                     path separator
#            dimensions: list of dimension sizes
#            datatype: nx5 datatype. Popular types include:
#                4.......char
#                5.......float
#                6.......double
#                24......unsigned int
#                25......int
#            storage: StdVector-like object that contains the actual data for
#                     the dataset (default None)
#        Output:
#            new Dataset object to represent a dataset in an nx5 file."""
#        NexusElement.__init__(self, name, className, nxpath, pathstr)
#        self._dimensions = dimensions
#        self._datatype = datatype
#        self._storage = storage
        
#        dataset = nx5elements.dataset(
#            name, klass, None, None, dimensions, vector.datatype(),
#            vector)
#        return dataset



from histogram.DiscreteAxisMapper import DiscreteAxisMapper
from histogram.ContinuousAxisMapper import ContinuousAxisMapper
from histogram.EvenlyContinuousAxisMapper import EvenlyContinuousAxisMapper
types = {
    DiscreteAxisMapper: 'discrete',
    ContinuousAxisMapper: 'continuous',
    EvenlyContinuousAxisMapper: 'continuous',
    }



def test():
    from histogram import histogram, arange
    from numpy.random import rand
    h = histogram('h',
                  [('x', arange(0, 100, 1.) ),
                   ('y', arange(100, 180, 1.) ),],
                   data=rand(100,80)
                  )
    from h5py import File
    filename = 'test1.h5'
    fs = File( filename, 'w' )
    Renderer().render(fs, h)
    
#    from nx5.renderers import setPath, printGraph, writeGraph
#    setPath(g, h.name())
#    printGraph( g )
#
#    writeGraph( g, 't.h5', 'c' )
#    return


if __name__ == '__main__': test()



# version
__id__ = "$Id$"

# End of file 
