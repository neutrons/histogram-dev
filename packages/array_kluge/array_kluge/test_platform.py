#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                Jiao Lin
#                        California Institute of Technology
#                        (C) 2006 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

## \namespace array_kluge::test_platform
## check the platform we are running on.


#first determine what kind of machine we are using: 32bit or 64bit?

import os

#
#assume we are mostly dealing with 32 bit machine
#this surely should be changed when the computing techniques are evolving...
SysWordLen = 32

#
#only one case of 64 bit machine is taken into account for now...
try:
    if 'x86_64' in os.uname(): SysWordLen = 64
except AttributeError, msg:
    print "AttributeError raised: %s" % msg
    print "That means we don't have os.uname method in this platform"
    print "We are going to assume that this is a windows machine,"
    print "and it is 32-bit."
    SysWordLen = 32
    pass


# version
__id__ = "$Id: __init__.py 375 2005-08-16 18:44:57Z linjiao $"

#  End of file 
