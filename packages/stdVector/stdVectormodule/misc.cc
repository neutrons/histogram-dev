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

#include <portinfo>
#include <Python.h>

#include "misc.h"
#include "stdVector/hello.h"
#include <iostream>
#include <vector>
#include "stdVector/utils.h"
#include "journal/debug.h"

// copyright

char pystdVector_copyright__doc__[] = "";
char pystdVector_copyright__name__[] = "copyright";

static char pystdVector_copyright_note[] = 
    "stdVector python module: Copyright (c) 2004 T. M. Kelley";


PyObject * pystdVector_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pystdVector_copyright_note);
}
        
// PyCObject for test
char pystdVector_testcobj__name__[] = "testcobj";
char pystdVector_testcobj__doc__[] = 
"Get a PyCObject for test purposes\n";

namespace
{
    void deleteTest( void *ptr)
    {
        char *ptest = static_cast<char *>(ptr);
        delete ptest;
        return;
    }
}

PyObject * pystdVector_testcobj(PyObject *, PyObject *)
{
    char *pchar = new char;
    return PyCObject_FromVoidPtr( pchar, deleteTest);
}

// print C array
char pystdVector_printCArray__name__[] = "printCArray";
char pystdVector_printCArray__doc__[] = 
"printCArray( PyCObj, length) -> print length doubles to stdout starting at\n"
"location pointed to by PyCObj. Mainly useful for testing.\n"
"Input:\n"
"    PyCObj (PyCObject with pointer to array of doubles)\n"
"Output:\n"
"    None\n"
"Exceptions: ValueError";


PyObject * pystdVector_printCArray(PyObject *, PyObject *args)
{
    PyObject *pyobj = 0;
    int length = 0;
    int ok = PyArg_ParseTuple( args, "Oi", &pyobj, &length);
    if (!ok) return 0;

    std::string errstr("pystdVector_printCArray() ");

    if (length < 0)
    {
        errstr += "negative index!";
        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }

    double *bob = static_cast<double *>( PyCObject_AsVoidPtr( pyobj));

    std::cout << "Contents of array: " << std::endl;

    for( int i=0; i<length; ++i)
        std::cout << bob[i] << std::endl;

    std::cout << "End of array" << std::endl;

    Py_INCREF( Py_None);
    return Py_None;
}


// print C array
char pystdVector_printIterator__name__[] = "printIterator";
char pystdVector_printIterator__doc__[] = 
"printIterator( PyCObj, dtype, length) -> print length numbers to stdout starting at\n"
"location pointed to by PyCObj. Mainly useful for testing.\n"
"Input:\n"
"    PyCObj (PyCObject with pointer to std::vector<type>::iterator)\n"
"    dtype (int template type"
"Output:\n"
"    None\n"
"Exceptions: ValueError";

namespace
{
    template <typename Iterator>
    void _printIt( PyObject *pyit, int dtype, size_t num)
    {
        Iterator *pit = 
            ARCSStdVector::unwrapIterator<Iterator>( pyit, dtype);
        Iterator temp( *pit);
        for( size_t i=0; i<num; ++i) 
        {
            std::cout << *temp++ << " ";
        }
        std::cout << std::endl;
        return;
    }
}


PyObject * pystdVector_printIterator(PyObject *, PyObject *args)
{
    PyObject *pyit = 0;
    int dtype = 0;
    int length = 0;
    int ok = PyArg_ParseTuple( args, "Oii", &pyit, &dtype, &length);
    if (!ok) return 0;

    std::string errstr("pystdVector_printIterator() ");

    if (length < 0)
    {
        errstr += "negative length!";
        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }

    switch( dtype)
    {
    case 5:   // float
        _printIt<std::vector<float>::iterator>( pyit, dtype, length);
        break;
    case 6:   // double
        _printIt<std::vector<double>::iterator>( pyit, dtype, length);
        break;
    case 24:  // int
        _printIt<std::vector<int>::iterator>( pyit, dtype, length);
 		break;
    case 25:  // unsigned int 
        _printIt<std::vector<unsigned>::iterator>( pyit, dtype, length);
 		break;
    default:
        errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
            "          float.......5\n"
            "          double......6\n"
            "          int........24\n"
            "          unsigned...25\n";
//         debug << at(__HERE__) << errstr;
//         debug.newline();
//         debug << "Datatype = " << dtype << endl;
        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }
    Py_INCREF( Py_None);
    return Py_None;
} // printIterator


// version
// $Id: misc.cc 85 2005-06-17 16:54:43Z tim $

// End of file
