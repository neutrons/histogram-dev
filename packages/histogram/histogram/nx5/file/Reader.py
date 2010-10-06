#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

class Reader( object):
    """Base class for Nexus file readers"""
    
    def read( self, selector, array=None, starts=[], sizes=[],
              targetType=None):
        msg = "%s must override read" % self.__class__.__name__
        raise NotImplementedError, msg


    def __init__( self):
        return
        

# version
__id__ = "$Id: Reader.py 57 2005-04-07 19:01:52Z tim $"

# End of file
