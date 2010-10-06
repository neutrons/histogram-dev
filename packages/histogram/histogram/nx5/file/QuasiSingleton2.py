#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved


class QuasiSingleton( object):
    """Base class that ensures no more than one interface to a given file"""

    instances = {}

    def __call__( self, filename, mode, *args, **kwds):
        """get nx5 file interface"""

        # use only filename as key: want to ensure others can't get a separate
        # interface
        key = filename 
        if key in self.instances:
            theFile = self.instances[ key]
        else:
            theFile = self.call( filename, mode, *args, **kwds)
            self.instances[key] = theFile
        return theFile


    # subclasses should provide file creation logic here
    def call( self, filename, mode, *args, **kwds):
        msg = "NIY: %s must override call" % self.__class__.__name__
        raise NotImplementedError, msg


    def __init__( self, *args, **kwds):
        return
    

# version
__id__ = "$Id: QuasiSingleton2.py 81 2005-06-22 22:43:53Z tim $"

# End of file
