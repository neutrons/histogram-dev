// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef ITERATORS_H
#define ITERATORS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

extern char pystdVector_iterator__name__[];
extern char pystdVector_iterator__doc__[];
extern "C"
PyObject * pystdVector_iterator(PyObject *, PyObject *);

// get iterator to beginning of vector
extern char pystdVector_begin__name__[];
extern char pystdVector_begin__doc__[];
extern "C"
PyObject * pystdVector_begin(PyObject *, PyObject *args);

// get iterator to end of vector
extern char pystdVector_end__name__[];
extern char pystdVector_end__doc__[];
extern "C"
PyObject * pystdVector_end(PyObject *, PyObject *args);

// compare iterators
extern char pystdVector_iteratorEqual__name__[];
extern char pystdVector_iteratorEqual__doc__[];
extern "C"
PyObject * pystdVector_iteratorEqual(PyObject *, PyObject *args);

// increment iterator
extern char pystdVector_increment__name__[];
extern char pystdVector_increment__doc__[];
extern "C"
PyObject * pystdVector_increment(PyObject *, PyObject *args);


#endif



// version
// $Id: iterators.h 23 2004-11-29 22:16:57Z tim $

// End of file
