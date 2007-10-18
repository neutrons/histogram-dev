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


from ControlPanel import ControlPanel
from HistNotebook import HistNotebook


class UpperPanel(wx.SplitterWindow):

    def __init__(self, *args, **kwds):
        wx.SplitterWindow.__init__(self, *args, **kwds)

        sty = wx.BORDER_SUNKEN
        
        p1 = ControlPanel(self, style=sty)
        
        p2 = HistNotebook(self, style=sty)
        
        self.SetMinimumPaneSize(250)
        self.SplitVertically(p1, p2, 250)

        self.controlPanel = p1; self.histPanel = p2
        return


    def getShelf(self): return self.GetParent().shelf


    def showHist(self, histIdentifier):
        self.histPanel.showHist( histIdentifier )
        return


    def addHistogram(self, histIdentifier):
        self.controlPanel.addHistogram( histIdentifier )
        self.showHist( histIdentifier )
        return


    pass # end of UpperPanel



# version
__id__ = "$Id$"

# End of file 
