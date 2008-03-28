#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import pylab
import numpy as N


def plothist( histogram, **kwds ):
    dim = histogram.dimension()
    if dim != 1:
        raise NotImplementedError, "dimension: %s" % dim
    x = histogram.axes()[0].binCenters()
    y = histogram.I
    yerr2 = histogram.E2
    yerr = N.sqrt( yerr2 )
    pylab.errorbar( x, y, yerr = yerr, **kwds )
    return 


_plot = pylab.plot
def plot(*args, **kwds):
    if len(args) == 1 and isHistogram(args[0]):
        plothist( args[0], **kwds )
        return
    _plot( *args, **kwds )
    return

pylab.plot = plot




def isHistogram( candidate ):
    from histogram.Histogram import Histogram
    return isinstance( candidate, Histogram )


# version
__id__ = "$Id$"

# End of file 
