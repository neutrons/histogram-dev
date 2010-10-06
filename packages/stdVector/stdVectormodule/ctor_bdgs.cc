// Timothy M. Kelley Copyright (c) 2005 All rights reserved

#include "ctor_bdgs.h"
#include "stdVector/utils.h"
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include "journal/debug.h"
#include <stdexcept>


namespace 
{
    char journalname [] = "stdVector_bdgs";
    using journal::at;
    using journal::endl;

    template <typename T>
    PyObject * _callVectorCtor( int dtype, size_t length, T initVal, 
                                std::stringstream & errstr)
    {
        journal::debug_t debug( journalname);

        debug << at(__HERE__) << "datatype: " << dtype << ", length "
              << length << ", initVal " << initVal << endl;
        std::vector<T> *pvec = 0;
        try
        {
            pvec = new std::vector<T>( length, initVal);
        }
        catch (std::bad_alloc &ba)
        {
            debug << at(__HERE__) << "bad_alloc" << endl;
            errstr << "in _callVectorCtor<>(): ";
            errstr << ba.what();
            PyErr_SetString( PyExc_RuntimeError, errstr.str().c_str());
            return 0;
        }
        PyObject *retval = ARCSStdVector::wrapVector<T>( pvec, dtype);
        if(retval == 0)
        {
            errstr << "unable to wrap";
            debug << errstr.str();
            return 0;   // exception context set in wrapVector
        }
        debug << at(__HERE__) << "vector at " << pvec << " with buffer at " 
              << &(*pvec)[0]
              << "; done." << endl;        

        return retval;
    }
} // anonymous::

namespace stdVector
{
    char stdVector_ctor__name__[] = "stdVector_ctor";
    char stdVector_ctor__doc__[] = 
    "stdVector_ctor( dtype, length, initval) -> new std::vector<dtype>\n"
    ""
    ;

    PyObject * stdVector_ctor(PyObject *, PyObject *args)
    {
        int dtype = 0;
        unsigned long length = 0;
        double initval = 0.0;
        int ok = PyArg_ParseTuple( args, "ikd", &dtype, &length, &initval);
        if (!ok) return 0;

        std::stringstream errstr("stdVector_ctor()");
        journal::debug_t debug( journalname);
        PyObject *retval = 0;

        switch( dtype)
        {
        case 4:   // char
            retval = _callVectorCtor<char>( 
                dtype, length, static_cast<char>(initval), errstr);
            break;
        case 5:   // float
            retval = _callVectorCtor<float>( 
                dtype, length, static_cast<float>(initval), errstr);
            break;
        case 6:   // double
            retval = _callVectorCtor<double>( dtype, length, initval, errstr);
            break;
        case 20:  // short short
            retval = _callVectorCtor<char>( 
                dtype, length, static_cast<char>(initval), errstr);
            break;
        case 21:  // unsigned short short
            retval = _callVectorCtor<unsigned char>( 
                dtype, length, static_cast<unsigned char>(initval), errstr);
            break;
        case 22:  // short
            retval = _callVectorCtor<short>( 
                dtype, length, static_cast<short>(initval), errstr);
            break;
        case 23:  // int
            retval = _callVectorCtor<unsigned short>( 
                dtype, length, static_cast<unsigned short>(initval), errstr);
            break;
        case 24:  // int
            retval = _callVectorCtor<int>( 
                dtype, length, static_cast<int>(initval), errstr);
            break;
        case 25:  // unsigned int
            retval = _callVectorCtor<unsigned int>( 
                dtype, length, static_cast<unsigned int>(initval), errstr);
            break;
        default:
            errstr << "unsupported target datatype. Recognized datatypes:\n"
                "          char.....4\n"
                "          float....5\n"
                "          double...6\n"
                "          short short ........... 20\n"
                "          unsigned short short .. 21\n"
                "          short ................. 22\n"
                "          unsigned short ........ 23\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.str().c_str());
            debug << at(__HERE__) << errstr.str() << endl;
            return 0;
        } // switch( dtype)
        return retval;
    } // stdVector_ctor

} // stdVector::


