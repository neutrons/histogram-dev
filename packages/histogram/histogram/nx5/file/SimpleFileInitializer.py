#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal, sys
debug = journal.debug("nx5.file")

class FileInitializer( object):

    def initialize( self, filename, mode, fs = None):

        if fs is None:
            # prepare filesystem
            fs = self.__makeFS( filename, mode)
        
        debug.log("__makeFS complete, ref count of fs.h5ref: %s" %
                  sys.getrefcount( fs.h5ref))
        
        # prepare graph
        fileGraph = self.__makeGraph( fs, filename)
        debug.log("__makeGraph complete, ref count of fs.h5ref: %s" %
                  sys.getrefcount( fs.h5ref))

        # prepare XML
        xmlRep = self.__makeXML( fileGraph.root())
        
        return fs, fileGraph, xmlRep


    def __makeFS( self, filename, mode):
        debug.log("filename: %s" % filename)
        
        # _checkFileValid(filename)

        debug.log("Attempting to open file")

        fs = None
        try:
            from hdf5fs import h5fs
            fs = h5fs.H5fs( filename, mode)
        except IOError, msg:
            print "File unable to initialize properly:", msg
            debug.log("File unable to initialize properly: %s" % str(msg))
            raise
        debug.log("H5fs.__init__ complete, ref count of fs.h5ref: %s" %
                  sys.getrefcount( fs.h5ref))

        debug.log("nexus file opened")

        return fs
        
    
    def __makeGraph( self, fs, filename):

        debug.log("beginning __makeGraph")
        
        from nx5.renderers.Graph_FromFile import Renderer as GraphRenderer
        graphRenderer = GraphRenderer()
        debug.log("about to render file to graph")
        graph = graphRenderer.render( fs, filename)

        debug.log("done rendering")

        from FileGraph import FileGraph
        fileGraph = FileGraph( graph)

        debug.log("done")

        return fileGraph
    

    def __makeXML( self, root):
        
        from nx5.renderers.XML_FromGraph import Renderer as XMLRenderer

        from pyre.weaver import Weaver
        wvr = Weaver.Weaver()
        # need to put the component through its lifecycle
        wvr._defaults(); wvr._configure(); wvr._init()
        wvr.renderer = XMLRenderer()

        debug.log("About to render XML structure")
        xml = wvr.render( root)
        
        from XMLRep import XMLRep
        xmlRep = XMLRep( xml)

        return xmlRep


    def __init__( self, ):
        return
    

# helper:
    
def __checkFileValid(filename):
    import os
    if not os.path.isfile(filename): 
        errstr = 'Invalid file name "%s"'%filename 
        raise IOError,errstr
    return

        
# version
__id__ = "$Id: SimpleFileInitializer.py 141 2008-06-01 15:44:12Z linjiao $"

# End of file
