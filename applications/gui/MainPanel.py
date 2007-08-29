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


import wx

from LowerPanel import LowerPanel
from UpperPanel import UpperPanel



class MainPanel(wx.SplitterWindow):


    def __init__(self, parent):
        self.createShelf()
        self.createHistShelf()

        wx.SplitterWindow.__init__(self, parent, -1, style = wx.SP_LIVE_UPDATE)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChanging)


        sty = wx.BORDER_SUNKEN
        
        self.upper = p1 = UpperPanel(self, style=sty)
        
        self.lower = p2 = LowerPanel(self, style=sty)
        
        self.SetMinimumPaneSize(20)
        self.SplitHorizontally(p1, p2, -200)

        self.initialUpdateShelf()
        return


    def createShelf(self):
        self.shelf = {}
        #cmd = "from histogram.plotter import plot1d as plot1dHist, plot2d as plot2dHist"
        #exec cmd in self.shelf
        #cmd = "from pylab import *"
        #exec cmd in self.shelf
        return


    def initialUpdateShelf(self):
        mainPanel = self
        upperPanel = mainPanel.upper
        lowerPanel = mainPanel.lower
        controlPanel = upperPanel.controlPanel
        histPanel = upperPanel.histPanel
        histPlotPanel = histPanel.histPlotPanel
        self.shelf.update( {"mainPanel": mainPanel,
                            "upperPanel": upperPanel,
                            "lowerPanel": lowerPanel,
                            "controlPanel": controlPanel,
                            "histPanel": histPanel,
                            "histPlotPanel": histPlotPanel,
                            } )
        return


    def createHistShelf(self):
        self.histShelf = {}
        self.shelf['hists'] = self.histShelf
        return


    def print_figure(self, filename):
        self.shelf['histPlotPanel'].print_figure( filename )
        return


    def addHistogram(self, identifier, hist):
        new = {identifier: hist}
        self.shelf.update( new )
        self.histShelf.update( new )
        self.upper.addHistogram( identifier )
        return


    def redrawHistogramPlot(self):
        self.shelf["histPanel"].histPlotPanel.Refresh()
        return


    def OnSashChanged(self, evt):
        #print "sash changed to %s\n" % str(evt.GetSashPosition())
        return
        

    def OnSashChanging(self, evt):
        #print "sash changing to %s\n" % str(evt.GetSashPosition())
        # uncomment this to not allow the change
        #evt.SetSashPosition(-1)
        return
    
                                            
    pass # end of MainPanel



# version
__id__ = "$Id$"

# End of file 
