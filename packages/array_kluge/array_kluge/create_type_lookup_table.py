#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                Jiao Lin
#                        California Institute of Technology
#                        (C) 1998-2003 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## this module should be kept in consistent with lib/array_kluge.h

## \namespace array_kluge::create_type_lookup_table
## create { type name: type code } dictionary

from test_platform import SysWordLen

#----------------------------------------------------------------------
types = {'char':4, 'string':4, 'float':5, 'double':6, 'short short':20, 
         'ushort short':21, 'short':22, 'ushort':23, 'int':24,'uint':25, 
         'long':24, 'ulong':25,
         }

if SysWordLen == 32:
    pass
elif SysWordLen == 64:
    pass

# create constants AK_CHAR, ...
for n, v in types.iteritems(): exec "AK_%s = %d" % (n.upper().replace( ' ', '_' ), v)

#'u'+<type> = 'unsigned '+<type>
#added 9/24/2005.
types.update(
    {'unsigned short short': types['ushort short'],
     'unsigned short'      : types['ushort'],
     'unsigned int'        : types['uint'],
     'unsigned long'       : types['ulong'],
     'unsigned'            : types['uint'],
     }
    )


def gettypename( code ):
    for name, c in types.iteritems():
        if code == c: return name
        continue
    raise ValueError , "type code %s not found" % code



def gettypecode( name ):
    return types[name]



# version
__id__ = "$Id: __init__.py 375 2005-08-16 18:44:57Z linjiao $"

#  End of file 
