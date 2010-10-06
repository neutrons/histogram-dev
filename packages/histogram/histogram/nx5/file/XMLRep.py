#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

class XMLRep( object):

    def asString(self):
        return '\n'.join( self._rep)


    def __init__( self, rep):
        self._rep = rep
        return


# version
__id__ = "$Id: XMLRep.py 54 2005-04-05 20:16:30Z tim $"

# End of file
