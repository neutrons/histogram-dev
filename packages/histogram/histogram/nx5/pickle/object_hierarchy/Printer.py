#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

class Printer:

    _INDENT = '    '
    
    def __init__(self):
        self._indent = 0
        return


    def render(self, node):
        self._lines = []
        node.identify(self)
        return self._lines
    
        
    def onBranch(self, node):
        self._write( "%s(%s)" % (
            node.__class__.__name__, node.name) )
        self._indent += 1

        for entry in node.leaves:
            entry.identify(self)

        self._indent -= 1
        return


    def onLeaf(self, node):
        try:
            self._write( "%s(%s): %s" % (
                node.__class__.__name__, node.name, node.data) )
        except:
            self._write( "%s(%s): " % (
                node.__class__.__name__, node.name) ) #+ str(node.data))
        return


    onInstance = onConstruction = onDict = onTuple = onList = onBranch
    onBuiltin = onLink = onGlobal = onLeaf


    def _write(self, content):
        self._lines.append( "%s%s" % (self._INDENT * self._indent, content) )
        return

#version
__id__ = "$Id$"
#End of file

