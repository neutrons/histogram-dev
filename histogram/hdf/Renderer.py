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

import nx5.nexml.elements as nx5elements

class Renderer(object):


    def render(self, histogram):
        return self.onHistogram(histogram)


    def onHistogram(self, histogram):
        name = histogram.name()
        node = nx5elements.group( name, 'Histogram', None, None)

        axesNode = nx5elements.group( 'grid', 'Grid', None, None)
        node.addChild( axesNode )
        for i, axis in enumerate(histogram.axes()):
            axisNode = self.onAxis( axis, i )
            axesNode.addChild( axisNode )
            continue
        
        data = histogram.data()
        errs = histogram.errors()
        
        datanode = self.onDataset(data)
        errsnode = self.onDataset(errs)

        node.addChild( datanode )
        node.addChild( errsnode )
        return node


    def onDataset(self, dataset):
        node = nx5elements.group(
            dataset.name(), 'ValueNdArray', None, None)
        
        unit = dataset.unit()
        node.setAttributes(
            {'unit': unit,
             }
            )
        
        arrnode = self.onVector(
            dataset.storage().as('StdVectorNdArray'),
            'storage', 'NdArray', dataset.shape() )

        node.addChild( arrnode )

        return node


    def onAxis(self, axis, index):
        #index: index of this axis in the axis array
        #we need to index that so that axis can be loaded
        #sequentially.
        
        mapper = axis._mapper
        type = types[mapper.__class__]

        name = axis.name()
        unit = axis.unit()
        
        node = nx5elements.group(name, 'Axis', None, None)
        node.setAttributes( { 'type': type, 'unit': unit, 'index': index } )

        bbs = axis.binBoundaries()
        bbsnode = self.onVector(
            bbs.as('StdVectorNdArray'),
            'bin boundaries', 'NdArray', [ bbs.size() ] )

        node.addChild( bbsnode )

        bcs = axis.binCenters()
        from ndarray.StdVectorNdArray import NdArray as StdVectorNdArray
        bcsnode = self.onVector(
            StdVectorNdArray(bbs.datatype(), bcs),
            'bin centers', 'NdArray', [ len(bcs) ] )
        node.addChild( bcsnode )
        return node
    
            
    def onVector(self, vector, name, klass, dimensions):
        dataset = nx5elements.dataset(
            name, klass, None, None, dimensions, vector.datatype(),
            vector)
        return dataset
        

    pass # end of Renderer


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
    h = histogram('h',
                  [('y', arange(0,100, 1.) ),
                   ('x', arange(100, 180, 1.) ),]
                  )

    g = Renderer().render(h)
    
    from nx5.renderers import *
    setPath(g, h.name())
    printGraph( g )

    writeGraph( g, 't.h5', 'c' )
    return


if __name__ == '__main__': test()



# version
__id__ = "$Id$"

# End of file 
