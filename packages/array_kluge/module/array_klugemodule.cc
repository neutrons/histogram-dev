// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2003 All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

//#include <portinfo>
#include <iostream>

#include <Python.h>
#define NO_IMPORT
#include <numpy/arrayobject.h>

#include "exceptions.h"
#include "bindings.h"


void **PyArray_API;


char pyarray_kluge_module__doc__[] = "";

// Initialization function for the module (*must* be called initarray_kluge)
extern "C"
#ifdef WIN32
__declspec(dllexport)
#endif
void
initarray_kluge()
{
    // create the module and add the functions
    PyObject * m = Py_InitModule4(
        "array_kluge", pyarray_kluge_methods,
        pyarray_kluge_module__doc__, 0, PYTHON_API_VERSION);

    // because of bindings to Numeric, we need to import it first
    //std::cout << "import Numeric" << std::endl;
    //import_array();

    // get its dictionary
    PyObject * d = PyModule_GetDict(m);

    // check for errors
    if (PyErr_Occurred()) {
        Py_FatalError("can't initialize module array_kluge");
    }

    // install the module exceptions
    pyarray_kluge_runtimeError = PyErr_NewException("array_kluge.runtime", 0, 0);
    PyDict_SetItemString(d, "RuntimeException", pyarray_kluge_runtimeError);

    return;
}

// version
// $Id: array_klugemodule.cc 33 2006-08-06 17:42:51Z linjiao $

// End of file
