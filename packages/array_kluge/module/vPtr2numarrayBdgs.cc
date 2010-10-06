// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Jiao Lin
//                        California Institute of Technology
//                        (C) 2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#include <iostream>
#include <string>
#include <sstream>

#include <Python.h>

//#define NO_IMPORT_ARRAY
#include <numpy/arrayobject.h>

#include "vPtr2numarray.h"
#include "vPtr2numarrayBdgs.h"



typedef unsigned char ubyte;
typedef signed char sbyte;



// -------------------- vPtr2numarray --------------------

char pyarray_kluge_vPtr2numarray__doc__[] = 
"Convert a PyCObject with a pointer of a c array to a numpy array\n"
"\n"
"  Arguments:\n"
"\n"
"    - cptr: PyCObject of the pointer\n"
"\n"
"    - numarr_typecode: int. type of the pointer. currently implemented types are "
"char, unsigned char, signed char, int, long, float, double, PyCObject *\n"
"\n"
"    - size: size of the c array given by the void pointer\n"
"\n"
"    - copy: copy=1, a copy is made. copy=0, the original data will be used"
"\n"
"\n"
"  Return:\n"
"\n"
"    numpy array\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pyarray_kluge_vPtr2numarray__name__[] = "vPtr2numarray";

int numArrTypeCode( const char *type );

void _import_numpy()
{
  import_array();
}

PyObject * pyarray_kluge_vPtr2numarray(PyObject *, PyObject *args)
{
 _import_numpy();

  // inputs:  pointer, type, size, copy

  // parse inputs
  PyObject *pyptr = 0;
  int size;
  int numarr_typecode;
  char *type;
  int copy=1;
  int ok = PyArg_ParseTuple(args, "Osi|i",&pyptr, &type,
			    &size, &copy);
  if(!ok) return NULL;

  if (!PyCObject_Check(pyptr)) {
    PyErr_SetString(PyExc_ValueError, "argument 1 must be PyCObject of "
      "a void pointer of a c array");
    return NULL;
  }

  void *vptr = PyCObject_AsVoidPtr(pyptr);
  if (!vptr) {
    PyErr_SetString(PyExc_RuntimeError, "void pointer is NULL. "
      "conversion cannot continue");
    return NULL;
  }

  PyObject *res;

  try {
    numarr_typecode = numArrTypeCode( type );
  } 
  catch (const char *msg) {
    std::stringstream err;
    err << msg << std::endl;
    err << "This array_kluge type has not been implemented yet: ";
    err << type;
    PyErr_SetString(PyExc_NotImplementedError, err.str().c_str());
    return NULL;
  }

  switch (numarr_typecode) {
    
  case PyArray_CHAR: 
    res = vPtr2numArr1D<char>( vptr, size_t( size), bool(copy), 
				 PyArray_CHAR);
    break;

  case PyArray_UBYTE: 
    res = vPtr2numArr1D<ubyte>( vptr, size_t( size), bool(copy), 
			    PyArray_UBYTE);
    break;

  //case PyArray_SBYTE: 
  // res = vPtr2numArr1D<sbyte>( vptr, size_t( size), bool(copy), 
//			    PyArray_SBYTE);
 //  break;

  case PyArray_INT: 
    res = vPtr2numArr1D<int>( vptr, size_t( size), bool(copy), 
			    PyArray_INT);
    break;

  case PyArray_UINT: 
    res = vPtr2numArr1D<unsigned int>( vptr, size_t( size), bool(copy), 
			    PyArray_UINT);
    break;

  case PyArray_LONG:
    res = vPtr2numArr1D<long>( vptr, size_t( size), bool(copy), 
			    PyArray_LONG);
    break;

  case PyArray_ULONG:
    res = vPtr2numArr1D<unsigned long>( vptr, size_t( size), bool(copy), 
			    PyArray_ULONG);
    break;

  case PyArray_FLOAT: 
    res = vPtr2numArr1D<float>( vptr, size_t( size), bool(copy), 
			    PyArray_FLOAT);
    break;

  case PyArray_DOUBLE: 
    res = vPtr2numArr1D<double>( vptr, size_t( size), bool(copy), 
			    PyArray_DOUBLE);
    break;

  case PyArray_OBJECT: 
    res = vPtr2numArr1D<PyObject *>( vptr, size_t( size), bool(copy), 
			    PyArray_OBJECT);
    break;

  default:
    std::stringstream err;
    err << "This array_kluge type is not implemented yet: ";
    err << numarr_typecode;
    PyErr_SetString(PyExc_NotImplementedError, err.str().c_str());
    res = NULL;
  }

  return res;
}



int numArrTypeCode( const char *type )
{
  using std::string;
  string stype = type;
  if (stype == string("char")) 
    return PyArray_CHAR;
  else if (stype == string("unsigned char")) 
    return PyArray_UBYTE;
  //else if (stype == string("signed char")) 
  //  return PyArray_SBYTE;
  else if (stype == string("unsigned int") || stype == string("unsigned") ) {
    
    switch( sizeof( unsigned))
      {
      case 4: return PyArray_UINT;
      case 8: return PyArray_UINT;
      default:
	std::cerr << "unexpected integer size" << sizeof(unsigned);
	throw "numArrTypeCode: unexpected integer size";
      }
  }
  else if (stype == string("int")) {
    
    switch( sizeof( int))
      {
      case 4: return PyArray_INT;
      case 8: return PyArray_INT;
      default:
	std::cerr << "unexpected integer size" << sizeof(int);
	throw "numArrTypeCode: unexpected integer size";
      }
  }
  else if (stype == string("long")) 
    return PyArray_LONG;
  else if (stype == string("ulong")) 
    return PyArray_ULONG;
  else if (stype == string("float")) 
    return PyArray_FLOAT;
  else if (stype == string("double")) 
    return PyArray_DOUBLE;
  else if (stype == string("PyObject *")) 
    return PyArray_OBJECT;
  else {
    std::cerr << "numArrTypeCode: Unkown data type " << type << std::endl;
    throw "numArrTypeCode: Unkown data type";
  }
}


// version
// $Id: misc.cc 375 2005-08-16 18:44:57Z linjiao $

// End of file
