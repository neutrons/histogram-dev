#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                Tim Kelley
#                        California Institute of Technology
#                        (C) 1998-2003 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \namespace array_kluge::numarray__vptr
## numpy array <-- c pointer to array

import array_kluge as binding
from create_type_lookup_table import types as typecodeTable

def vPtr2numarray( vptr, length, nxtypecode, typename, copy = 1):
    """Convert array/void ptr to std::vector instance
    3 Arguments: vptr, length, nxtypecode, typename 
Input:
      data (PyCObject w/ void ptr)
      length (integer)
      nxtypecode (integer)
      typename (string)
      copy (bool)  whether or not a copy is performed
Output: 
      a Numeric array instance
Exceptions: TypeError, ValueError, RuntimeError
nx type code for x86:
      TYPE          CODE
      char............4
      float...........5
      double..........6
      unsigned char..21
      int............24
      unsigned int...25

    """
    assert typecodeTable[typename] == nxtypecode, \
           "type mismatch: nx type code = %s, typename = %s" % (nxtypecode, typename)
    
    return binding.vPtr2numarray( vptr, typename, length, copy )
    

# version
__id__ = "$Id: array_kluge_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
