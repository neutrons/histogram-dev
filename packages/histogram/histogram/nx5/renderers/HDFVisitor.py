#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

msgBase = 'class %s must override %s'

import journal
debug = journal.debug("nx5.renderers")


class HDFVisitor(object):

    def onDataset(self, node):
        msg = msgBase % (self.__class__.__name__, 'onDataset')
        raise NotImplementedError, msg


    def onDetectorArray( self, node):
        msg = msgBase % (self.__class__.__name__, 'onDetectorArray')
        raise NotImplementedError, msg


    def onDetectorPack( self, node):
        msg = msgBase % (self.__class__.__name__, 'onDetectorPack')
        raise NotImplementedError, msg


    def onGroup(self, node):
        msg = msgBase % (self.__class__.__name__, 'onGroup')

        debug.log("Group name: %s, class: %s, path: %s" % 
                  (node.name(), node.className(), node.path())
                  )
        raise NotImplementedError, msg


    def onInstrument( self, node):
        msg = msgBase % (self.__class__.__name__, 'onInstrument')
        raise NotImplementedError, msg


    def onLPSD( self, node):
        msg = msgBase % (self.__class__.__name__, 'onLPSD')
        raise NotImplementedError, msg


    def onLPSDPixel( self, node):
        msg = msgBase % (self.__class__.__name__, 'onLPSDPixel')
        raise NotImplementedError, msg
    

    def onModerator( self, node):
        msg = msgBase % (self.__class__.__name__, 'onModerator')
        raise NotImplementedError, msg
    

    def onMonitor( self, node):
        msg = msgBase % (self.__class__.__name__, 'onMonitor')
        raise NotImplementedError, msg
    

#version
__id__ = "$Id: HDFVisitor.py 88 2005-07-16 16:12:36Z tim $"

#end of file
