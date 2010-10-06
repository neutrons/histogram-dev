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

try:
    import pylab
except SystemError:
    import matplotlib, pylab

import numpy as N


def plothist( histogram, **kwds ):
    dim = histogram.dimension()
    if dim != 1:
        raise NotImplementedError, "dimension: %s" % dim
    x = histogram.axes()[0].binCenters()

    from plotter import process_Iaxis_unit
    scale_factor, Iunit = process_Iaxis_unit( histogram.unit() )
    y = histogram.I * scale_factor
    yerr2 = histogram.E2 
    yerr = N.sqrt( yerr2 ) * scale_factor
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
