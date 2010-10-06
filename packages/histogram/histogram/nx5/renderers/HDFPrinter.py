#!/usr/bin/env python
# Copyright (C) 2005 Timothy M. Kelley All rights reserved

from HDFVisitor import HDFVisitor

class HDFPrinter(HDFVisitor):

    _INDENT = '    '
    
    def render(self, node):
        node.identify(self)
        

    def __init__(self):
        self._indent = 0
        return


    def onGroup(self, node):
        self._render(node, "Group")
        self._indent += 1

        for child in node.children():
            child.identify(self)

        self._indent -= 1
        return


    def onDataset(self, node):
        self._render(node, "Dataset")
        return

    def _render(self, node, code):
        attrstring = ''
        
        for name, value in node.attributes().items():
            if name in ['name', 'class']: continue
            attrstring += ' %s=%s' % (name, value)
            continue
        
        print "%s(%s) name=%s class=%s path=%s%s" % \
              (self._INDENT*self._indent, code, node.name(), node.className(), node.path(),
               attrstring)
        return

#version
__id__ = "$Id: HDFPrinter.py 123 2007-03-24 05:09:30Z linjiao $"
#End of file

