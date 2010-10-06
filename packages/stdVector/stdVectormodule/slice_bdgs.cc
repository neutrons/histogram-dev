// Timothy M. Kelley Copyright (c) 2005 All rights reserved

#include "slice_bdgs.h"

#include "stdVector/slice.h"
#include "stdVector/utils.h"
#include "journal/debug.h"
//#include "reduction/utils.h"
#include "stdVector/reduction_utils.h"


// extractSlice
namespace
{
    using journal::at;
    using journal::endl;
    const char journalname[] = "stdVector";

    template <typename NumT>
    static bool _callExtractSlice( PyObject *pysrc,
                                   int dtype,
                                   PyObject *pytarg,
                                   std::slice const & slc,
                                   std::string & errstr)
    {
        journal::debug_t debug(journalname);

        debug << at(__HERE__) << "about to unwrap source vector" << endl;
        
        std::vector<NumT> *psrc = 
            ARCSStdVector::unwrapVector<NumT> (pysrc, dtype);

        debug << at(__HERE__) << "about to unwrap target vector" << endl;
        
        std::vector<NumT> *ptarg = 
            ARCSStdVector::unwrapVector<NumT> (pytarg, dtype);

        debug << at(__HERE__) << "about to call extractSlice" << endl;
        
        try
        {
            ARCSStdVector::extractSlice<NumT>( *psrc, *ptarg, slc);
        }
        catch( std::string & str)
        {
            errstr += "Caught exception: ";
            errstr += str;
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return false;
        }
        return true;
    }
} // anonymous::


namespace stdVector
{
    char extractSlice__name__[] = "extractSlice";
    char extractSlice__doc__[] = 
    "extractSlice( source, datatype, target, slice) --> None\n"
    "Extract slice from source, load into target.\n"
    "inputs:\n"
    "    source (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    target (std::vector<datatype>, PyCObject)\n"
    "    slice (std::slice, PyCObject)\n"
    "output: None\n"
    "Exceptions: ValueError\n"
    "Notes: ";

