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


import journal
jrnltag = 'histogram.hdf.Renderer'
debug = journal.debug( jrnltag )


class Renderer(object):


    def __init__(self, fs, compressionType='lzf', compressionLevel=4):
        self.fs = fs
        self.compressionType = compressionType
        return

    def render(self, histogram):
        return self.onHistogram(histogram)


    def onHistogram(self, histogram):
        fs = self.fs
        name = histogram.name()
        histogramGrp = fs.create_group( name)

        axesGrp = histogramGrp.create_group('grid')
        for i, axis in enumerate(histogram.axes()):
            self.onAxis(axesGrp, axis, i)
            continue
        
        data = histogram.data()
        errs = histogram.errors()
        
        self.onDataset(histogramGrp, data)
        self.onDataset(histogramGrp, errs)

        self._setAttrs(histogramGrp, histogram)
        return


    def onDataset(self, histogramGrp, dataset, skip_attrs=None):
        data = dataset.storage().as_('NumpyNdArray').asNumarray()
        histogramDset = histogramGrp.create_dataset(
            dataset.name(), data = data, 
            compression=self.compressionType,)
        unit = dataset.unit()
#        node.setAttributes(
#            {'unit': unit,
#             }
#            )
        # in the tests, 'unit' is either an object or a string,
        # so i try to handle both
        try:
            histogramDset.attrs['unit'] = unit.value
        except:
            histogramDset.attrs['unit'] = unit

        return


    def onAxis(self, axesGrp, axis, index):
        #index: index of this axis in the axis array
        #we need to index that so that axis can be loaded
        #sequentially.
        
        mapper = axis._mapper
        type = types[mapper.__class__]

        #
        name = axis.name()
        axisGrp = axesGrp.create_group(name)
        axisGrp.attrs['name'] = name
        
        #
        unit = axis.unit()
        axisGrp.attrs['type'] = type
        

        # attributes of axis
        attrnames = axis.listAttributes()
        for name in attrnames:
            from _reserved_attrs import keys as skip
            if name in skip: continue
            axisGrp.attrs[name] = axis.attribute(name)

        #
        # in the tests, 'unit' is either an object or a string,
        # so i try to handle both
        try:
            axisGrp.attrs['unit'] = unit.value
        except:
            axisGrp.attrs['unit'] = unit
        axisGrp.attrs['index'] = index

        bbs = axis.binBoundaries()
        axisGrp.create_dataset('bin boundaries', 
                               data = bbs.as_('NumpyNdArray'))

        bcs = axis.binCenters()
        from ndarray.NumpyNdArray import NdArray
        axisGrp.create_dataset('bin centers', data = NdArray(bbs.datatype(), bcs))
#        return node


    def _setAttrs(self, node, attributecontainer, skip_attrs=None):
        if skip_attrs is None:
            from _reserved_attrs import keys as skip_attrs
        for key in attributecontainer.listAttributes():
            if key in skip_attrs: continue
            value = attributecontainer.getAttribute(key)
            node.attrs[key] = value
            continue
        return    
    
            

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
