#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug( "nx5.elements")

from Group import Group

class Instrument( Group):
    """Represent an instrument group in an nx5 file"""

    def identify( self, visitor):
        try:
            return visitor.onInstrument( self)
        except AttributeError, msg:
            debug.log("nexml.Instrument.identify() exception: %s" % str( msg))
            if 'onInstrument' in str(msg):
                return visitor.onGroup( self)
            else:
                raise
        return


    def __init__( self, name, className = 'Instrument', nxpath = None,
                  pathstr = ''):
        """Instrument( name, className, nxpath, pathstr) -> new nexml
        Instrument node.
        Create a node to represent an Instrument group in the file.
        Inputs:
            name: name (string)
            className: default 'Instrument' (string)
            nxpath: NXpath instance for nexml search (default None)
            pathstr: this node's path, use '/' as separator
        Output:
            new Instrument group node
        Exceptions: None
        Notes: None"""
        Group.__init__( self, name, className, nxpath, pathstr)
        return
    

# version
__id__ = "$Id: Instrument.py 87 2005-07-16 16:00:24Z tim $"

# End of file
