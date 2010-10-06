#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

class Selector( object):
    """Identify user's choice of node in hdf file"""

    def filename( self):
        """name of file to which this Selector refers"""
        return self._filename
    

    def fs( self):
        """Get reference to the nx5file"""
        return self._fs
    

    def select( self, selectionPath):
        """record path selected by user"""
        self.__validate( selectionPath)
        self._selection = selectionPath
        return


    def selection( self):
        """path selected by user"""
        return self._selection


    def __init__( self, filename, fs):
        self._filename = filename
        self._fs = fs
        self._selection = None
        return


    def __validate( self, path):
        pass
    

# version
__id__ = "$Id: Selector.py 57 2005-04-07 19:01:52Z tim $"

# End of file
