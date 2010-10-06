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

#if !defined(pyarray_kluge_misc_h)
#define pyarray_kluge_misc_h

// copyright
extern char pyarray_kluge_copyright__name__[];
extern char pyarray_kluge_copyright__doc__[];
extern "C"
PyObject * pyarray_kluge_copyright(PyObject *, PyObject *);

// void ptr to Python list:
extern char pyNeXus_vptr2pylist__name__[];
extern char pyNeXus_vptr2pylist__doc__[];
extern "C" PyObject * pyNeXus_vptr2pylist(PyObject *, PyObject *);

// Python list to void ptr
extern char pyNeXus_pylist2vptr__name__[];
extern char pyNeXus_pylist2vptr__doc__[];
extern "C" PyObject * pyNeXus_pylist2vptr(PyObject *, PyObject *args);

// Python list to existing void ptr
extern char pyNeXus_pylistin2vptr__name__[];
extern char pyNeXus_pylistin2vptr__doc__[];
extern "C" PyObject * pyNeXus_pylistin2vptr(PyObject *, PyObject *args);

#endif

// version
// $Id: misc.h 11 2004-08-05 18:49:40Z tim $

// End of file
