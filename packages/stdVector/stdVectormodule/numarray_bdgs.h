// Timothy M. Kelley Copyright (c) 2005 All rights reserved
#ifndef NUMARRAY_BDGS_H
#define NUMARRAY_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    extern char asNumarray__name__[];
    extern char asNumarray__doc__[];
    extern "C" PyObject * asNumarray(PyObject *, PyObject *args);
} // stdVector::

#endif


// version
// $Id: numarray_bdgs.h 53 2005-04-06 19:19:40Z tim $

// End of file
