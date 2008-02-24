// Timothy M. Kelley Copyright (c) 2005 All rights reserved

#include "reduceSum_bdgs.h"
#include "stdVector/reduceSum.h"
#include "stdVector/utils.h"
#include "journal/debug.h"


namespace
{
    using journal::at;
    using journal::endl;
    char journalname [] = "stdVector.reduceSum_bdgs";
} // anonymous::


namespace stdVector
{
    // reduce2d
    char ReduceSum2d__name__[] = "ReduceSum2d";
    char ReduceSum2d__doc__[] = 
    "vectorReduce2d( 2dvec, datatype, 1dvec, otherDim, whichAxis) --> None\n"
    "Sum the 2dvec over whichAxis into the 1dvec.\n"
    "inputs:\n"
    "    2dvec (source; std::vector<datatype, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    1dvec (target; std::vector<datatype, PyCObject)\n"
    "    otherDim (length of dimension being summed over; int)\n"
    "    whichAxis (which axis is being summed over; int = 1 or 2)\n"
    "outputs: None\n"
    "Exceptions: ValueError\n"
    "Notes: 1) Recognized datatypes:\n"
    "          float....5\n"
    "          double...6\n"
    "2) otherDim*(1dvec.size()) must equal 2dvec.size()\n";

    namespace
    {
        bool _reduceSum2d_convertSzs( PyObject *pyszList, 
                                      std::vector<size_t> &szs,
                                      std::string & errstr)
        {
            if( !PyList_Check(pyszList))
            {
                errstr += "fourth argument must be a Python list!";
                PyErr_SetString( PyExc_TypeError, errstr.c_str());
                return false;
            }
            if( PyList_Size(pyszList) != 2)
            {
                errstr += "List of two dimensions must have two elements!";
                PyErr_SetString( PyExc_TypeError, errstr.c_str());
                return false;
            }
            for(size_t i=0; i<2; ++i) 
                szs[i] = static_cast<size_t>(
                    PyInt_AsLong( PyList_GetItem( pyszList, i) ) );
            return true;
        } // _reduceSum2d_convertSzs


        template <typename NumT>
        bool _callReduce2d( PyObject *py2dv,
                            int dtype, 
                            PyObject*py1dv,
                            std::vector<size_t> const & otherDim,
                            size_t axis)
        {
            journal::debug_t debug( journalname);

            std::vector<NumT> *p2dv = 
                ARCSStdVector::unwrapVector<NumT> (py2dv, dtype);
            if(p2dv == 0)
            {
                debug << at(__HERE__) << "unwrap 2d vector failed" << endl;
                return false;
            }

            std::vector<NumT> *p1dv = 
                ARCSStdVector::unwrapVector<NumT> (py1dv, dtype);
            if(p1dv == 0)
            {
                debug << at(__HERE__) << "unwrap 1d vector failed" << endl;
                return false;
            }


            ARCSStdVector::reduceSum2d<NumT>( *p2dv, *p1dv, otherDim, axis);
            return true;
        } // _callReduce2d

    } // anonymous::


