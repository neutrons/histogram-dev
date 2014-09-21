

class Tools:

    """data structure to help dispatch evthandlers to
    the core functionality to be provide by the
    menu items in the tools menu"""


    def dispatch(self, evthandler):
        return self.evthandler_registry[ evthandler ]


    def __init__(self, mainController ):
        """
        toolkit: gui toolkit
        toolsMenu: tools menu
        parent_refresh_function: parent window's refresh function
        """
        toolkit = mainController.toolkit
        toolsMenu = mainController.view.getSubview( "toolsMenu" )
        parent_refresh_function = mainController.refreshPlot

        self.mainframe = mainController.view.getSubview( 'mainframe' )
        self.evthandler_registry = {}
        self.toolsMenu = toolsMenu
        self.toolkit = toolkit
        self.submenus = {}
        self.parent_refresh_function = parent_refresh_function
        self.evaluation_environment = mainController.pyshell_locals
        return


    def addSubMenu(self, name):
        'add a sub menu to the menu "tools"'
        if name in self.submenus: self.deleteSubMenu(name)
        toolsMenu = self.toolsMenu
        toolkit = self.toolkit
        newsubmenu = toolkit.menu( self.mainframe, name )
        newmenuitem = toolkit.menuitem( name, submenu = newsubmenu )
        self.submenus[ name ]  = newsubmenu
        toolsMenu.append( newmenuitem )
        return


    def deleteSubMenu(self, name):
        self.toolsMenu.delete( name )
        del self.submenus[name]
        return
        

    def addTool( self, name, func, submenu):
        '''add a subsubmenu item to the submenu. the new item will be
        given the name "name", and will provide functionality "func"
        '''
        toolkit = self.toolkit

        #
        submenu = self.submenus[ submenu ]
        def evthandler(evt):
            core = self.dispatch( evthandler )
            try:
                core( self.evaluation_environment )
            except:
                import traceback
                tb = traceback.format_exc()
                toolkit.messageDialog(None, "Error", tb)
                return
            self.parent_refresh_function()
            return

        self.evthandler_registry[ evthandler ] = func

        item = toolkit.menuitem( name, callbacks = {'click': evthandler} )
        submenu.append( item )
        return
        

    def addToolset(self, name, toolset):
        ''' add a toolset as a submenu in the "tools" menu
        name is the name of the submenu
        toolset is a dictionary. for each pair of (key, value),
          key will show up as the name of the subsubmenu in the submenu
          value is the function that will be called when the subsubmenu
          is selected.
        '''
        name = name.replace( '_', ' ' )
        self.addSubMenu( name )
        for k,v in toolset: self.addTool( k, v, name )
        return
        
    
    pass # end of Tools
        


def toolsetFromPythonModule(directory, filename):
    """create a toolset from a python module

    directory, filename: gives the location of the python module
    return: (moduleName, toolset)
      toolset: a dictionary of {name: func}
    """
    
    import sys

    print "toolsetFromPythonModule: directory=%s, filename=%s" % (
        directory, filename )
    #do we need to restore the sys.path?
    if directory not in sys.path:
        sys.path = [directory] + sys.path
        pass

    moduleName, ext = os.path.splitext( filename )

    m = __import__( moduleName )
    reload( m )

    toolset = []
    try:
        d = m.__export__
    except AttributeError :
        d = _listFromDict( m.__dict__ )
        pass
    for k,v in d:
        if k.startswith('_'): continue
        if not callable( v ): continue
        toolset.append( (k,v) )
        continue
    
    return moduleName, toolset
    

def _listFromDict( d ):
    return [ (k,v) for k,v in d.iteritems() ]


import os
