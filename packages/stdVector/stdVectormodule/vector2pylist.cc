// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vector2pylist.h"
#include "stdVector/utils.h"
#include <vector>
#include <string>

#ifdef BLD_PROCEDURE
#include "journal/info.h"
#include "journal/debug.h"
#endif

namespace
{
#ifdef BLD_PROCEDURE
//    journal::info_t info("stdVector");
//    journal::debug_t debug("stdVector");
//    bool havejournal = true;
    using journal::at;
    using journal::endl;
// #else
//     bool havejournal = false;
#endif

    //------------------ C Numbers to Python numbers -------------------
    template <typename T> PyObject *_convertNum( T num)
    {
        return PyFloat_FromDouble( num);
    }
    template <> PyObject *_convertNum<float>( float num)
    {
        return PyFloat_FromDouble( (double)num);
    }
    template <> PyObject *_convertNum<int>( int num)
    {
        return PyInt_FromLong( num);
    }
    template <> PyObject *_convertNum<unsigned>( unsigned num)
    {
        return PyInt_FromLong( (unsigned)num);
    }

    //------------------ Load vector -> Python list ---------------------
    template <typename NumT>
    PyObject *_vec2NewList( PyObject *pyvec, std::string & errstr, 
                            int type)
    {
        journal::debug_t debug("stdVector");
        

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, type);
        if( !pvec) return 0; // exception context set by unwrapVector

        size_t len = (*pvec).size();
        PyObject *pylist = PyList_New( (int)len);

        int ok = 0;
        for( size_t i=0; i<len; ++i)
        {
            ok = PyList_SetItem( pylist, i, _convertNum<NumT>((*pvec)[i]));
            if( ok != 0)
            {
                errstr += "unknown problem loading list in _vec2NewList";
//                 if(havejournal) debug << at(__HERE__) << errstr << endl;
                PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
                return 0;
            }
        }
        return pylist;
    }// PyObject *_vec2NewList( ...


    //------------------ Load vector -> Python string ---------------------
    PyObject *_vec2NewStr( PyObject *pyvec, std::string & errstr, 
                           int type)
    {
        journal::debug_t debug("stdVector");
        
        std::vector<char> *pvec = 
            ARCSStdVector::unwrapVector<char>( pyvec, type);
        if( !pvec) return 0; // exception context set by unwrapVector

        size_t len = (*pvec).size();
        char * buf = new char[len+1]; buf[len]=0;

        for( size_t i=0; i<len; ++i) 
        {
            buf[i] = (*pvec)[i];
        }

        PyObject *pystr = PyString_FromStringAndSize( buf, len);
        delete [] buf;
        return pystr;
    }// PyObject *_vec2NewStr( ...
    
} // anonymous::


char pystdVector_vector2pylist__name__[] = "vector2pylist";
char pystdVector_vector2pylist__doc__[] = 
"vector2pylist( pyCObject, type) -> python list\n"
"Convert a C++ STL vector to a Python\n"
"inputs: \n"
"    pyCObject (must wrap a VectorWrapper pointer)\n"
"    type (data type, integer, one of the following recognized types:\n"
"        char.........4\n"
"        float........5\n"
"        double.......6\n"
"        int.........24\n"
"        unsigned....25\n"
"output:\n"
"    python list with contents of vector\n"
"Exceptions: TypeError, ValueError, RuntimeError\n";

PyObject * pystdVector_vector2pylist(PyObject *, PyObject *args)
{
    journal::debug_t debug("stdVector");

    std::string errstr("vector2pylist wrapper ");

    PyObject *pycobj = 0;
    int type = 0;
    int ok = PyArg_ParseTuple( args, "Oi", &pycobj, &type);
    if (!ok) return 0;

    if(!PyCObject_Check( pycobj))
    {
        errstr += "arg 1: must be a PyCObject wrapping a std::vector";
	//        if(havejournal) debug << at(__HERE__) << errstr << endl;
        PyErr_SetString( PyExc_TypeError, errstr.c_str());
        return 0;
    }

    // Do not add a type without adding an explicit specialization
    // of _convertNum
    switch( type)
    {
    case 4:  // char
        return _vec2NewStr( pycobj, errstr, type);
        break;
    case 5:  // float       
        return _vec2NewList<float>( pycobj, errstr, type);
        break;
    case 6:  // double 
        return _vec2NewList<double>( pycobj, errstr, type);
        break;
    case 24: // int
        return _vec2NewList<int>( pycobj, errstr, type);
        break;
    case 25: // unsigned
        return _vec2NewList<unsigned>( pycobj, errstr, type);
        break;
    default:
        errstr += "unrecognized data type. Known types are\n"
            "    char..........4\n"
            "    double........5\n"
            "    float.........6\n"
            "    int..........24\n"
            "    unsigned.....25\n";
	//        if(havejournal) debug << at(__HERE__) << errstr << endl;
        PyErr_SetString(PyExc_ValueError, errstr.c_str());
        return 0;
    }
    // never reached
    errstr += "reached \"unreachable\" code";
    //if(havejournal) debug << at(__HERE__) << errstr << endl;
    PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
    return 0;    

} // pystdVector_vector2pylist(...




// version
// $Id: vector2pylist.cc 138 2007-03-29 21:41:29Z linjiao $

// End of file
