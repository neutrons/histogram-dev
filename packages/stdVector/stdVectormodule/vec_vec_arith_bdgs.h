// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef VEC_VEC_ARITH_BDGS_H
#define VEC_VEC_ARITH_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    extern char vectorPlusEquals__name__[];
    extern char vectorPlusEquals__doc__[];
    extern "C"
    PyObject * vectorPlusEquals(PyObject *, PyObject *);


    extern char vectorMinusEquals__name__[];
    extern char vectorMinusEquals__doc__[];
    extern "C"
    PyObject * vectorMinusEquals(PyObject *, PyObject *);


    extern char vectorTimesEquals__name__[];
    extern char vectorTimesEquals__doc__[];
    extern "C"
    PyObject * vectorTimesEquals(PyObject *, PyObject *);


    extern char vectorDivideEquals__name__[];
    extern char vectorDivideEquals__doc__[];
    extern "C"
    PyObject * vectorDivideEquals(PyObject *, PyObject *);

    extern char vectorPlus__name__[];
    extern char vectorPlus__doc__[];
    extern "C"
    PyObject * vectorPlus(PyObject *, PyObject *);


    extern char vectorMinus__name__[];
    extern char vectorMinus__doc__[];
    extern "C"
    PyObject * vectorMinus(PyObject *, PyObject *);


    extern char vectorTimes__name__[];
    extern char vectorTimes__doc__[];
    extern "C"
    PyObject * vectorTimes(PyObject *, PyObject *);


    extern char vectorDivide__name__[];
    extern char vectorDivide__doc__[];
    extern "C"
    PyObject * vectorDivide(PyObject *, PyObject *);

} // stdVector::

#endif



// version
// $Id: vec_vec_arith_bdgs.h 74 2005-05-17 23:38:47Z tim $

// End of file
