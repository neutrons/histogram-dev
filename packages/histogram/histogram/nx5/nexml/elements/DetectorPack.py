#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.elements")

from Group import Group

class DetectorPack( Group):
    """Represent a detector pack in an nx5 file"""

    def identify( self, visitor):
        try:
            return visitor.onDetectorPack( self)
        except AttributeError, msg:
            if "onDetectorPack" in str(msg):
                debug.log( "nexml.DetectorPack.identify() exception: %s" %
                           str( msg))
                return visitor.onGroup( self)
            else:
                raise
        return


    def __init__( self, name, className = 'DetectorPack', nxpath = None,
                  pathstr = ''):
        """DetectorPack( name, className, nxpath, pathstr) -> new nexml
        DetectorPack node.
        Create a node to represent an DetectorPack group in the file.
        Inputs:
            name: name (string)
            className: default 'DetectorPack' (string)
            nxpath: NXpath instance for nexml search (default None)
            pathstr: this node's path, use '/' as separator
        Output:
            new DetectorPack group node
        Exceptions: None
        Notes: None"""
        Group.__init__( self, name, className, nxpath, pathstr)
        return


# version
__id__ = "$Id: DetectorPack.py 94 2005-07-29 16:52:54Z tim $"

# End of file
