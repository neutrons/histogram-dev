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


## \namespace array_kluge::string__charPtr
## python string <--> c pointer to c string ( char * )

import array_kluge as binding

def charPtr2string( ptr ):
    """Convert void ptr of a NULL-terminated char array to a python string
    1 Arguments: ptr
Input:
      ptr (PyCObject w/ void ptr)
Output: 
      a string
Exceptions: TypeError, ValueError, RuntimeError
    """
    return binding.charPtr2string( ptr )
    



def string2charPtrWD( s, desc = "" ):
    """Convert a python string to a PyCObject of a void ptr
    pointing at a NULL-terminated char array
    2 Arguments: s, desc
Input:
      s (string)
      desc (string)
Output: 
      a PyCObject with a pointer to a NULL-terminated char array
Exceptions: TypeError, ValueError, RuntimeError
    """
    return binding.string2charPtrWD( s, desc )
    


def string2charPtr( s ):
    """Convert a python string to a PyCObject of a void ptr
    pointing at a NULL-terminated char array
    1 Arguments: s
Input:
      s (string)
Output: 
      a PyCObject with a pointer to a NULL-terminated char array
Exceptions: TypeError, ValueError, RuntimeError
    """
    return binding.string2charPtr( s )
    


__id__ = "$Id: pyre_script_generator.py 376 2005-08-16 23:31:07Z linjiao $"

#end of file
