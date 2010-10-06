// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef UFUNCS_H
#define UFUNCS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{

    extern char accumPlus__name__[];
    extern char accumPlus__doc__[];
    extern "C" PyObject * accumPlus(PyObject *, PyObject *args);

    // assign a value to each element of a vector
    extern char assign1__name__[];
    extern char assign1__doc__[];
    extern "C" PyObject * assign1(PyObject *, PyObject *args);

    extern char size__name__[];
    extern char size__doc__[];
    extern "C" PyObject * size(PyObject *, PyObject *);
    
    extern char sqrt__name__[];
    extern char sqrt__doc__[];
    extern "C" PyObject * sqrrt(PyObject *, PyObject *);

    extern char square__name__[];
    extern char square__doc__[];
    extern "C" PyObject * square(PyObject *, PyObject *);

    extern char voidPtr__name__[];
    extern char voidPtr__doc__[];
    extern "C" PyObject * voidPtr(PyObject *, PyObject *);
    

} // stdVector::

#endif



// version
// $Id: ufuncs.h 40 2005-02-02 01:56:28Z tim $

// End of file
