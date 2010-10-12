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
class Axis(AbstractNode):


    def __init__( self, name, unit, type, bin_centers, bin_boundaries, attributes=None):
        AbstractNode.__init__(self, name)
        self.unit = unit
        self.type = type
        self.bin_centers = bin_centers
        self.bin_boundaries = bin_boundaries
        self.attributes = attributes or {}
        return


    def fetch(self):
        bin_centers = self.bin_centers.fetch().asNumarray()
        bin_boundaries = self.bin_boundaries.fetch().asNumarray()
        attributes = self.attributes
        return _axis( self.name, self.unit, self.type,
                      bin_centers, bin_boundaries,  attributes)


def _axis( name, unit, type, bin_centers, bin_boundaries, attrs ):
    from histogram import paxis, IDaxis
    if type == 'continuous':
        return paxis( name, unit, boundaries = bin_boundaries, attributes=attrs )
    else:
        return IDaxis( name, bin_centers, attributes=attrs )
    raise "Should not reach here"


# version
__id__ = "$Id$"

# End of file 