    PyObject * extractSlice(PyObject *, PyObject *args)
    {
        PyObject *pysrc = 0, *pytarg = 0, *pyslice = 0;
        int dtype = 0;
        int ok  = PyArg_ParseTuple( args, "OiOO", &pysrc, &dtype, &pytarg, 
                                    &pyslice);
        if(!ok) return 0; 

        std::string errstr("extractSlice ");
        journal::debug_t debug(journalname);

        debug << at(__HERE__) << "about to unwrap" << endl;

        std::slice *slice = 
            Reduction::utils::unwrapObject<std::slice>( pyslice, 0);

        if( slice == 0)
        {
            // exception context set by unwrapObject
            debug << at(__HERE__) << "unwrap failed" << endl;

            return 0;
        }

        bool okay = true;

        switch (dtype)
        {
        case 5:   // float
            okay = _callExtractSlice<float>( pysrc, dtype, pytarg, *slice, 
                                             errstr);
            break;
        case 6:   // double
            okay = _callExtractSlice<double>( pysrc, dtype, pytarg, *slice, 
                                              errstr);
            break;
        case 24:  // int
            okay = _callExtractSlice<int>( pysrc, dtype, pytarg, *slice, 
                                           errstr);
            break;
        case 25:  // unsigned int
            okay = _callExtractSlice<unsigned int>( pysrc, dtype, pytarg, 
                                                    *slice, errstr);
            break;
        default:
            errstr += "unrecognized datatype. Recognized datatypes:\n"
                "          float....5\n"
                "          double...6\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        if( !okay)
        {
            return 0; // exception context set in subroutine
        }
        Py_INCREF( Py_None);
        return Py_None;
    } // extractSlice( ...)


// slice ctor

    int slice__magicNumber__ = 610849325;

    char slice_ctor3__name__[] = "slice_ctor3"; 
    char slice_ctor3__doc__[] = 
    "slice_ctor3( start, size, stride) -> new std::slice object\n"
    "Create a new std::slice object\n"
    "Inputs:\n"
    "    start: offset in array\n"
    "    size: number of elements in slice\n"
    "    stride: distance between elements in the slice (1 means contiguous)\n"
    "Output:\n"
    "    new slice object, wrapped in ObjectWrapper with type zero\n"
    "Exceptions: None\n"
    "Notes: None\n";


    PyObject * slice_ctor3(PyObject *, PyObject *args)
    {
        size_t start = 0, size = 0, stride = 0;
        int ok = PyArg_ParseTuple( args, "III", &start, &size, &stride);
        if(!ok) return 0;

        journal::debug_t debug(journalname);
        std::stringstream errstr("stdVector::slice_ctor3 ");
        
        std::slice *pslice = 0;

        debug << at(__HERE__) << "about to allocate" << endl;

        try
        {
            pslice = new std::slice( start, size, stride);
        }
        catch( std::bad_alloc & ba)
        {
            errstr << "Failed to allocate new std::slice; message: "
                   << ba.what();
            debug << at(__HERE__) << errstr.str().c_str() << journal::endl;
            return 0;
        }

        debug << at(__HERE__) << "about to wrap" << endl;

        PyObject *retval = 
            Reduction::utils::wrapObject<std::slice>( pslice, 0, 
                                                      slice__magicNumber__);
        if( retval == 0)
        {
            // error context set in wrapObject<T>
            delete pslice;
        }

        debug << at(__HERE__) << "about to return" << endl;
 
        return retval;
    }


    // get the wrapper magic number
    char slice_magicNumber__name__[] = "slice_magicNumber";
    char slice_magicNumber__doc__[] = 
    "slice_magicNumber() -> # associated with this class\n"
    "Input: None\n"
    "Output: int\n"
    "Exceptions: None\n"
    "Notes: None\n";

    PyObject * slice_magicNumber(PyObject *, PyObject *args)
    {
        return Py_BuildValue("i", slice__magicNumber__);
    }


    char slice_start__name__[] = "slice_start";
    char slice_start__doc__[] =
    "slice_start( handle) -> start\n"
    "Get the start of this slice\n"
    "Input:\n"
    "    slice instance (wrapped by Reduction::utils::wrapObject<T>)\n"
    "Output:\n"
    "    start (integer)\n"
    "Exceptions: TypeError\n"
    "Notes: None\n";

    PyObject * slice_start(PyObject *, PyObject *args)
    {
        PyObject *pyslice = 0;
        int ok = PyArg_ParseTuple( args, "O", &pyslice);
        if (!ok) return 0;

        std::slice *pslice = 
            Reduction::utils::unwrapObject<std::slice>( pyslice, 0);
        if( pslice == 0)
        {
            // exception context set by unwrapObject
            journal::debug_t debug(journalname);
            debug << at(__HERE__) << "Failed to unwrap slice" << endl;
            return 0;
        }
        
        size_t start = pslice->start();
        int sstart = static_cast<int>( start);
        return Py_BuildValue("i", sstart);
    } // slice_start(...)


    char slice_size__name__[] = "slice_size";
    char slice_size__doc__[] = 
    "slice_size( handle) -> size\n"
    "Get the size of this slice\n"
    "Input:\n"
    "    slice instance (wrapped by Reduction::utils::wrapObject<T>)\n"
    "Output:\n"
    "    size (integer)\n"
    "Exceptions: TypeError\n"
    "Notes: None\n";

    PyObject * slice_size(PyObject *, PyObject *args)
    {
        PyObject *pyslice = 0;
        int ok = PyArg_ParseTuple( args, "O", &pyslice);
        if (!ok) return 0;

        std::slice *pslice = 
            Reduction::utils::unwrapObject<std::slice>( pyslice, 0);
        if( pslice == 0)
        {
            // exception context set by unwrapObject
            journal::debug_t debug(journalname);
            debug << at(__HERE__) << "Failed to unwrap slice" << endl;
            return 0;
        }
        
        size_t size = pslice->size();
        int ssize = static_cast<int>( size);
        return Py_BuildValue("i", ssize);
    } // slice_size(...)


    char slice_stride__name__[] = "slice_stride";
    char slice_stride__doc__[] = 
    "slice_stride( handle) -> stride\n"
    "Get the stride of this slice\n"
    "Input:\n"
    "    slice instance (wrapped by Reduction::utils::wrapObject<T>)\n"
    "Output:\n"
    "    stride (integer)\n"
    "Exceptions: TypeError\n"
    "Notes: None\n";

    PyObject * slice_stride(PyObject *, PyObject *args)
    {
        PyObject *pyslice = 0;
        int ok = PyArg_ParseTuple( args, "O", &pyslice);
        if (!ok) return 0;

        std::slice *pslice = 
            Reduction::utils::unwrapObject<std::slice>( pyslice, 0);
        if( pslice == 0)
        {
            // exception context set by unwrapObject
            journal::debug_t debug(journalname);
            debug << at(__HERE__) << "Failed to unwrap slice" << endl;
            return 0;
        }
        
        size_t stride = pslice->stride();
        int sstride = static_cast<int>( stride);
        return Py_BuildValue("i", sstride);
    } // slice_stride(...)


} // stdVector




// version
// $Id: slice_bdgs.cc 100 2005-07-29 20:24:35Z tim $

// End of file
