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

class Branch:

    "Branch node of object tree"


    def __init__(self, name):
        self.name = name
        self.leaves = []
        return


    def addLeaf(self, leaf):
        self.leaves.append( leaf )
        return


    def identify(self, visitor):
        return visitor.onBranch(self)

    
# version
__id__ = "$Id$"

# End of file 
