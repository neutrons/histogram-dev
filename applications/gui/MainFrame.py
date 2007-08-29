#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx



ID_ABOUT=201
ID_HELPONLINETUTORIAL=202
ID_FILEOPENPKL=102
ID_FILEOPENPHAROSIDPT=103
ID_FILESAVEFIGURE=104
ID_EXIT=199


about_msg = """
Histogram viewer is a GUI application in the ARCS
inelastic neutron scattering (INS) reduction software.
It can be used to plot histograms created from a
reduction procedure.

   DANSE team INS subgroup
   California Institute of Technology
   (C) 2006 All Rights Reserved
"""


tutorial_url = "http://wiki.cacr.caltech.edu/danse/index.php/HistogramViewer-tutorial"



class MainFrame(wx.Frame):
    
    def __init__(self, parent=None, id=-1, name = "Histogram Viewer", pos = wx.DefaultPosition):
        wx.Frame.__init__(self, parent,id,name, pos, (800,650))
        self.drawscreen()
        return


    def drawscreen(self):
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        self.createMenu()
        self.createPanel()
        self.Show(True)
        return
    

    def createMenu(self):
        # Setting up the menu.
        filemenu= wx.Menu()
        filemenu.Append(ID_FILEOPENPKL, "&Open pickled histogram", " load a histogram that was saved by python pickle") 
        filemenu.Append(ID_FILEOPENPHAROSIDPT, "Open &PHAROS I(det,pix,tof)", " load a I(detector, pixel, tof) histogram from a Pharos data file")
        filemenu.Append(ID_FILESAVEFIGURE, "&Save plot", " save the plot to a file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")

        helpmenu = wx.Menu()
        helpmenu.Append(ID_HELPONLINETUTORIAL, "&Online Tutorial",
                        " Open online tutorial")
        helpmenu.Append(ID_ABOUT, "&About"," Information about this program")
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"&Help") # Adding the "helpmenu" to the MenuBar
        
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        #event handler connections
        wx.EVT_MENU(self, ID_FILEOPENPHAROSIDPT, self.OnFileOpenPHAROSIdpt)
        wx.EVT_MENU(self, ID_FILEOPENPKL, self.OnFileOpenPKL)
        wx.EVT_MENU(self, ID_FILESAVEFIGURE, self.OnFileSaveFigure)
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout) # 
        wx.EVT_MENU(self, ID_HELPONLINETUTORIAL, self.OnOnlineTutorial) # 
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)   # 
        return


    def createPanel(self):
        from MainPanel import MainPanel
        self.panel = MainPanel( self )
        return


    # event handlers

    def OnFileOpenPKL(self, evt):
        d = wx.FileDialog( self, "load pickled histogram" )
        if d.ShowModal() != wx.ID_OK: d.Destroy(); return
        pklfile = d.GetPath()
        d.Destroy()
        import pickle
        hist = pickle.load( open( pklfile ) )
        self.panel.addHistogram( hist.name(), hist )
        return

    
    def OnFileOpenPHAROSIdpt(self, evt):
        d = wx.FileDialog( self, "load pharos data file" )
        if d.ShowModal() != wx.ID_OK: d.Destroy(); return
        pharos_datafile = d.GetPath()
        d.Destroy()

        d = wx.FileDialog( self, "load pharos instrument definition file")
        if d.ShowModal() != wx.ID_OK: d.Destroy(); return
        pharos_instrfile = d.GetPath()
        d.Destroy()
        
        d = wx.TextEntryDialog(
            self, "What is the entry in the pharos data file\n %s" %pharos_datafile,
            'Entry', '/run_???')
       
        if d.ShowModal() != wx.ID_OK: d.Destroy(); return
        entry = d.GetValue()
        d.Destroy()

        d = wx.TextEntryDialog(
            self, "Please give the new histogram a name:",
            "histogram name", "new_hist" )
        if d.ShowModal() != wx.ID_OK: d.Destroy(); return
        histIdentifier = d.GetValue()
        d.Destroy()        

        #print pharos_datafile, pharos_instrfile, entry
        hist = getPharosDetPixTOFData( pharos_instrfile, pharos_datafile, entry)
        self.panel.addHistogram( histIdentifier, hist )
        return


    def OnFileSaveFigure(self, e):
        canvas = self.panel.shelf['histPlotPanel'].canvas

        # Fetch the required filename and file type.
        filetypes = canvas._get_imagesave_wildcards()
        dlg =wx.FileDialog(self, "Save to file", "", "", filetypes,
                           wx.SAVE|wx.OVERWRITE_PROMPT|wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            dirname  = dlg.GetDirectory()
            filename = dlg.GetFilename()
            print ('Save file dir:%s name:%s' % (dirname, filename), 3, self)
            import os
            canvas.print_figure(os.path.join(dirname, filename))
            pass
        return


    def OnOnlineTutorial(self, e):
        import webbrowser
        webbrowser.open( tutorial_url )
        return

    
    def OnAbout(self,e):
        d= wx.MessageDialog( self, about_msg, "Histogram Viewer", wx.OK)
        # Create a message dialog box
        d.ShowModal() # Shows it
        d.Destroy() # finally destroy it when finished.
        return


    def OnExit(self,e):
        self.Close(True)  # Close the frame.return
        return


    pass # end of MainFrame



#simple dialog to get entry in pharos hdf5 file
#class H5EntryDialog

class SimpleDialog(wx.Dialog):

    "simple dialog with one title and one input box"
    
    def __init__(self, parent = None,
                 size = wx.DefaultSize, pos = wx.DefaultPosition,
                 style = wx.DEFAULT_DIALOG_STYLE,
                 pharos_datafile = None
                 ):

        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, -1, "entry in Pharos data file %s" % pharos_datafile,
                   pos, size, style)
        self.PostCreate(pre)

        vbox = wx.BoxSizer( wx.VERTICAL ) 
        
        self.text = wx.TextCtrl(self, -1, "/run_??", (90, 50), (200,-1))
        self.Bind(wx.EVT_TEXT, self.OnEvtText, self.text)
        
        vbox.Add( self.text, 0, wx.ALIGN_CENTER, 20 )
        # add ok and cancel buttons to sizer
        ok = wx.Button(self, wx.ID_OK, "OK")
        cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")

        buttonBox = wx.BoxSizer( wx.HORIZONTAL )
        buttonBox.Add(ok, 0, wx.ALL, 20); buttonBox.Add(cancel, 0, wx.ALL, 20)
        
        vbox.Add(buttonBox, 0, wx.ALIGN_CENTER, 20)

        # now paint the screen
        border = wx.BoxSizer()
        border.Add(vbox, 1, wx.GROW|wx.ALL, 25)
        border.Fit(self)
        self.SetSizer(border)
        self.Layout()        
        
        self.userinput = None
        return


    def OnEvtText(self, evt):
        self.userinput = self.text.GetValue().replace(' ','')
        return 
    

    pass # end of H5EntryDialog



def getPharosDetPixTOFData( pharos_instrfile, pharos_datafile, entry):
    r = getPharosRun(pharos_instrfile, pharos_datafile, entry)
    return r.getDetPixTOFData()


def getPharosRun( pharos_instrfile, pharos_datafile, entry):
    pharos, geometer = createPharosInstrument( pharos_instrfile )
    import nx5.file
    nxf = nx5.file.file( pharos_datafile, 'r' )
    from measurement.PharosRun import PharosRun
    pharosRun = PharosRun( pharos, geometer, nxf, entry )
    return pharosRun


pharosInstruments = {}
def createPharosInstrument(instrumentFilename):
    if not pharosInstruments.has_key(instrumentFilename):
        pharosInstruments[instrumentFilename] = _createPharosInstrument( instrumentFilename )
        pass
    return pharosInstruments[instrumentFilename]
    

def _createPharosInstrument(instrumentFilename):
    from instrument.factories.PharosBootstrap import InstrumentFactory
    ifact = InstrumentFactory()
    pharos, geometer = ifact.construct( detPackFilename =
                                        instrumentFilename)
    return pharos, geometer
    

# version
__id__ = "$Id$"

# End of file 
