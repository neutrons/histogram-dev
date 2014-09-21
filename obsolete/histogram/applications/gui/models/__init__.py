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


_histograms = None

def histograms():
    global _histograms
    if _histograms is None:
        from HistogramContainer import HistogramContainer
        _histograms = HistogramContainer()
        pass
    return _histograms


def models():
    from ModelContainer import ModelContainer
    models = ModelContainer( )
    models.set( "histograms", histograms() )
    return models


# version
__id__ = "$Id$"

# End of file 
