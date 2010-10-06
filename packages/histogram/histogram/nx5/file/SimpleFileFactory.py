#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.file")


from QuasiSingleton2 import QuasiSingleton


class FileFactory( QuasiSingleton):
    """makes files for people"""


    def call( self, filename, mode, *args, **kwds):
        
        # prepare filesystem
        fs = self.__makeFS( filename, mode)

        # prepare graph
        fileGraph = self.__makeGraph( fs, filename)

        # prepare XML
        xmlRep = self.__makeXML( fileGraph.root())
        
        # make File
        from File2 import File
        theFile = File( filename, mode, fs, fileGraph, xmlRep)

        return theFile


    def __makeFS( self, filename, mode):
        debug.log("filename: %s" % filename)
        
        # _checkFileValid(filename)

        debug.log("Attempting to open file")

        try:
            from hdf5fs import h5fs
            fs = h5fs.H5fs( filename, mode)
        except IOError, msg:
            print "File unable to initialize properly:", msg
            debug.log("File unable to initialize properly: %s" % str(msg))
            raise

        debug.log("nexus file opened")

        return fs
        
    
    def __makeGraph( self, fs, filename):
        
        from nx5.renderers.Graph_FromFile import Renderer as GraphRenderer
        graphRenderer = GraphRenderer()
        graph = graphRenderer.render( fs, filename)
        from FileGraph import FileGraph
        fileGraph = FileGraph( graph)

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


    def __init__( self):
        QuasiSingleton.__init__( self)
#        print "nx5.file.SimpleFileFactory.__init__()"
        return
    # end of SimpleFileFactory


# helper:
    
def __checkFileValid(filename):
    import os
    if not os.path.isfile(filename): 
        errstr = 'Invalid file name "%s"'%filename 
        raise IOError,errstr
    return


# version
__id__ = "$Id: SimpleFileFactory.py 81 2005-06-22 22:43:53Z tim $"

# End of file
