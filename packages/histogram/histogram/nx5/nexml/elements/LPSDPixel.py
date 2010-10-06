#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.elements")

from Group import Group

class LPSDPixel( Group):
    """Represent an LPSD pixel in an nx5 file"""

    def identify( self, visitor):
        try:
            return visitor.onLPSDPixel( self)
        except AttributeError, msg:
            if "onLPSDPixel" in str( msg):
                debug.log( "nexml.LPSDPixel.identify() exception: %s" %
                           str( msg))
                return visitor.onGroup( self)
            else:
                raise
        return


    def __init__( self, name, className = 'LPSDPixel', nxpath = None,
                  pathstr = ''):
        """LPSDPixel( name, className, nxpath, pathstr) -> new nexml
        LPSDPixel node.
        Create a node to represent an LPSDPixel group in the file.
        Inputs:
            name: name (string)
            className: default 'LPSDPixel' (string)
            nxpath: NXpath instance for nexml search (default None)
            pathstr: this node's path, use '/' as separator
        Output:
            new LPSDPixel group node
        Exceptions: None
        Notes: (1) You must specify a valid path!"""
        Group.__init__( self, name, className, nxpath, pathstr)
        return
    

# version
__id__ = "$Id: LPSDPixel.py 94 2005-07-29 16:52:54Z tim $"

# End of file
