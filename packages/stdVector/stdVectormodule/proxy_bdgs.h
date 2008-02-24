// -*- C++ -*-
//
// Jiao Lin
// for connecting boost python based modules to Tim's stdVector

#ifndef PROXY_BDGS_H
#define PROXY_BDGS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace stdVector
{
    extern char stdVector_proxy__name__[];
    extern char stdVector_proxy__doc__[];
    extern "C"
    PyObject * stdVector_proxy(PyObject *, PyObject *);
} // stdVector

#endif



// version
// $Id: proxy_bdgs.h 141 2005-07-08 22:32:11Z linjiao $

// End of file
