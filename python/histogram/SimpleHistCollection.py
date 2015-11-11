#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """
a histogram collection with one single histogram

  - NAME: SimpleHistCollection
  - PURPOSE: represent a histogram collection with one single histogram
  - DESCRIPTION: this class implements DetHistCollection. Any instance of
  this class contains only one histogram.
  - RELATED: DetHistCollection
  - TODOs:
"""

from DetHistCollection import DetHistCollection as DHCBase


class SimpleHistCollection(DHCBase):

    """Hist collection is useful when detector system is complex.
    For example, some instrument has two sets of detectors, the
    longer one and the short one. One histogram is not good enough
    to represent data from such a complex detector system, and
    a collection of histogram is a more appropriate representation.

    For uniformity, all main detector data should be represented
    by a histogram collection.
    
    This SimpleHistCollection is used when the main detector system
    is simple, and one histogram is good enough to represent the
    data from the whole detector system.
    """

    def __init__(self, hist): self._hist = hist

    def getAll(self): return [self._hist]

    def __call__(self, detector=None): return self._hist

    pass # end of SimpleHistCollection



# version
__id__ = "$Id$"

# End of file 
