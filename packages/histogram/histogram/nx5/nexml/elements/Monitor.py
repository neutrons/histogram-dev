#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.elements")

from Group import Group

class Monitor( Group):
    """Represent a monitor in an nx5 file"""

    def identify( self, visitor):
        try:
            return visitor.onMonitor( self)
        except AttributeError, msg:
            if "onMonitor" in str( msg):
                debug.log( "nexml.Monitor.identify() exception: %s" %
                           str( msg))
                return visitor.onGroup( self)
            else:
                raise
        return


    def __init__( self, name, className = 'Monitor', nxpath = None,
                  pathstr = ''):
        """Monitor( name, className, nxpath, pathstr) -> new nexml
        Monitor node.
        Create a node to represent an Monitor group in the file.
        Inputs:
            name: name (string)
            className: default 'Monitor' (string)
            nxpath: NXpath instance for nexml search (default None)
            pathstr: this node's path, use '/' as separator
        Output:
            new Monitor group node
        Exceptions: None
        Notes: (1) You must specify a valid path!"""
        Group.__init__( self, name, className, nxpath, pathstr)
        return


# version
__id__ = "$Id: Monitor.py 94 2005-07-29 16:52:54Z tim $"

# End of file
