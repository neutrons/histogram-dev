// Timothy M. Kelley Copyright (c) 2004 All rights reserved
#ifndef VECTORCAST_BDGS_H
#define VECTORCAST_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    //  Copy one vec to another, casting.
    extern char vectorCast__name__[];
    extern char vectorCast__doc__[];
    extern "C" PyObject * vectorCast(PyObject *, PyObject *args);
} // stdVector::

#endif



// version
// $Id: vectorCast_bdgs.h 38 2005-02-01 23:48:47Z tim $

// End of file
