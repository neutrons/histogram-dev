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


from pyre.components.Component import Component


class plotter(Component):


    class Inventory(Component.Inventory):
        import pyre.inventory
        pass # end of Inventory


    def __getattribute__(self, key):
        try:
            return object.__getattribute__(self, key)
        except:
            assert self._engine is not None, "no engine for component %s" % (
                self.__class__.__name__ )
            return getattr(self._engine, key)
        raise "should not reach here"


    def __init__(self, name='plotter'):
        Component.__init__(self, name, facility='plotter')
        return


    def _init(self):
        Component._init(self)
        from histogram.plotter import HistogramMplPlotter as P
        self._engine = P()
        return


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Sat Jul 21 21:49:23 2007

# End of file 
