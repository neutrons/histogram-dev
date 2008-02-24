// Timothy M. Kelley Copyright (c) 2005 All rights reserved

#include "numarray_bdgs.h"
//#include "numpy/libnumarray.h"
#include "numpy/arrayobject.h"
#include "stdVector/utils.h"

#include <sstream>

namespace
{
    /// Convert our typecode into a numarray typecode
    int getNAType( int dtype)
    {
        std::stringstream errstr;
        errstr << __FILE__ << " " << __LINE__ << " getNAType():" << std::endl;

        //NumarrayType naType;
	int naType;

        switch( dtype)
        {
        case 5:      // float
            naType = PyArray_FLOAT;
            break;

        case 6:      // double
            naType = PyArray_DOUBLE;
            break;

        case 24:     // int
            switch( sizeof( int))
            {
            case 4:
                naType = PyArray_INT;
                break;
            case 8:
                naType = PyArray_INT;
                break;
            default:
                errstr << "unexpected integer size " << sizeof(int);
                PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
                return -1;
            }
            break;

        case 25:     // unsigned
            switch( sizeof( unsigned))
            {
            case 4:
                naType = PyArray_UINT;
                break;
            case 8:
                naType = PyArray_UINT;
                break;
            default:
                errstr << "unexpected integer size" << sizeof(unsigned);
                PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
                return -1;
            }
            break;
        default:
            errstr << "unknown type code "<< dtype 
                   << ".  Recognized types and codes:\n"
                   << "    double........5\n"
                   << "    float.........6\n"
                   << "    int..........24\n"
                   << "    unsigned.....25\n";
                PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
                return -1;
        } // switch( dtype)
        return naType;
    } // getNAType


    bool getDims( std::vector<int> &dims, PyObject *pydims)
    {
        // is it a list?
        std::stringstream errstr;
        errstr << __FILE__ << " " << __LINE__ << " getDims():" << std::endl;

        if(!PyList_Check( pydims))
        {
            errstr << "third argument must be a list";
            PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
            return false;
        }
        
        // resize dims vector
        int sz = PyList_Size( pydims);
        try
        {
            dims.resize( static_cast<size_t>(sz));
        }
        catch( std::bad_alloc & badAlloc)
        {
            errstr << "Couldn't resize dims vector: " << badAlloc.what();
            PyErr_SetString( PyExc_RuntimeError, errstr.str().c_str());
            return false;
        }

        // copy list contents to vector
        for( int i = 0; i <sz; ++i)
        {
            PyObject *pyitem = PyList_GetItem( pydims, i);
            if( pyitem == 0)
            {
                return false;   // PyList_GetItem sets exception context
            }
            if( !PyInt_Check( pyitem))
            {
                errstr << "dimension sizes must be integers!";
                PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
                return false;
            }
            long dim = PyInt_AsLong( pyitem);
            dims[i] = static_cast<int>( dim);  // Numarray wants int (shrug)
        }
        return true;
    } // getDims(...)


    template <typename NumT>
    PyObject *makeNA( PyObject *pyvec, int dtype, std::vector<int> & dims,
                     int naType)
    {
        std::stringstream errstr;
        errstr << __FILE__ << " " << __LINE__ << " getNA():" << std::endl;

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        if( pvec == 0)
        {
            return 0;   // exception set by unwrapVector
        }

        NumT *pdata = &(*pvec)[0];
        char *data = (char *)pdata;

        int nd = static_cast<int>( dims.size());

        PyObject *numpyarray = 
            PyArray_FromDimsAndData( nd, &dims[0], naType, data);

        if( numpyarray == 0)
        {
            errstr << "unknown problem creating numarray. ";
	    errstr << "dims = " ;
	    for (int i = 0; i<nd; i++) 
	      errstr << dims[i] << ", ";
	    errstr << ". ";
	    errstr << "type = " << naType << ".";
            PyErr_SetString( PyExc_RuntimeError, errstr.str().c_str());
        }
        return numpyarray;
    } // getNA(...)

} // anonymous::


void _import_numpy()
{
 import_array();
}


namespace stdVector
{

    char asNumarray__name__[] = "asNumarray";
    char asNumarray__doc__[] = "document me!";
    PyObject * asNumarray(PyObject *, PyObject *args)
    {
      _import_numpy();

        PyObject *pyvec = 0, *pydims = 0;
        int dtype = 0;
        int ok = PyArg_ParseTuple( args, "OiO", &pyvec, &dtype, &pydims);
        if (!ok) return 0;

        std::vector<int> dims;
        ok = getDims( dims, pydims);
        if (!ok) return 0;

        int naType = getNAType( dtype);
        if (naType == -1) // something untoward happened in getNAType()
        {
            return 0;
        }

        PyObject *numpyarray = 0;

        switch( dtype)
        {
        case 5:  // float
            numpyarray = makeNA<float>( pyvec, dtype, dims, naType);
            break;
        case 6:  // double
            numpyarray = makeNA<double>( pyvec, dtype, dims, naType);
            break;
        case 24:  // int
            numpyarray = makeNA<int>( pyvec, dtype, dims, naType);
            break;
        case 25:  // unsigned
            numpyarray = makeNA<unsigned>( pyvec, dtype, dims, naType);
            break;
        default:
            std::stringstream errstr;
            errstr << __FILE__ << " " << __LINE__ << " asNumarray(): \n"
                   << "unrecognized datatype. Recognized types and codes:\n"
                   << "    double........5\n"
                   << "    float.........6\n"
                   << "    int..........24\n"
                   << "    unsigned.....25\n";
            PyErr_SetString( PyExc_TypeError, errstr.str().c_str());
        }

        return numpyarray;
    }


} // stdVector::

// version
// $Id: numarray_bdgs.cc 144 2007-12-11 16:51:23Z linjiao $

// End of file
