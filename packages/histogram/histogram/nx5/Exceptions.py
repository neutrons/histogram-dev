#!/usr/bin/env python
# (c) 2003 T. M. Kelley California Institute of Technology tkelley@caltech.edu

class NXError(StandardError):
    def __init__(self, msg):
        StandardError.__init__(self,msg)

class NXSearchError(NXError):
    def __init__(self, msg):
        NXError.__init__(self, msg)

#version
__id__ = "$Id: Exceptions.py 8 2005-01-20 23:09:19Z tim $"

# End of file
