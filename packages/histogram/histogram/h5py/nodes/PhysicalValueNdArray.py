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
class PhysicalValueNdArray(AbstractNode):


    def __init__( self, name, unit, valuearray):
        AbstractNode.__init__(self, name)
        self.unit = unit
        self.valuearray = valuearray
        return


    def fetch(self, slices = None):
        name = self.name
        unit = self.unit
        storage = self.valuearray.fetch( slices )
        from histogram.NdArrayDataset import Dataset as NdArrayDataset
        return NdArrayDataset( name, unit, storage = storage )


    pass # end of PhysicalValueNdArray


# version
__id__ = "$Id$"

# End of file 
