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
manage a collection of histograms for a detector system

  - NAME: DetHistCollection
  - PURPOSE: manage a collection of histograms for a detector system
  - DESCRIPTION: a histogram is a data defined on a nD grid. sometime one histogram
  is not enough to represent all data collected from a detector system. For example,
  in ARCS detector system, there are  two kinds of detector tubes, one long, the
  ohter short. Two histograms are needed for two kinds of tubes:
    - longData( detector, pixel, tof )
    - shortData( detector, pixel, tof )
  The class in this module will collect all histograms and dispatch requests for
  histograms to the appropriate histogram
  - RELATED:
  - TODOs:
"""


class DetHistCollection:

    def __call__( self, detector=None ):
        """According to detector property, determine which histogram should
        be used.
        """
        raise NotImplementedError , "%s must provide __call__" % (
            self.__class__.__name__)

    
    def getAll( self, detector=None ):
        """return a list of all hists
        """
        raise NotImplementedError , "%s must provide 'getAll'" % (
            self.__class__.__name__)


    def __iter__(self): return self.getAll().__iter__()
    
    pass



# version
__id__ = "$Id$"

# End of file 
