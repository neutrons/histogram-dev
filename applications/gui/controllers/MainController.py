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


tutorial_url = "http://wiki.cacr.caltech.edu/danse/index.php/HistogramViewer-tutorial"

about_msg = """
Histogram viewer is a GUI application in the ARCS
inelastic neutron scattering (INS) reduction software.
It can be used to plot histograms created from a
reduction procedure.

        DANSE team INS subgroup
   California Institute of Technology
   (C) 2006-2007 All Rights Reserved
"""



from ControllerBase import ControllerBase

class MainController(ControllerBase):


    def __init__(self, toolkit, maingml):
        self.gmlfile = maingml
        self.toolkit = toolkit
        
        #model
        from histogram.applications.gui.models.HistogramContainer import HistogramContainer
        self.histograms = HistogramContainer()

        #data
        self.pyshell_locals = {}
        self.pyshell_locals.update( self.histograms )
        self.focus = None
        self.open_tools_default_dir = '.'
        self.open_data_default_dir = '.'
        self.threads = []
        return


    def __del__(self):
        for thread in self.threads: thread.join()
        return
    

    def main(self):

        self.pyshell_locals['controller'] = self
        
        gmlfile = self.gmlfile
        toolkit = self.toolkit
        
        self.view = view = toolkit.mainView()
        view.controller = self
        self.pyshell_locals[ 'view' ] = view
        
        from luban.gml import gml2gui
        view = gml2gui( gmlfile, self, toolkit.renderer() )
        import pylab
        self.pyshell_locals[ 'pylab'] = pylab
        
        plotwindow = view.getSubview('histogramfigure')
        plotwindow.makePylabUsable()

        self.pyshell_locals['refresh'] = self.refreshPlot
        self.plotCmdHistory = {}

        #add "." to sys.path
        import sys
        sys.path = ['.'] + sys.path

        from Tools import Tools
        self._tools = Tools( self )

        self.addDefaultTools()
        view.start()
        return


    def refreshPlot(self):
        plotwindow = self.view.getSubview('histogramfigure')
        # this is assuming a method 'Refresh' on a view
        plotwindow.Refresh()
        return


    def addNewHistogram( self, name, histogram):
        histograms = self.histograms
        histograms.set( name, histogram )
        self.pyshell_locals.update( histograms )
        names = histograms.keys()
        self.view.getSubview("histogramList").update( names )
        self.SwitchFocus( name )
        return


    def addPythonModuleAsToolset(self, menuname, pyfile):
        '''add a python module as a toolset that shows up
        in the "tools" menu
        '''
        from Tools import toolsetFromPythonModule
        directory, filename = os.path.split( pyfile )
        moduleName, toolset = toolsetFromPythonModule( directory, filename )
        self.addToolset( menuname, toolset )
        return


    def addDefaultTools(self):
        ''' add default tools to the "tools" menu
        '''
        import histogram.applications.gui.tools as tools

        modules = tools.__export__

        for menuname, m in modules:
            pyfile =  m.__file__
            self.addPythonModuleAsToolset( menuname, pyfile )
            continue
        return                


    def addToolset( self, name, toolset):
        ''' add a toolset as a submenu in the "tools" menu
        name is the name of the submenu
        toolset is a dictionary. for each pair of (key, value),
          key will show up as the name of the subsubmenu in the submenu
          value is the function that will be called when the subsubmenu
          is selected.
        '''
        self._tools.addToolset(name, toolset)
        return
        
    
    def OnAbout(self,e):
        toolkit = self.toolkit
        toolkit.messageDialog( None, "Histogram Viewer", about_msg )
        return


    def OnLoadToolset(self, e):
        open_tools_default_dir = self.open_tools_default_dir
        pyfile = self.toolkit.loadfileDialog(
            None, "Open toolset module (any python file)",
            open_tools_default_dir)
        self.open_tools_default_dir = os.path.dirname( pyfile )
        directory, filename = os.path.split( pyfile )
        name, ext = os.path.splitext( filename )
        self.addPythonModuleAsToolset( name , pyfile )


    def OnOnlineTutorial(self, e):
        import webbrowser
        webbrowser.open( tutorial_url )
        return
    
    
    def OnExit(self, evt):
        self.view.end()
        return

    
    def OnOpenHistogramFile( self, evt ):
        open_data_default_dir = self.open_data_default_dir
        pklfile = self.toolkit.loadfileDialog(
            None, "Open histogram data file" ,
            defaultDir = open_data_default_dir )
        self.open_data_default_dir = os.path.dirname( pklfile )
        
        from histogram.hpickle import load
        hist = load( pklfile )
        name = hist.name()
        name = _validVariableName( name )
        name = newHistName( name, self.histograms.keys() )
        self.addNewHistogram( name, hist )
        return



    def OnSelectHistogram(self, evt):
        listview = self.view.getSubview( 'histogramList' )
        index = listview.getSelection()
        names = self.histograms.keys()
        key = names[ index ]
        self.SwitchFocus( key )
        return


    def OnSaveFigure(self, evt):
        figure = self.view.getSubview("histogramfigure")
        filetypes = figure.getPictureTypes()
        toolkit = self.toolkit
        filename = toolkit.savefileDialog( None, "Save figure to file", filetypes )
        if filename: figure.savePlot( filename )
        return


    def OnKeyDownInShellWindow(self, evt):
        view = self.view
        
        #check if <enter> is hit
        if evt.getKeyCode() != 13: return

        from histogram.Histogram import Histogram

        #get a dictinoary of histograms in the shell window locals
        histograms = {}
        for key, value in self.pyshell_locals.iteritems():
            if isinstance(value, Histogram):
                histograms[key] = value
                pass
            continue

        #assign the dictionary to the data model
        changed = self.histograms.assign( histograms )

        #if there is change, we need to update views
        if changed: 
            names = self.histograms.keys()
            view.getSubview("histogramList").update( names )
            if len(names) > 0:
                focus = names[-1]
                self.SwitchFocus( focus )
                pass
            pass
        else:
            pyshell = view.getSubview( "pythonshell" )
        
            #check whether "plotting" command is involved
            lastcommand = pyshell.history[0]
            for cmd in ['pylab', ]: # getpylabcmds():
                if lastcommand.find( cmd ) != -1:
                    #if so, update the plot
                    self.refreshPlot()
                    # and also keep the command in the history
                    focus = self.focus
                    if focus:
                        history = self.plotCmdHistory.get(focus) or []
                        history.append( lastcommand )
                        self.plotCmdHistory[ focus ] = history
                        pass # end if focus
                    pass # end if lastcommand
                continue # end for cmd 
            pass
        return


    def removeHistogram(self, histogram):
        listbox = self.view.getSubview('histogramList')
        histograms = self.histograms
        names = histograms.keys()
        index = names.index( histogram )
        #index = listbox.getSelection()
        selected = histogram
        self.histograms.delete( selected )
        del self.pyshell_locals[ selected ]
        del self.plotCmdHistory[ histogram ]
        #new list of histogram names
        names = histograms.keys()
        # keep listbox in sync
        listbox.update( names )
        #move cursor to the next histogram
        if len(names) != 0:
            if index >= len( names ):
                # if what is just deleted is the last item, then
                # we refocus to the current last item
                focus = names[ -1 ]
            else:
                # otherwise, we switch to the item that was just after
                # the deleted one
                focus = names[index]
            self.SwitchFocus( focus )
            pass
        else:
            #no histograms
            self.view.getSubview("histogramfigure").update( None )
            self.focus = None
            pass
        return


    def OnKeyDownInListWindow(self, evt):
        #print evt.getKeyCode()
        if evt.getKeyCode( ) == 127: # delete
            listbox = self.view.getSubview('histogramList')
            histograms = self.histograms
            names = histograms.keys()
            index = listbox.getSelection()
            selected = names[ index ]
            self.removeHistogram( selected )
        return

    
    #helpers
    
    def SwitchFocus( self, key ):
        print "MainController.SwitchFocus: self.focus = %s, key=%s" % (
            self.focus, key )
        if self.focus == key: return
        self.focus = key
        names = self.histograms.keys()
        histogram = self.histograms.get( key ) 
        self.view.getSubview("histogramfigure").update( histogram )
        self.view.getSubview("histogramList").select( names.index( key ) )
        # rerun commands 
        if histogram:
            history = self.plotCmdHistory.get(key) or []
            goodhistory = []
            for i, cmd in enumerate(history):
                try:
                    exec cmd in self.pyshell_locals
                    goodhistory.append( cmd )
                except: pass
                continue
            self.plotCmdHistory[key] = goodhistory
        return
        

    pass # end of MainController




def newHistName(name, names):
    "return a unique name for the new histogram"
    #not a good algorithm, but it works for now.
    if name not in names: return name
    # h0, h1, ..., h99 
    for i in range(100):
        new = "%s%d" % (name, i)
        if new not in names: return new
        continue
    raise RuntimeError, "Cannot find a good name for the new histogram '%s'. Existing histograms: %s" %(name, hists.keys() )



def getpylabcmds():
    import pylab
    cmds = pylab.__dict__.keys()
    return cmds


def _validVariableName( name ):
    import string
    good = string.ascii_letters + string.digits + '_' 
    ret = []
    for i in name:
        if i not in good: i = '_'
        ret.append(i)
        continue
    return ''.join( ret )


import os


# version
__id__ = "$Id$"

# End of file 
