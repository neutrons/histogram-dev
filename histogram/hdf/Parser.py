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


# create a histogram object out of a nexml graph


class Parser:
    
    
    def parse( self, graph ):
        return graph.identify(self)
    
    
    def onGroup(self, group):
        
        klass = group.className()

        try:
            handler = getattr( self, 'on%s' % klass )
        except AttributeError :
            raise NotImplementedError, "handler for %s" % klass
        
        return handler( group )


    def onDataset(self, dataset):
        shape = dataset.dimensions()
        from ndarray.StdVectorNdArray import arrayFromVector
        ret = arrayFromVector(dataset.storage())
        ret.setShape( shape )
        return ret


    def onNdArray(self, ndarray):
        return ndarray.storage()


    def onAxis(self, axis):
        for e in axis.children():
            name = e.name()
            v = e.identify(self).asNumarray()
            exec '%s=v' % name.replace(' ', '_')
            continue

        name = axis.name()
        unit = axis.getAttribute( 'unit' )
        type = axis.getAttribute( 'type' )

        ret = _axis( name, unit, type, bin_centers, bin_boundaries )
        
        return ret


    def onGrid(self, grid):
        #for now, grid is a directory of axes

        #number of axes
        n = len( grid.children() )

        #container of results
        ret = [None for i in range(n)]
        
        for axisNode in grid.children():
            index = axisNode.getAttribute( 'index' )
            axis = axisNode.identify(self)
            ret[index] = axis
            continue

        for axis in ret: assert axis is not None

        return ret            


    def onValueNdArray(self, valueArray):
        storage = valueArray.getChild('storage').identify(self)
        from histogram.NdArrayDataset import Dataset as NdArrayDataset
        name = valueArray.name()
        unit = valueArray.getAttribute( 'unit' )
        return NdArrayDataset( name, unit, storage = storage )


    def onHistogram(self, histogram):
        errors = None
        
        for e in histogram.children():
            name = e.name()
            exec '%s = e.identify(self)' % name
            continue

        axes = grid
        #print axes, name, data, errors

        name = histogram.name() 

        from histogram import histogram
        return histogram( name, axes, data = data, errors = errors )

    onNXroot = onHistogram # hack

    pass # end of Parser


def _axis( name, unit, type, bin_centers, bin_boundaries ):
    from histogram import *
    if type == 'continuous':
        return paxis( name, unit, boundaries = bin_boundaries )
    else:
        return IDaxis( name, bin_centers )
    raise "Should not reach here"


def test():
    from nx5.renderers import *
    g = graphFromHDF5File( 't.h5', '/h' )
    printGraph( g )
    dataExtractor( 't.h5' ).render( g )

    h = Parser().parse( g )

    print h
    return


if __name__ == '__main__': test()

            
    


# version
__id__ = "$Id$"

# End of file 
