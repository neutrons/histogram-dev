#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
debug = journal.debug("nexml.parser")


from pyre.xml.Node import Node
import urllib


class AbstractNode(Node):


    def __init__(self, document, attributes):
        Node.__init__(self, document)
        attrs = {}
        for k,v in attributes.items():
            attrs[str(k)] = v
        self.element = self._makeElement( attrs )
        return


    def content(self, content):
        raise NotImplementedError


    def notify(self, parent):
        return self.element.identify( parent )


    def onElement(self, element):
        self.element.addChild( element )
        return


    def _makeElement(self, attributes):
        raise NotImplementedError


    def _checkRequiredAttributes(self, attributes, required):
        for k in required:
            if attributes.get(k) is None:
                msg = "malformed nexml file: attribute %r is required for tag %r" %(
                    k, self.tag )
                raise SyntaxError , msg
            continue
        return

    pass


# version
__id__ = "$Id$"

# End of file 
