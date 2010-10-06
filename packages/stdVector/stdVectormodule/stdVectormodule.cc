// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               T. M. Kelley
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <portinfo>

#include <Python.h>

#include "exceptions.h"
#include "bindings.h"
//#include "numarray/libnumarray.h"

char pystdVector_module__doc__[] = "";

// Initialization function for the module (*must* be called initstdVector)
extern "C"
void
initstdVector()
{
    // create the module and add the functions
    PyObject * m = Py_InitModule4(
        "stdVector", pystdVector_methods,
        pystdVector_module__doc__, 0, PYTHON_API_VERSION);

    // get its dictionary
    PyObject * d = PyModule_GetDict(m);

    // check for errors
    if (PyErr_Occurred()) {
        Py_FatalError("can't initialize module stdVector");
    }

    // install the module exceptions
    pystdVector_runtimeError = PyErr_NewException("stdVector.runtime", 0, 0);
    PyDict_SetItemString(d, "RuntimeException", pystdVector_runtimeError);

    // import numarray function pointer table 
    // (writing a library like everyone else is hard, let's go shopping!)
    // import_libnumarray();

    return;
}

// version
// $Id: stdVectormodule.cc 124 2006-08-06 17:59:20Z linjiao $

// End of file
