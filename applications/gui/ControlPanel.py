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


ID_HISTSELECTION = 201

import wx

class ControlPanel(wx.Panel):

    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)


        sizer = wx.BoxSizer()
        
        hs = \
           wx.TreeCtrl(self, ID_HISTSELECTION, style =
                       wx.TR_DEFAULT_STYLE #| wx.TR_HAS_VARIABLE_ROW_HEIGHT
                       )
        self.histSelection = hs
        
        self.hsRoot = hs.AddRoot('Histograms')
        hs.Expand( self.hsRoot )

        hs.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=ID_HISTSELECTION)
        
        sizer.Add(hs, 1, wx.EXPAND, 5)

        self.SetSizer(sizer)
        self.SetAutoLayout(1)
        sizer.Fit(self)
        return


    def OnSelChanged(self, event):
        item = event.GetItem()
        itemText = self.histSelection.GetItemText(item)
        self.showHist( itemText )
        return
    
    
    def showHist(self, histName):
        self.GetParent().showHist( histName )
        return


    def addHistogram(self, histIdentifier):
        newItem = self.histSelection.AppendItem( self.hsRoot, histIdentifier )
        self.histSelection.SelectItem( newItem )
        return


    pass #end of ControlPanel


# version
__id__ = "$Id$"

# End of file 
