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


# make sure pylab uses WXAgg
import matplotlib as mpl
mpl.use('WXAgg')
del mpl


from pyre.applications.Script import Script


class HistogramGUIApp(Script):


    class Inventory(Script.Inventory):

        import pyre.inventory

        toolkit = pyre.inventory.str('toolkit', default='wx')
        toolkit.meta['tip'] = 'the gui toolkit to use'

        maingml = pyre.inventory.str('maingml', default='')
        maingml.meta['tip'] = 'path to the main gml file'

        pass # end of Inventory


    def main(self, *args, **kwds):
        from histogram.applications.gui.controllers.MainController import MainController
        m = MainController ( self.toolkit, self.maingml )
        m.main()
        return


    def __init__(self):
        Script.__init__(self, 'HistogramGUIApp')
        return


    def _defaults(self):
        Script._defaults(self)
        return


    def _configure(self):
        Script._configure(self)
        self.toolkit = self.inventory.toolkit
        self.maingml = self.inventory.maingml
        return


    def _init(self):
        Script._init(self)
        from luban.gml import toolkits
        toolkit = toolkits.__dict__.get( self.toolkit )
        if toolkit is None: raise "Cannot find toolkit %s" % self.toolkit
        self.toolkit = toolkit

        if self.maingml == '':
            from histogram.paths import etc

            App = self.__class__.__name__
            import os
            self.maingml = os.path.join( etc, App, "main.gml" )
            pass
        return


def main():
    app = HistogramGUIApp()
    return app.run()


# version
__id__ = "$Id$"

# End of file 
