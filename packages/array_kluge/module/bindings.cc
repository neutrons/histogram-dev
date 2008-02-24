// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2003 All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

//#include <portinfo>
#include <Python.h>

#include "bindings.h"

#include "misc.h"          // miscellaneous methods
#include "vPtr2stdvectorPtrBdgs.h"
#include "vPtr2numarrayBdgs.h"
#include "charPtr2stringBdgs.h"

// the method table

struct PyMethodDef pyarray_kluge_methods[] = {

    // dummy entry for testing
    {pyarray_kluge_copyright__name__, pyarray_kluge_copyright,
     METH_VARARGS, pyarray_kluge_copyright__doc__},
//Don't try this at home!!!
    {pyNeXus_vptr2pylist__name__ , pyNeXus_vptr2pylist, METH_VARARGS,
                                                pyNeXus_vptr2pylist__doc__},
    {pyNeXus_pylist2vptr__name__ , pyNeXus_pylist2vptr, METH_VARARGS,
                                                pyNeXus_pylist2vptr__doc__},
    {pyNeXus_pylistin2vptr__name__ , pyNeXus_pylistin2vptr, METH_VARARGS,
                                                pyNeXus_pylistin2vptr__doc__},

    //
    {pyarray_kluge_vPtr2stdvectorPtrWD__name__, pyarray_kluge_vPtr2stdvectorPtrWD,
     METH_VARARGS, pyarray_kluge_vPtr2stdvectorPtrWD__doc__},
    {pyarray_kluge_vPtr2stdvectorPtr__name__, pyarray_kluge_vPtr2stdvectorPtr,
     METH_VARARGS, pyarray_kluge_vPtr2stdvectorPtr__doc__},

    {pyarray_kluge_vPtr2numarray__name__, pyarray_kluge_vPtr2numarray,
     METH_VARARGS, pyarray_kluge_vPtr2numarray__doc__},

    {pyarray_kluge_string2charPtr__name__, 
     pyarray_kluge_string2charPtr,
     METH_VARARGS, pyarray_kluge_string2charPtr__doc__},

    {pyarray_kluge_string2charPtrWD__name__, 
     pyarray_kluge_string2charPtrWD,
     METH_VARARGS, pyarray_kluge_string2charPtrWD__doc__},

    {pyarray_kluge_charPtr2string__name__, 
     pyarray_kluge_charPtr2string,
     METH_VARARGS, pyarray_kluge_charPtr2string__doc__},


// Sentinel
    {0, 0}
};

// version
// $Id: bindings.cc 26 2006-04-17 03:41:54Z jiao $

// End of file