//---------------------------- copy ctor 1 ------------------------------------


namespace 
{
    template <typename T>
    PyObject * _callVectorCopyCtor1( int dtype, PyObject *pyvec, 
                                     std::stringstream & errstr)
    {
        journal::debug_t debug( journalname);

        // recover vector to be copied:
        std::vector<T> *pvec = ARCSStdVector::unwrapVector<T>( pyvec, dtype);
        if (pvec == 0)
        {
            debug << at(__HERE__) << "unwrap failed" << endl;
            return 0; // exception context set in unwrapVector
        }

        // alloc new vector:
        std::vector<T> *pnewvec = 0;
        try
        {
            pnewvec = new std::vector<T>( *pvec);
        }
        catch (std::bad_alloc &ba)
        {
            errstr << "in _callVectorCopyCtor1<>(): ";
            errstr << ba.what();
            debug << at(__HERE__) << errstr.str() << endl;
            PyErr_SetString( PyExc_RuntimeError, errstr.str().c_str());
            return 0;
        }

        // wrap & return
        PyObject * retval = ARCSStdVector::wrapVector<T>( pnewvec, dtype);
        if( retval==0)
        {
            errstr << "wrapVector failed";
            debug << at(__HERE__) << errstr.str() << endl;
        }
        return retval;
    } // _callVectorCopyCtor1(...)

} // anonymous::


namespace stdVector
{
    char stdVector_copy_ctor1__name__[] = "stdVector_copy_ctor1";
    char stdVector_copy_ctor1__doc__[] = 
    "stdVector_copy_ctor1( dtype, length, initval) -> new std::vector<dtype>\n"
    ""
    ;

    PyObject * stdVector_copy_ctor1(PyObject *, PyObject *args)
    {
        int dtype = 0;
        PyObject *pyvec = 0;
        int ok = PyArg_ParseTuple( args, "iO", &dtype, &pyvec);
        if (!ok) return 0;

        std::stringstream errstr("stdVector_copy_ctor1()");

        PyObject *retval = 0;

        switch( dtype)
        {
        case 4:   // char
            retval = _callVectorCopyCtor1<char>( dtype, pyvec, errstr);
            break;
        case 5:   // float
            retval = _callVectorCopyCtor1<float>( dtype, pyvec, errstr);
            break;
        case 6:   // double
            retval = _callVectorCopyCtor1<double>( dtype, pyvec, errstr);
            break;
        case 20:  // short short
            retval = _callVectorCopyCtor1<char>( dtype, pyvec, errstr);
            break;
        case 21:  // unsigned short short
            retval = _callVectorCopyCtor1<unsigned char>( dtype, pyvec, errstr);
            break;
        case 22:  // short
            retval = _callVectorCopyCtor1<short>( dtype, pyvec, errstr);
            break;
        case 23:  // int
            retval = _callVectorCopyCtor1<unsigned short>( dtype, pyvec, errstr);
            break;
        case 24:  // int
            retval = _callVectorCopyCtor1<int>( dtype, pyvec, errstr);
            break;
        case 25:  // unsigned int
            retval = _callVectorCopyCtor1<unsigned int>( dtype, pyvec, errstr);
            break;
        default:
            errstr << "unsupported target datatype. Recognized datatypes:\n"
                "          char.....4\n"
                "          float....5\n"
                "          double...6\n"
                "          short short ........... 20\n"
                "          unsigned short short .. 21\n"
                "          short ................. 22\n"
                "          unsigned short ........ 23\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.str().c_str());
            return 0;
        } // switch( dtype)

        return retval;
    } // stdVector_copy_ctor1

} // stdVector::


//---------------------------- copy ctor 2 ------------------------------------


