// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "pylist2vector.h"
#include "stdVector/utils.h"
#include <vector>
#include <string>
#include <sstream>

#ifdef BLD_PROCEDURE
#include "journal/info.h"
#include "journal/debug.h"
#else
#include <iostream>
#endif

#include "array_kluge/array_kluge.h"

namespace
{
#ifdef BLD_PROCEDURE
//    journal::info_t info("stdVector");
//    journal::debug_t debug("stdVector");
//    bool havejournal = true;
    using journal::at;
    using journal::endl;

    const char journalname[] = "stdVector";
#endif


    //------------------ Python numbers to C numbers -------------------
    template <typename T> T _convertPyNum( PyObject *pynum)
    {
        return PyFloat_AsDouble( pynum);
    }
    template <> float _convertPyNum<float>( PyObject *pynum)
    {
        return (float)PyFloat_AsDouble( pynum);
    }
    template <> int _convertPyNum<int>( PyObject *pynum)
    {
        return PyInt_AsLong( pynum);
    }
    template <> unsigned _convertPyNum<unsigned>( PyObject *pynum)
    {
        return (unsigned)PyInt_AsLong( pynum);
    }

    //-------------------- list -> vector loading ---------------------
    template <typename NumT>
    PyObject *_list2NewVec( PyObject *pylist, std::ostringstream &oss, 
                            int datatype)
    {
        size_t len = (size_t) PyList_Size( pylist);
        std::vector<NumT> *pvec = 0;

        journal::debug_t debug( journalname);

        try
        {
            pvec = new std::vector<NumT>(len);
        }
        catch( std::bad_alloc & ba)
        {
            oss << " Failed to allocate std::vector";
            PyErr_SetString( PyExc_RuntimeError, oss.str().c_str());
            debug << at(__HERE__) << oss.str() << "; message: " << ba.what() 
                  << endl;
            return 0;
        }

        for(size_t i=0; i<len; ++i)
        {
            PyObject *pynum = PyList_GetItem( pylist, i);
            NumT num = _convertPyNum<NumT>( pynum);
            (*pvec)[i] = num;
        }

        PyObject *retval = ARCSStdVector::wrapVector<NumT>( pvec, datatype);
        if( retval == 0)
        {
            // exception context set by wrapVector
            delete pvec;
            debug << at(__HERE__) << "wrapVector FAILED" << endl;
        }
        return retval;
    
    } // PyObject *_list2NewVec( ...


    PyObject *_str2NewVec( PyObject *pystr, std::ostringstream & oss,
                           int datatype)
    {
        size_t len = static_cast<size_t>( PyString_Size( pystr ));
        const char * str = PyString_AsString( pystr );
      
        journal::info_t info( journalname);
        journal::debug_t debug( journalname);
        info << at(__HERE__) << "size of string " << str << " is " << len 
             << endl;
      
        std::vector<char> *pvec = 0;
        try
        {
            pvec = new std::vector<char>( str, str+len);
        }
        catch( std::bad_alloc &ba)
        {
            oss << " Failed to allocate std::vector<char>";
            PyErr_SetString( PyExc_RuntimeError, oss.str().c_str());
            debug << at(__HERE__) << oss.str() << "; message: " << ba.what() 
                  << endl;
            return 0;
        }

        PyObject *retval = ARCSStdVector::wrapVector<char>( pvec, datatype);
        if( retval == 0)
        {
            // exception context set by wrapVector
            delete pvec;
            debug << at(__HERE__) << "wrapVector FAILED" << endl;
        }
        return retval;
    } // _str2NewVec( ...)
  

} // anonymous::


char pystdVector_pylist2vector__name__[] = "pylist2vector";
char pystdVector_pylist2vector__doc__[] = 
"pylist2vector( list, type) -> PyCObject wrapping stdVector\n"
"Convert a Python list to a C++ STL vector\n"
"inputs: \n"
"    python list of numbers\n"
"    type (data type, integer, one of the following recognized types:\n"
"        char.........4\n"
"        float........5\n"
"        double.......6\n"
"        int.........24\n"
"        unsigned....25\n"
"output:\n"
"    PyCObject wrapping a VectorWrapper. C++ can recover the pointer\n"
"    to the vector by using stdVector::unwrapVector().\n"
"Exceptions: TypeError, ValueError, RuntimeError\n";

PyObject * pystdVector_pylist2vector(PyObject *, PyObject *args)
{
    journal::debug_t debug("stdVector");

    std::string errstr("pylist2vector wrapper ");
    std::ostringstream oss(errstr);

    PyObject *pylist = 0;
    int type = 0;
    int ok = PyArg_ParseTuple( args, "Oi", &pylist, &type);
    if (!ok) return 0;

    if ( !PyList_Check( pylist) && type !=4) {
      oss << "pylist2vector argument 1: must be a Python list of numbers";
#ifdef BLD_PROCEDURE
      debug << at(__HERE__) << oss.str() << endl;
#endif
      PyErr_SetString(PyExc_TypeError, oss.str().c_str());
      return 0;
    }
      
    if ( !PyString_Check( pylist) && type==4 ) 
    {
      oss << "pylist2vector argument 1: must be a string";
#ifdef BLD_PROCEDURE
      debug << at(__HERE__) << oss.str() << endl;
#endif
      PyErr_SetString(PyExc_TypeError, oss.str().c_str());
      return 0;
    }

    // Do not add a type without adding an explicit specialization
    // of _convertPyNum
    switch( type)
    {
    case 4:  // char
        return _str2NewVec( pylist, oss, type);
        break;
    case 5:  // float
        return _list2NewVec<float>( pylist, oss, type);
        break;
    case 6:  // double 
        return _list2NewVec<double>( pylist, oss, type);
        break;
    case 24: // int
        return _list2NewVec<int>( pylist, oss, type);
        break;
    case 25: // unsigned
        return _list2NewVec<unsigned>( pylist, oss, type);
        break;
    case NX_INT64:
        typedef long long int64;
        if ( sizeof( int64 ) != 8 ) {
           oss    << "This is not a 64-bit machine\n";
           PyErr_SetString(PyExc_ValueError, oss.str().c_str());
           return 0;
        }
        return _list2NewVec<int64>( pylist, oss, type);
    default:
        oss    << "unrecognized data type "
               << type 
         << ". Known types are\n"
            "    char..........4\n"
            "    double........5\n"
            "    float.........6\n"
            "    int..........24\n"
            "    unsigned.....25\n";
#ifdef BLD_PROCEDURE
	debug << at(__HERE__) << oss.str() << endl;
#endif
        PyErr_SetString(PyExc_ValueError, oss.str().c_str());
        return 0;
    }
    // never reached
    oss    << "reached \"unreachable\" code";
#ifdef BLD_PROCEDURE
    debug << at(__HERE__) << oss.str() << endl;
#endif
    PyErr_SetString( PyExc_RuntimeError, oss.str().c_str());
    return 0;
} // PyObject * pystdVector_pylist2vector(PyObject *, PyObject *args)


// version
// $Id: pylist2vector.cc 139 2007-05-03 00:30:11Z linjiao $

// End of file
