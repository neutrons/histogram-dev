#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \package histogram.ins.ARCSDetHistCollection
## manage a collection of histograms for the ARCS detector system
##
## a histogram is a data defined on a nD grid. For ARCS, one
## histogram is not enough to represent all data. In ARCS detector system,
## there are  two kinds of detector tubes, one long, the
## ohter short. Two histograms are needed for two kinds of tubes:
##
##   - longData( detector, pixel, tof )
##   - shortData( detector, pixel, tof )
##
## This class will collect all histograms and dispatch requests for
## histograms to the appropriate histogram
##



from histogram.DetHistCollection import DetHistCollection as DHCBase


class ARCSDetHistCollection(DHCBase):

    
    def __init__(self, shortDetData, longDetData):
        self._short = shortDetData
        self._long = longDetData
        return


    def getAll(self): return [self._short, self._long]
    

    def __call__(self, detector=None):
        if detector is None or detector.height() > 999.0: return self._long
        return self._short
    
    pass # end of ARCSDetHistCollection



# version
__id__ = "$Id: ARCSDetHistCollection.py 1159 2006-10-12 04:53:25Z linjiao $"

# End of file 
