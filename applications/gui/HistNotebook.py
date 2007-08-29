#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                         (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import journal
debug = journal.debug("HistNotebook")
warning = journal.warning("HistNotebook")


import wx

class HistNotebook(wx.Notebook):

    def __init__(self, *args, **kwds):
        wx.Notebook.__init__(self, *args, **kwds)
        from HistInfoPanel import HistInfoPanel
        self.histInfoPanel = HistInfoPanel(self)
        from HistPlotPanel import HistPlotPanel
        self.histPlotPanel = HistPlotPanel(self, -1)
        self.AddPage( self.histInfoPanel, "histogram info" )
        self.AddPage( self.histPlotPanel, "plot" )
        return
    
    
    def getShelf(self): return self.GetParent().getShelf()
    
    
    def showHist(self, histIdentifier):
        self.histInfoPanel.showHist( histIdentifier )
        self.histPlotPanel.showHist( histIdentifier )
        return
    
    
    pass #end of HistNotebook



# version
__id__ = "$Id$"

# End of file 
