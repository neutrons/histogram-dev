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


from AbstractNode import AbstractNode
class Histogram(AbstractNode):


    def __init__( self, name, axes, data, errors):
        AbstractNode.__init__(self, name)
        self.axes = axes
        self.data = data
        self.errors = errors
        return


    def fetch(self, **kwds):
        '''fetch( **kwds ) --> histogram.Histogram.Histogram instance
  For example, for I(detID, pixID, tof)
    fetch( detID=(2,10), pixID= (3,7) )
'''
    
        axes = [ axis.fetch() for axis in self.axes ]
        from histogram.Histogram import _slicingInfosFromDictionary
        slicingInfos = _slicingInfosFromDictionary( kwds, axes )
        indexSlices = [
            slice( *axis.slicingInfo2IndexSlice( si ) )
            for axis, si in zip( axes, slicingInfos ) ]

        data = self.data.fetch( indexSlices )
        if self.errors is not None:
            errors = self.errors.fetch( indexSlices )
            pass

        newaxes = [axis[si] for axis, si in zip(axes, slicingInfos) ]

        name = self.name
        from histogram import histogram
        return histogram(
            name, newaxes, data = data, errors = errors, unit = data.unit() )

    pass # end of Histogram


# version
__id__ = "$Id$"

# End of file 
