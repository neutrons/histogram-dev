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


## \namespace array_kluge::stdvector__vptr
## pointer to std::vector <-- c pointer to array

import array_kluge as binding

def vPtr2stdvectorPtr( vptr, length, datatype):
    """Convert array/void ptr to std::vector instance. Data is copied.
    3 Arguments: vptr, length, type. 
Input:
      data (PyCObject w/ void ptr)
      length (integer)
      datatype (integer) 
Output: 
      (return) PyCObject of a pointer to a std::vector instance
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
    return binding.vPtr2stdvectorPtr( vptr, length, datatype )
    

def vPtr2stdvectorPtrWD( vptr, length, datatype, desc = ""):
    """Convert array/void ptr to std::vector instance. Data is copied.
    The returned PyCObject contains a description of the vector
    speciefied by argument 'desc'. If you do not supply argument
    'desc', a swig-like description of the vector type will be
    automatically used.

    >>> vPtr2stdvectorPtrWD( vptr, 10, 6, desc = "std::vector<double>" )
    >>> vPtr2stdvectorPtrWD( vptr, 10, 6 )
    
    4 Arguments: vptr, length, type, and desc
Input:
      data (PyCObject w/ void ptr)
      length (integer)
      datatype (integer)
      desc (string)
Output: 
      (return) PyCObject of a pointer to a std::vector instance
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
    return binding.vPtr2stdvectorPtrWD( vptr, length, datatype, desc )
    
