#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

class FileFactory( object):
    """Make files for the people"""

    def __call__( self, filename, mode):

        # 1 initialize fs

        # 2 Stat graph rep in file

        # 2a graph found: unpickle graph, cache

        # 2b graph not found: Stat XML rep

        # 2b 1 XML rep found: read/cache XML, construct graph from XML, cache
        # graph

        # 2b 2 XML rep not found: construct graph from fs, construct XML rep
        # from graph, cache both

        # 3 create File object, initialize with fs, graph, and XML rep

        raise NotImplementedError, "Coming soon..."
        

    def __init__( self):
        return

# version
__id__ = "$Id: FileFactory.py 29 2005-03-26 00:57:42Z tim $"

# End of file
