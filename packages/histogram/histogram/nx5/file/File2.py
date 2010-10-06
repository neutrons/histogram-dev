#!/usr/bin/env python
# (c) Copyright 2005 T. M. Kelley, California Institute of Technology


class File(object):

    def addNode( self, node):
        self.__approveAddition( node)
        self.__addNodeToGraph( node)
        self.__addNodeToFS( node)
        self.__addNodeToXML(  node)
        return
    

    def deleteNode( self, selector, node):
        raise NotImplementedError, "NIY!"
##         self.__approveDeletion( self, selector, node)
##         self.__deleteNodeFromGraph( self, selector, node)
##         self.__deleteNodeFromFile( self, selector, node)
##         self.__deleteNodeFromXML(  self, selector, node)
##         return
    

    def filename( self):
        return self._filename


    def fs( self):
        return self._fs


    def getNode( self, path):
        """getNode( path) -> node or None
        Get the node at <path>. If no such path in the file, None returned."""
        return self._graph.pathToNode( path)
        

    def graph( self):
        return self._graph


    def selector( self):
        from Selector import Selector
        selector = Selector( self._filename, self._fs)
        return selector


    def xmlRep( self):
        return  self._xmlRep


    def xmlString( self):
        return self._xmlRep.asString()


    def __init__(self, filename, mode, filesystem, graph, xmlRep,
                 fsRenderer = None, xmlRenderer = None):
        """File( filename, mode, filesystem, graph, xmlRep, fsRenderer = None,
        xmlRenderer = None): -> new File object.

        XMLRenderer must be compatible with pyre.weaver
        """
        if fsRenderer is None:
            from nx5.renderers.File_FromGraph import Renderer as FileRenderer
            fsRenderer = FileRenderer( filename, fs = filesystem)

        if xmlRenderer is None:
            from nx5.renderers.XML_FromGraph import Renderer as XMLRenderer
            xmlRenderer = XMLRenderer()
        from pyre.weaver import Weaver
        wvr = Weaver.Weaver()
        # need to put the component through its lifecycle
        wvr._defaults(); wvr._configure(); wvr._init()
        wvr.renderer = xmlRenderer
            
        self._filename = filename
        self._mode = mode
        self._fs = filesystem
        self._graph = graph
        self._xmlRep = xmlRep
        self._fsRenderer = fsRenderer
        self._xmlWeaver = wvr
        
        return

    #____________________ end of public interface _____________________


    def __addNodeToGraph( self,  node):
        self._graph.addNode( node)
        return


    def __addNodeToFS( self, node):
        self._fsRenderer.render( node)
        return
    

    def __addNodeToXML( self, node):
        """Right now, simply creates new xml rep"""
        xmlLines = self._xmlWeaver.render( self._graph.root())
        from XMLRep import XMLRep
        self._xmlRep._rep = xmlLines
        return


    def __approveAddition( self, node):
        return True


    def __approveDeletion( self, node):
        return True


    def __deleteNodeFromGraph( self, selector, node):
        self._graph.deleteNode( selector, node)
        return


    def __deleteNodeFromFS( self, selector, node):
        raise NotImplementedError, "Not done yet!"


    def __deleteNodeFromXML( self, selector, node):
        self._xmlRep.deleteNode( selector, node)
        return

    
# version
__id__ = "$Id: File2.py 81 2005-06-22 22:43:53Z tim $"

# End of file
