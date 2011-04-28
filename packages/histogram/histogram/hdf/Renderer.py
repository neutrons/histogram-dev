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

    def render(self, histogram):
        return self.onHistogram(histogram)


    def onHistogram(self, histogram):
        fs = self.fs
        name = histogram.name()
        histogramGrp = fs.create_group( name)

        axesGrp = histogramGrp.create_group('grid')
        for i, axis in enumerate(histogram.axes()):
            self.onAxis(axesGrp, axis, i)
        
        data = histogram.data()
        errs = histogram.errors()
        
        self.onDataset(histogramGrp, data)
        self.onDataset(histogramGrp, errs)

        self._setAttrs(histogramGrp, histogram)


    def onDataset(self, histogramGrp, dataset, skip_attrs=None):
        data = dataset.storage().as_('NumpyNdArray').asNumarray()
        histogramDset = histogramGrp.create_dataset(
            dataset.name(), data = data, 
            compression=self.compressionType,)
        unit = dataset.unit()
        histogramDset.attrs['unit'] = str(unit)
        return


    def onAxis(self, axesGrp, axis, index):
        #index: index of this axis in the axis array
        #we need to index that so that axis can be loaded
        #sequentially.

        mapper = axis._mapper
        type = types[mapper.__class__]

        #
        name = axis.name()
        try:
            axisGrp = axesGrp.create_group(name)
        except Exception, e:
            raise RuntimeError, "Failed to create group %r in group %s. Original exception:\n%s: %s" % (name, axesGrp, e.__class__.__name__, e)
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
        axisGrp.attrs['unit'] = str(unit)
        axisGrp.attrs['index'] = index

        bbs = axis.binBoundaries()
        axisGrp.create_dataset('bin boundaries', 
                               data = bbs.as_('NumpyNdArray'))

        bcs = axis.binCenters()
        from ndarray.NumpyNdArray import NdArray
        axisGrp.create_dataset('bin centers',
                               data = bcs)
        # data = NdArray(bcs.datatype(), bcs))


    def _setAttrs(self, node, attributecontainer, skip_attrs=None):
        if skip_attrs is None:
            from _reserved_attrs import keys as skip_attrs
        for key in attributecontainer.listAttributes():
            if key in skip_attrs: continue
            value = attributecontainer.getAttribute(key)
            node.attrs[key] = value
          

from histogram.DiscreteAxisMapper import DiscreteAxisMapper
from histogram.ContinuousAxisMapper import ContinuousAxisMapper
from histogram.EvenlyContinuousAxisMapper import EvenlyContinuousAxisMapper
types = {
    DiscreteAxisMapper: 'discrete',
    ContinuousAxisMapper: 'continuous',
    EvenlyContinuousAxisMapper: 'continuous',
    }



if __name__ == '__main__': test()



# version
__id__ = "$Id$"

# End of file 
