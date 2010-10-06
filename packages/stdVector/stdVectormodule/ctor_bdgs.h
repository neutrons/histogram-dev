// Timothy M. Kelley Copyright (c) 2005 All rights reserved
#ifndef CTOR_BDGS_H
#define CTOR_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    extern char stdVector_ctor__name__[];
    extern char stdVector_ctor__doc__[];
    extern "C"
    PyObject * stdVector_ctor(PyObject *, PyObject *);

    extern char stdVector_copy_ctor1__name__[];
    extern char stdVector_copy_ctor1__doc__[];
    extern "C"
    PyObject * stdVector_copy_ctor1(PyObject *, PyObject *);

    extern char stdVector_copy__name__[];
    extern char stdVector_copy__doc__[];
    extern "C"
    PyObject * stdVector_copy(PyObject *, PyObject *);

} // stdVector

#endif



// version
// $Id: ctor_bdgs.h 97 2005-07-27 01:54:40Z tim $

// End of file
