// Timothy M. Kelley Copyright (c) 2005 All rights reserved
#ifndef REDUCESUM_BDGS_H
#define REDUCESUM_BDGS_H

#include "Python.h"

namespace stdVector
{
    extern char ReduceSum2d__name__[];
    extern char ReduceSum2d__doc__[];
    extern "C"
    PyObject * ReduceSum2d(PyObject *, PyObject *args);
    
    extern char ReduceSum3d__name__[];
    extern char ReduceSum3d__doc__[];
    extern "C"
    PyObject * ReduceSum3d(PyObject *, PyObject *args);
} // stdVector::

#endif


// version
// $Id: reduceSum_bdgs.h 102 2005-07-31 21:39:44Z tim $

// End of file
