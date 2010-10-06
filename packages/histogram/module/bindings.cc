// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <portinfo>
#include <Python.h>

#include "bindings.h"

#include "misc.h"          // miscellaneous methods

// the method table

struct PyMethodDef pyhistogram_methods[] = {

    // dummy entry for testing
    {pyhistogram_hello__name__, pyhistogram_hello,
     METH_VARARGS, pyhistogram_hello__doc__},

    {pyhistogram_copyright__name__, pyhistogram_copyright,
     METH_VARARGS, pyhistogram_copyright__doc__},


// Sentinel
    {0, 0}
};

// version
// $Id$

// End of file
