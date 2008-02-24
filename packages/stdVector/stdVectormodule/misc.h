// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               T. M. Kelley
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#if !defined(pystdVector_misc_h)
#define pystdVector_misc_h

// copyright
extern char pystdVector_copyright__name__[];
extern char pystdVector_copyright__doc__[];
extern "C"
PyObject * pystdVector_copyright(PyObject *, PyObject *);

// PyCObject for test
extern char pystdVector_testcobj__name__[];
extern char pystdVector_testcobj__doc__[];
extern "C"
PyObject * pystdVector_testcobj(PyObject *, PyObject *);

// print C array
extern char pystdVector_printCArray__name__[];
extern char pystdVector_printCArray__doc__[];
extern "C"
PyObject * pystdVector_printCArray(PyObject *, PyObject *);

// print Iterator
extern char pystdVector_printIterator__name__[];
extern char pystdVector_printIterator__doc__[];
extern "C"
PyObject * pystdVector_printIterator(PyObject *, PyObject *);

#endif

// version
// $Id: misc.h 23 2004-11-29 22:16:57Z tim $

// End of file
