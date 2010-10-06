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


## \namespace array_kluge::pylist__vptr
## python list <--> c pointer to array

import array_kluge as binding

def vptr2pylist( vptr, length, datatype):
    """3 Arguments: vptr, length, type. Convert array/void ptr to Python list.
Input:
      data (PyCObject w/ void ptr)
      length (integer)
      datatype (integer) 
Output: 
      (return) PyList
Exceptions: TypeError, ValueError, RuntimeError
Datatypes for x86:
      TYPE          CODE
      char............4
      float...........5
      double..........6
      unsigned char..21
      int............24
      unsigned int...25

Special Case:
      when datatype=4, the returned value will be a list,
      but only the first element is meaningful, and it is
      a python string of length "length". For example,
      if vptr is a pointer to a C char array
        char * a = "abcdef";
      then vptr2pylist( vptr, 3, 4 ) will return
        ["abc", <null>, <null> ]
    """
    return binding.vptr2pylist( vptr, length, datatype)

    
def pylist2vptr( pylist, datatype):
    """2 Arguments: pylist, datatype.
    Load Python list into C-array. Memory allocated for you.
Input:
      Python list (PyList)
      desired C datatype (integer) 
Output: 
      (return) (PyCObject w/ void ptr)
Exceptions: TypeError, ValueError, RuntimeError
Datatypes for x86:
      TYPE          CODE
      char............4
      float...........5
      double..........6
      unsigned char..21
      int............24
      unsigned int...25

    """
    return binding.pylist2vptr( pylist, len(pylist), datatype)
