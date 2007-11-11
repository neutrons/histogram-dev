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


# render a graph consisting nodes in the "nodes" subpackage out of
# the graph of a hdf5 file.


import nodes


class Parser:
    
    
    def __init__( self, filename):
        import nx5.file
        self._nxf = nx5.file.file( filename, 'r')

        from nx5.file.VectorReader import Reader
        self._reader = Reader()

        self._selector = self._nxf.selector()
        return


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
            continue

        name = axis.name()
        unit = axis.getAttribute( 'unit' )
        type = axis.getAttribute( 'type' )

        ret = nodes.axis( name, unit, type, bin_centers, bin_boundaries )
        
        return ret


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


    def onHistogram(self, histogram):
        errors = None
        
        for e in histogram.children():
            name = e.name()
            exec '%s = e.identify(self)' % name
            continue

        axes = grid
        #print axes, name, data, errors

        name = histogram.name() 

        return nodes.histogram( name, axes, data = data, errors = errors )

    onNXroot = onHistogram # hack

    pass # end of Parser


def test():
    from nx5.renderers import *
    g = graphFromHDF5File( 't.h5', '/h' )
    printGraph( g )

    h = Parser().parse( g )

    print h
    return


if __name__ == '__main__': test()

            
    


# version
__id__ = "$Id$"

# End of file 