namespace 
{
    template <typename T>
    bool _callVectorCopy( int dtype, PyObject *pyvec, 
                                     PyObject *pyoutvec, 
                                     std::stringstream & errstr)
    {
        journal::debug_t debug( journalname);

        // recover vector to be copied:
        std::vector<T> *pvec = ARCSStdVector::unwrapVector<T>( pyvec, dtype);
        if (pvec == 0)
        {
            debug << at(__HERE__) << "pyvec unwrap failed" << endl;
            return false; // exception context set in unwrapVector
        }
        // recover destination vector:
        std::vector<T> *poutvec = 
            ARCSStdVector::unwrapVector<T>( pyoutvec, dtype);
        if (poutvec == 0)
        {
            debug << at(__HERE__) << "pyoutvec unwrap failed" << endl;
            return false; // exception context set in unwrapVector
        }
      
        // If destination vector cannot hold copy of source vector, resize it.
        if( (*poutvec).size() != (*pvec).size())
        {
            debug << at(__HERE__) << "resizing output vector from " 
                  << (*poutvec).size() << " to " << (*pvec).size() << endl;
            try
            {
                (*poutvec).resize( (*pvec).size());
            }
            catch (std::bad_alloc &ba)
            {
                errstr << "bad alloc in _callVectorCopy<>(): ";
                errstr << ba.what();
                debug << at(__HERE__) << errstr.str() << endl;
                PyErr_SetString( PyExc_RuntimeError, errstr.str().c_str());
                return false;
            }
        }
        
        // copy
        std::copy( (*pvec).begin(), (*pvec).end(), (*poutvec).begin());

        return true;
    } // _callVectorCopy(...)

} // anonymous::


namespace stdVector
{
    char stdVector_copy__name__[] = "stdVector_copy";
    char stdVector_copy__doc__[] = 
    "stdVector_copy( dtype, length, initval) -> None\n"
    ""
    ;

    PyObject * stdVector_copy(PyObject *, PyObject *args)
    {
        int dtype = 0;
        PyObject *pyvec = 0, *pyoutvec=0;
        int ok = PyArg_ParseTuple( args, "iOO", &dtype, &pyvec, &pyoutvec);
        if (!ok) return 0;

        std::stringstream errstr("stdVector_copy()");

        bool okay = false;

        switch( dtype)
        {
        case 4:   // char
            okay = _callVectorCopy<char>( dtype, pyvec, pyoutvec,
                                                 errstr);
            break;
        case 5:   // float
            okay = _callVectorCopy<float>( dtype, pyvec, pyoutvec, 
                                                  errstr);
            break;
        case 6:   // double
            okay = _callVectorCopy<double>( dtype, pyvec, pyoutvec,
                                                   errstr);
            break;
        case 20:  // short short
            okay = _callVectorCopy<char>( dtype, pyvec, pyoutvec,
                                                 errstr);
            break;
        case 21:  // unsigned short short
            okay = _callVectorCopy<unsigned char>( dtype, pyvec, 
                                                          pyoutvec, errstr);
            break;
        case 22:  // short
            okay = _callVectorCopy<short>( dtype, pyvec, pyoutvec, 
                                                  errstr);
            break;
        case 23:  // int
            okay = _callVectorCopy<unsigned short>( dtype, pyvec, 
                                                           pyoutvec, errstr);
            break;
        case 24:  // int
            okay = _callVectorCopy<int>( dtype, pyvec, pyoutvec, 
                                                errstr);
            break;
        case 25:  // unsigned int
            okay = _callVectorCopy<unsigned int>( dtype, pyvec, 
                                                         pyoutvec, errstr);
            break;
        default:
            errstr << "unsupported target datatype. Recognized datatypes:\n"
                "          char.....4\n"
                "          float....5\n"
                "          double...6\n"
                "          short short ........... 20\n"
                "          unsigned short short .. 21\n"
                "          short ................. 22\n"
                "          unsigned short ........ 23\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.str().c_str());
            return 0;
        } // switch( dtype)

        if( !okay) return 0;
        
        Py_INCREF( Py_None);
        return Py_None;
    } // stdVector_copy

} // stdVector::


// version
// $Id: ctor_bdgs.cc 144 2007-12-11 16:51:23Z linjiao $

// End of file
