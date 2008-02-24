#include <iostream>
#include <string>
#include <Python.h>

#include "vPtr2stdvectorPtr.h"
#include "vPtr2stdvectorPtrBdgs.h"

// -------------------- vPtr2stdvectorPtrWD --------------------

char pyarray_kluge_vPtr2stdvectorPtrWD__doc__[] = 
"vPtr2stdvectorPtrWD(cptr, size, nxtypecode, desc=\"\") ==> "
"PyCObject/vector_ptr with description\n"
"\n"
"Convert a PyCObject with a void pointer of a c array to a PyCObject "
"containing a pointer of a std::vector object with a description of "
"the pointer "
"(so that it can be taken by swig stl vector)\n"
"\n"
"  Arguments:\n"
"\n"
"    - cptr: PyCObject of the pointer\n"
"    - nxtypecode: integer. nx typecode of the pointer. currently implemented types are "
"        float.......5\n"
"        double......6\n"
"        int........24\n"
"        unsigned...25\n"
"    - size: size of the c array given by the void pointer\n"
"    - desc(optional): description of the new std::vector pointer\n"
"\n"
"  Return:\n"
"\n"
"    PyCObject with a pointer to a std::vector object\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pyarray_kluge_vPtr2stdvectorPtrWD__name__[] = "vPtr2stdvectorPtrWD";

PyObject * pyarray_kluge_vPtr2stdvectorPtrWD(PyObject *, PyObject *args)
{
  // inputs:  pointer, typecode, size, desc

  // parse inputs
  PyObject *pyptr = 0;
  int size;
  int nxtypecode;
  char *desc="";

  int ok = PyArg_ParseTuple(args, "Oii|s",&pyptr, &size, &nxtypecode, &desc);
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

  bool usedefaultdesc = false;
  if ( std::string(desc).length()==0 ) {
    usedefaultdesc = true;
  }

  static char *float_swig_desc = "_p_std__vectorTfloat_t";
  static char *double_swig_desc = "_p_std__vectorTdouble_t";
  static char *int_swig_desc = "_p_std__vectorTint_t";
  static char *unsigned_swig_desc = "_p_std__vectorTunsigned_t";

  std::string errstr("pyarray_conversiont_cPtr2stdVector() ");

  switch (nxtypecode) {
  case 5:
    if (usedefaultdesc)
      desc = float_swig_desc;
    return PyCObject_FromVoidPtrAndDesc(newVector<float>(vptr, size), desc,
				deleteObjectWDesc<std::vector<float> >);
  case 6:
    if (usedefaultdesc)
      desc = double_swig_desc;
    return PyCObject_FromVoidPtrAndDesc(newVector<double>(vptr, size), desc,
				deleteObjectWDesc<std::vector<double> >);
  case 24:
    if (usedefaultdesc)
      desc = int_swig_desc;
    return PyCObject_FromVoidPtrAndDesc(newVector<int>(vptr, size), desc,
				deleteObjectWDesc<std::vector<int> >);
  case 25:
    if (usedefaultdesc)
      desc = unsigned_swig_desc;
    return PyCObject_FromVoidPtrAndDesc(newVector<unsigned>(vptr, size), desc,
				deleteObjectWDesc<std::vector<unsigned> >);
  default:
    errstr += "Unrecognized type code. Recognized type codes are\n"
      "        float.......5\n"
      "        double......6\n"
      "        int........24\n"
      "        unsigned...25\n";
    PyErr_SetString( PyExc_ValueError, errstr.c_str());
    return 0;
  }
  // never reached
  errstr += "reached \"unreachable\" code!";
  std::cerr << __FILE__ << " " << __LINE__ << ": " << errstr;
  PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
  return 0;
}


//-------------------- vPtr2stdvectorPtr --------------------
char pyarray_kluge_vPtr2stdvectorPtr__name__[] = "vPtr2stdvectorPtr";
char pyarray_kluge_vPtr2stdvectorPtr__doc__[] = 
"vPtr2stdvectorPtr( cptr, size, type) -> PyCObj/vector\n"
"Copy a C array with void pointer stored as a PyCObject to "
"a std::vector object\n"
"\n"
"  Arguments:\n"
"\n"
"    - cptr: PyCObject of the pointer\n"
"    - type: int. nx typecode of the pointer. currently implemented types are "
"        float.......5\n"
"        double......6\n"
"        int........24\n"
"        unsigned...25\n"
"    - size: size of the c array given by the void pointer\n"
"\n"
"  Return:\n"
"\n"
"    PyCObject with a pointer to a std::vector object\n"
"\n"
"  Exceptions: ValueError\n";

PyObject *pyarray_kluge_vPtr2stdvectorPtr( PyObject *, PyObject *args)
{
  // parse inputs
  PyObject *pyptr = 0;
  int size = 0, nxtypecode = 0;
  
  int ok = PyArg_ParseTuple( args, "Oii", &pyptr, &size, &nxtypecode);
  if(!ok) return 0; 
  
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

    std::string errstr("pyarray_kluge_vPtr2stdvectorPtr() ");

    switch( nxtypecode )
    {
//     case 4: // char
//         return PyCObject_FromVoidPtr( newVector<char>(vptr, size),
//                                       deleteObject<std::vector<char> >);
//         break;
    case 5: // float
        return PyCObject_FromVoidPtr( newVector<float>(vptr, size),
                                      deleteObject<std::vector<float> >);
        break;
    case 6: // double
        return PyCObject_FromVoidPtr( newVector<double>(vptr, size),
                                      deleteObject<std::vector<double> >);
        break;
//     case 21: // unsigned char
//         return PyCObject_FromVoidPtr( newVector<uchar>(vptr, size),
//                                       deleteObject<std::vector<uchar> >);
//         break;
    case 24: // int
        return PyCObject_FromVoidPtr( newVector<int>(vptr, size),
                                      deleteObject<std::vector<int> >);
        break;
    case 25: // unsigned 
        return PyCObject_FromVoidPtr( newVector<unsigned>(vptr, size),
                                      deleteObject<std::vector<unsigned> >);
        break;
    default:   // Unrecognized type
        errstr += "Unrecognized type code. Recognized type codes are\n"
            "        float.......5\n"
            "        double......6\n"
            "        int........24\n"
            "        unsigned...25\n";
        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }
    // never reached
    errstr += "reached \"unreachable\" code!";
    std::cerr << __FILE__ << " " << __LINE__ << ": " << errstr;
    PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
    return 0;
}

