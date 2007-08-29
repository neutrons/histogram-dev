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


## \package histogram.ins
##
## Histograms for inelastic neutron scattering experiments


def arcshistograms( shorthistogram, longhistogram ):
    from histogram import makeHistogramCollection as make
    from ARCSDetHistCollection import ARCSDetHistCollection
    return make( (shorthistogram, longhistogram), ARCSDetHistCollection )


# version
__id__ = "$Id$"

# End of file 
