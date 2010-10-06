#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                          (C) 2007  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
debug = journal.debug('nx5.nexml')

from Group import Group

class Nexus(Group):

    def identify(self, visitor):
        try: return visitor.onNexus(self)
        except Exception, msg:
            debug.log( "%s: %s" % (msg.__class__.__name__, msg) )
            return visitor.onGroup(self)


# version
__id__ = "$Id$"

# End of file
