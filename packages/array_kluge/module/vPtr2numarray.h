// -*- C++ -*-
// Copyright (C) 2004 Jiao Lin California Institute of Technology

#ifndef H_VPTR2NUMARRAY
#define H_VPTR2NUMARRAY

#include "utils.h"

#include <Python.h>
#define NO_IMPORT
#include <numpy/arrayobject.h>


namespace 
{
  /// convert or copy a c array to a num array
  /// this function is not robust because it does not have a way to
  /// check consistency of given typename and typecode
  template <typename T>
  PyObject *vPtr2numArr1D( void *vptr, size_t size, bool copy,
			     int numarr_typecode);
} 

namespace 
{
  template <typename T>
  PyObject *vPtr2numArr1D( void *vptr, size_t size, bool copy,
			     int numarr_typecode)
  {
    T *cptr = static_cast<T *>(vptr);
    if (cptr == NULL) {
      PyErr_SetString(PyExc_ValueError, "invalid void pointer");
      return NULL;
    }
    
    PyArrayObject *num_arr_obj;
    int dimensions[1];
    dimensions[0] = size;
    
    if (copy) {
      
      // make a new array object
      num_arr_obj = (PyArrayObject *)PyArray_FromDims(1,dimensions,
						      numarr_typecode);
      if (!num_arr_obj) {
	std::string err;
	err = "cPtr2numArr1D() could not construct a new numpy array"
	  "with dimension [";
	err += dimensions[0]+"]";
	PyErr_SetString(PyExc_RuntimeError, err.c_str());
	return NULL;
      }
      
      // copy the data over
      T *newptr = (T *)num_arr_obj->data;
      size_t idx;
      for (idx=0; idx<size; idx++) {
	newptr[idx] = cptr[idx];
      }

    } else {

    // directly take the data pointer. this only works for a pointer 
    // that will not be freed until very late
      num_arr_obj = (PyArrayObject *)
	PyArray_FromDimsAndData(1, dimensions, numarr_typecode,
				(char *)cptr);
      
    }

    //  std::cout << "done." << std::endl;
    return PyArray_Return(num_arr_obj);
  }

} // anonymous namespace a slight improvement over static


#endif // H_VPTR2NUMARRAY


// version 
// $Id: array_conversion.h 375 2005-08-16 18:44:57Z linjiao $

// End of file 

