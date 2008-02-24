// Timothy M. Kelley Copyright (c) 2005 All rights reserved
#ifndef STDVECTORMODULESLICE_BDGS_H
#define STDVECTORMODULESLICE_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    extern int slice__magicNumber__;
    extern char slice_magicNumber__name__[];
    extern char slice_magicNumber__doc__[];
    extern "C" PyObject * slice_magicNumber(PyObject *, PyObject *args);

    extern char extractSlice__name__[];
    extern char extractSlice__doc__[];
    extern "C" PyObject * extractSlice(PyObject *, PyObject *args);

    extern char slice_ctor3__name__[];
    extern char slice_ctor3__doc__[];
    extern "C" PyObject * slice_ctor3(PyObject *, PyObject *args);

    extern char slice_start__name__[];
    extern char slice_start__doc__[];
    extern "C" PyObject * slice_start(PyObject *, PyObject *args);

    extern char slice_size__name__[];
    extern char slice_size__doc__[];
    extern "C" PyObject * slice_size(PyObject *, PyObject *args);

    extern char slice_stride__name__[];
    extern char slice_stride__doc__[];
    extern "C" PyObject * slice_stride(PyObject *, PyObject *args);
} // stdVector::

#endif



// version
// $Id: slice_bdgs.h 88 2005-06-23 17:57:29Z tim $

// End of file