    PyObject * ReduceSum2d(PyObject *, PyObject *args)
    {
        PyObject *py2dv = 0, *py1dv = 0, *pyszs = 0;
        int dtype = 0, saxis = 0;
        int ok = PyArg_ParseTuple( args, "OiOOi", &py2dv, &dtype, &py1dv, 
                                   &pyszs, &saxis);
        if (!ok) return 0;

        std::string errstr("reduce2d() ");
        if ( saxis < 1 || saxis > 2)
        {
            errstr += "axNum < 1 or axNum > 2";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        std::vector<size_t> szs(2);

        // exception context set by subroutine
        if(! _reduceSum2d_convertSzs( pyszs, szs, errstr)) return 0;

        size_t axis = static_cast<size_t>(saxis);
        bool okay = true;

        switch(dtype)
        {
        case 5:   // float
            okay = _callReduce2d<float> ( py2dv, dtype, py1dv, szs, axis);
            break;
        case 6:   // double
            okay = _callReduce2d<double>( py2dv, dtype, py1dv, szs, axis);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "          float....5\n"
                "          double...6\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        if( !okay)
        {
            return 0; // exception context set in subroutine
        }
        Py_INCREF(Py_None);
        return Py_None;	
    }


    char ReduceSum3d__name__[] = "ReduceSum3d";
    char ReduceSum3d__doc__[] = 
    "vectorReduceSum3d(vec3d, datatype, vec2d, sizes, axNum)->None\n"
    "Reduce a 3d vector by summing over axis axNum, storing results in vec2d.\n"
    "Inputs:\n"
    "    vec3d (std::vector< datatype>, PyCObject)\n"
    "    datatype (int, see Notes for codes/supported types)\n"
    "    vec2d (std::vector<datatype>, PyCObject)\n"
    "    sizes (Python list of dimensions for vec3d: 3 ints)\n"
    "    axNum (which axis to sum along, 1-3, 1 being the slowest running index,\n"
    "           3 the fastest)\n"
    "Output: PyNone\n"
    "Exceptions: ValueError, TypeError, IndexError, RuntimeError\n"
    "Notes:\n"
    "Recognized datatypes:\n"
    "    float....5\n"
    "    double...6\n"
    "    int.....24\n"
    "    unsigned int...25\n"
    "vec2d must be the correct size or an exception will be thrown.\n";

    namespace
    {
        bool _reduceSum3d_convertSzs( PyObject *pyszList, std::vector<size_t> &szs,
                                      std::string & errstr)
        {
            if( !PyList_Check(pyszList))
            {
                errstr += "fourth argument must be a Python list!";
                PyErr_SetString( PyExc_TypeError, errstr.c_str());
                return false;
            }
            if( PyList_Size(pyszList) != 3)
            {
                errstr += "List of three dimensions must have three elements!";
                PyErr_SetString( PyExc_TypeError, errstr.c_str());
                return false;
            }
            for(size_t i=0; i<3; ++i) 
                szs[i] = static_cast<size_t>(
                    PyInt_AsLong( PyList_GetItem( pyszList, i) ) );
            return true;
        } // _reduceSum3d_convertSzs(...)


        template <typename NumT>
        static bool _callReduceSum3d( PyObject *pyvec3d, PyObject *pyvec2d, 
                                      int dtype,
                                      std::vector<size_t> const & szs, 
                                      size_t axNum,
                                      std::string & errstr)
        {
            journal::debug_t debug( journalname);

            std::vector<NumT> *pvec3d = 
                ARCSStdVector::unwrapVector<NumT> (pyvec3d, dtype);
            if(pvec3d == 0)
            {
                debug << at(__HERE__) << "unwrap 3d vector failed" << endl;
                return false;
            }

            std::vector<NumT> *pvec2d = 
                ARCSStdVector::unwrapVector<NumT> (pyvec2d, dtype);
            if(pvec2d == 0)
            {
                debug << at(__HERE__) << "unwrap 2d vector failed" << endl;
                return false;
            }


            bool ok = true;
            try
            {
                ARCSStdVector::reduceSum3d<NumT>( *pvec3d, *pvec2d, szs, 
                                                  axNum);
            }
            catch( std::string & msg)
            {
                errstr += "Caught exception in call to ARCSStdVector::reduceSum3d:\n";
                errstr += msg;
                PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
                debug << at(__HERE__) << errstr.c_str() << endl;
                ok = false;
            }
            return ok;
        } // _callReduceSum3d(...)

    } // anonymous::


    PyObject * ReduceSum3d(PyObject *, PyObject *args)
    {
        int dtype = 0;
        int axNum = 0;
        PyObject *pyszs = 0, *pyvec3d = 0, *pyvec2d = 0;
        int ok = PyArg_ParseTuple( args, "OiOOi", &pyvec3d, &dtype, &pyvec2d, 
                                   &pyszs, &axNum);
        if(!ok) return 0;
        std::string errstr("reduceSum3d(): ");
        if (axNum < 1 || axNum > 3)
        {
            errstr += "axNum must be 1, 2, or 3";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        std::vector<size_t> szs(3);

        // exception context set by subroutine
        if(!_reduceSum3d_convertSzs( pyszs, szs, errstr)) return 0;

        bool good;

        // exception context set by _callReduceSum3d
        switch(dtype)
        {
        case 5:   // float
            good = _callReduceSum3d<float> ( pyvec3d, pyvec2d, dtype, szs, (size_t)axNum,
                                             errstr);
            break;
        case 6:   // double
            good = _callReduceSum3d<double>( pyvec3d, pyvec2d, dtype, szs, (size_t)axNum,
                                             errstr);
            break;
        case 24:  // int
            good = _callReduceSum3d<int>( pyvec3d, pyvec2d, dtype, szs, (size_t)axNum,
                                          errstr);
            break;
        case 25:  // unsigned int 
            good = _callReduceSum3d<unsigned int>( pyvec3d, pyvec2d, dtype, szs, 
                                                   (size_t)axNum, errstr);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "          float....5\n"
                "          double...6\n"
                "    int.....24\n"
                "    unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        if (!good) return 0;
        Py_INCREF(Py_None);
        return Py_None;	
    }


} // stdVector::

// version
// $Id: reduceSum_bdgs.cc 102 2005-07-31 21:39:44Z tim $

// End of file
