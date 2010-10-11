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


class AbstractNode(object):

    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes or {}
        return

    def fetch(self, *args, **kwds):
        raise NotImplementedError

    pass # end of AbstractNode


# version
__id__ = "$Id$"

# End of file 
