#!/usr/bin/env python
# (c) Copyright 2005 T. M. Kelley, California Institute of Technology

import xml.sax
   
class Searcher(xml.sax.ContentHandler):
    """
    ctor 2 args: targetType (string) and targetAttributes (dict)
    
    A SAX-based content handler that searches an XML document for
    desired node. Special to simple nexus in that it makes
    assumptions about content model---there are only <Group>s and
    <Dataset>s.
    """
    
    def startElement(self, name, attributes):
        self._currentNode = (name,attributes)
        self._nodeStack.append(self._currentNode)

        if name == self._targetType:
            nodeAttrs = {}
            for item in attributes.keys():
                nodeAttrs[item] = attributes[item]
            match = dictIsSubset(self._goal, nodeAttrs)
            if match == 1:
                stack = []
                for i in range(len(self._nodeStack)):
                    stack.append( self._nodeStack[i])
                self._results.append(stack )
        return

    def endElement(self, name):
        self.currentNode = self._nodeStack.pop()
        return

    def results(self):
        return self._results

    def targetType(self): return seld._targetType

    def targetAttributes(self): return self._goal

    def __init__(self, targetType, targetAttributes):
        """
       
        """
        xml.sax.ContentHandler.__init__(self)
        self._nodeStack = []
        self._currentNode = None
        self._documentNode = None
        self._targetType = targetType
        self._goal = targetAttributes
        self._results = []
        return

# Helpers
def dictIsSubset(a, b):
    """Is dictionary 'a' a subset of dictionary 'b'?
    True if every key:value in 'a' is in 'b'.
    """
    retval = 1
    akeys = a.keys()
    bkeys = b.keys()
    for item in akeys:
        if item in bkeys:
            if a[item] == b[item]: retval *= 1
            else: retval *= 0
        else:
            retval *= 0
    return retval

# version
__id__ = "$Id: Searcher.py 5 2005-01-20 22:59:57Z tim $"

# End of file


