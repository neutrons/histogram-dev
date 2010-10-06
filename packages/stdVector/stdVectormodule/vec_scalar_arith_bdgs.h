// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef VEC_SCALAR_ARITH_BDGS_H
#define VEC_SCALAR_ARITH_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

extern char pystdVector_add_scalar_vec__name__[];
extern char pystdVector_add_scalar_vec__doc__[];
extern "C"
PyObject * pystdVector_add_scalar_vec(PyObject *, PyObject *);


extern char pystdVector_mult_scalar_vec__name__[];
extern char pystdVector_mult_scalar_vec__doc__[];
extern "C"
PyObject * pystdVector_mult_scalar_vec(PyObject *, PyObject *);

#endif



// version
// $Id: vec_scalar_arith_bdgs.h 2 2004-10-01 18:15:11Z tim $

// End of file
