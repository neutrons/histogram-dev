#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from utils import getModules
import os
curdir = os.path.split( __file__ ) [0]
del os
modules = getModules(curdir)

table = {}

for m in modules:
    name = m.__name__.split( '.' )[-1]
    if '2' not in name: continue
    table[ name ] = m.__dict__[name]
    continue


def convert( ndarray, newArrayTypeName ):
    origClass = ndarray.__module__.split('.')[-1]
    
    #return the original when no conversion is necessary
    if origClass == newArrayTypeName: return ndarray
    
    name = "%s2%s" % (origClass, newArrayTypeName)
    return table[name]( ndarray )


# version
__id__ = "$Id$"

# End of file 

