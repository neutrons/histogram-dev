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


#include <string>
#include <Python.h>

#include "charPtr2stringBdgs.h"


//-------------------- string2charPtrWD --------------------

char pyarray_kluge_string2charPtrWD__doc__[] = 
"Convert a string to a PyCObject with a void pointer to a NULL-terminated "
"c string. a copy is made so that the original string is intact. "
"a description of the pointer can be attached to the returned PyCObject. "
"\n"
"  Arguments:\n"
"\n"
"    - string: the input string\n"
"    - desc: default=\"_p_char\". description of the pointer \n"
"\n"
"  Return:\n" 
"\n"
"    PyCObject of a void pointer to a copy of original string\n"
"\n"
"  Exceptions:\n"
"\n"
"    RuntimeError"
;
char pyarray_kluge_string2charPtrWD__name__[] = "string2charPtrWD";

static void deleteCharArrWD(void *ptr, void *desc)
{
  //std::cout << "deleteCharArr ";
  char *charptr = (char *)ptr;
  //std::cout << ptr << std::endl;
  delete [] charptr;
}

PyObject * pyarray_kluge_string2charPtrWD(PyObject *, PyObject *args)
{
  //std::cout << "pyarray_kluge_string2charPtrWD: ";

  char *str;
  char *desc="_p_char";

  int ok = PyArg_ParseTuple(args, "s|s", &str,&desc);
  if(!ok) return NULL;
  char *copy=NULL;
  std::string temp(str);
  copy = new char [temp.length()+1];
  if (copy==NULL) {
    std::string err("pyarray_kluge_string2charPtrWD()"
		    "could not allocate"
		    " memory for a new copy of the input string");
    PyErr_SetString(PyExc_RuntimeError, err.c_str());
    return NULL;
  }
  strcpy(copy, str);
  //std::cout << "make a copy of string "
  //	    << str
  //	    << " at " 
  //	    << (void *)copy 
  //	    << std::endl;
  return PyCObject_FromVoidPtrAndDesc( copy, desc, deleteCharArrWD );
}
  

//-------------------- string2charPtr --------------------

char pyarray_kluge_string2charPtr__doc__[] = 
"Convert a string to a PyCObject with a void pointer to a NULL-terminated "
"c string. a copy is made so that the original string is intact. "
"\n"
"  Arguments:\n"
"\n"
"    - string: the input string\n"
"\n"
"  Return:\n" 
"\n"
"    PyCObject of a void pointer to a copy of original string\n"
"\n"
"  Exceptions:\n"
"\n"
"    RuntimeError"
;
char pyarray_kluge_string2charPtr__name__[] = "string2charPtr";

static void deleteCharArr(void *ptr)
{
  //std::cout << "deleteCharArr ";
  char *charptr = (char *)ptr;
  //std::cout << ptr << std::endl;
  delete [] charptr;
}

PyObject * pyarray_kluge_string2charPtr(PyObject *, PyObject *args)
{
  //std::cout << "pyarray_kluge_string2charPtr: ";

  char *str;

  int ok = PyArg_ParseTuple(args, "s", &str);
  if(!ok) return NULL;
  char *copy=NULL;
  std::string temp(str);
  copy = new char [temp.length()+1];
  if (copy==NULL) {
    std::string err("pyarray_kluge_string2charPtr() "
		    "could not allocate"
		    " memory for a new copy of the input string");
    PyErr_SetString(PyExc_RuntimeError, err.c_str());
    return NULL;
  }
  strcpy(copy, str);
  //std::cout << "make a copy of string "
  //	    << str
  //	    << " at " 
  //	    << (void *)copy 
  //	    << std::endl;
  return PyCObject_FromVoidPtr( copy, deleteCharArr );
}
  

// -------------------- charPtr2string --------------------

char pyarray_kluge_charPtr2string__doc__[] = 
"Convert a PyCObject with a void pointer to a NULL-terminated string "
"to a python string\n"
"\n"
"  Arguments:\n"
"\n"
"    - charptr: PyCObject of the pointer\n"
"\n"
"  Return:\n"
"\n"
"    the string\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pyarray_kluge_charPtr2string__name__[] = "charPtr2string";

PyObject * pyarray_kluge_charPtr2string(PyObject *, PyObject *args)
{
  //std::cout << "pyarray_kluge_charPtr2string" << std::endl;

  PyObject *object;
  int ok = PyArg_ParseTuple(args, "O", &object);
  if(!ok) return NULL;
  if(!PyCObject_Check(object)) {
    std::string err("Input must be a PyCObject of a pointer to a "
      "NULL-terminated c string");
    PyErr_SetString(PyExc_ValueError, err.c_str());
    return NULL;
  }
  void *temp;
  temp = PyCObject_AsVoidPtr(object);
  if (!temp) {
    PyErr_SetString(PyExc_RuntimeError, "void pointer is NULL. "
		    "conversion cannot continue");
    return NULL;
  }
  char *str = static_cast<char *>(temp);
  return PyString_FromString(str);
}

    


// version
// $Id: misc.cc 375 2005-08-16 18:44:57Z linjiao $

// End of file
