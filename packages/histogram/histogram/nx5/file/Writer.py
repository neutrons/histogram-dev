#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

class Writer( object):
    """Bsae class for nexus-like writers"""

    def write( self, selector, arrayObj=None, starts=[], sizes=[],
               targetType=None):
        msg = "class %s must override write" % self.__class__.__name__
        raise NotImplementedError, msg


    def __init__( self, **kwds):

        return

# version
__id__ = "$Id: Writer.py 57 2005-04-07 19:01:52Z tim $"

# End of file
