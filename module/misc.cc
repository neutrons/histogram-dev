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

#include "misc.h"
//#include "lib/hello.h"


// copyright

char pyhistogram_copyright__doc__[] = "";
char pyhistogram_copyright__name__[] = "copyright";

static char pyhistogram_copyright_note[] = 
    "histogram python module: Copyright (c) 1998-2005 Michael A.G. Aivazis";


PyObject * pyhistogram_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pyhistogram_copyright_note);
}
    
// hello

char pyhistogram_hello__doc__[] = "";
char pyhistogram_hello__name__[] = "hello";

PyObject * pyhistogram_hello(PyObject *, PyObject *)
{
    return Py_BuildValue("s", "Hello");
}
    
// version
// $Id$

// End of file
