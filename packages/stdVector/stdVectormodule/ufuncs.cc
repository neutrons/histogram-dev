// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "ufuncs.h"
#include "stdVector/utils.h"
#include <string>
#include "journal/info.h"
#include "journal/debug.h"
#include <iostream>
#include <sstream>
#include <numeric> // std::accumulate
#include <cmath>

using namespace ARCSStdVector;

namespace 
{
    char journalname [] = "stdVector_bdgs";
    using journal::at;
    using journal::endl;

} // anonymous namespace


namespace 
{
    typedef std::vector<float>::iterator vfit;
    typedef std::vector<double>::iterator vdit;
    typedef std::vector<unsigned>::iterator vuit;
    typedef std::vector<int>::iterator viit;

    template <typename NumT, typename ItT>
    PyObject * _accumPlus( PyObject *pyvec, int dtype, size_t start, 
                           size_t end, std::stringstream & errstr)
    {
        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        std::vector<NumT> &vec( *pvec);

        if( start > end)
        {
            errstr << "start (" << start << ") is greater than end (" << end
                   << ")";
            PyErr_SetString( PyExc_IndexError, errstr.str().c_str());
            return 0;
        }
        if( end > vec.size())
        {
            errstr << "end (" << end << ") is greater than size of vector ("
                   << vec.size() << ")";
            PyErr_SetString( PyExc_IndexError, errstr.str().c_str());
            return 0;
        }
        
        ItT s = vec.begin() + start;
        ItT e = vec.begin() + end;
        
        NumT accum = std::accumulate( s, e, static_cast<NumT>(0.0));
        return Py_BuildValue( "d", static_cast<double>(accum));
    }
} // anonymous::

namespace stdVector
{
    char accumPlus__name__[] = "accumPlus";
    char accumPlus__doc__[] =
    "accumPlus( vector, dtype, start, end) -> avg\n"
    "add elements of the vector from start to but not including end\n"
    "Inputs:\n"
    "    vector: std::vector<dtype> (StdVector.handle())\n"
    "    dtype: datatype (int). Recognized datatypes:\n"
    "        5......float\n"
    "        6.....double\n"
    "        24..unsigned\n"
    "        25.......int\n"
    "Output:\n"
    "    \\sum_{i in [start, end)}\n"   // remember: escape the "\"
    "Exceptions: ValueError, IndexError\n"
    "Notes: start must be less than end, and end must be >= size\n"
    "       of the vector.";

    PyObject * accumPlus(PyObject *, PyObject *args)
    {
        int dtype = 0; 
        unsigned start = 0, end = 0;
        PyObject *pyvec = 0;
        int ok = PyArg_ParseTuple( args, "OiII", &pyvec, &dtype, &start, &end);
        if(!ok) return 0;

        std::stringstream errstr("stdVector::average");

        switch( dtype)
        {
        case 5:   // float
            return _accumPlus<float, vfit>( pyvec, dtype, start, end, errstr);
        case 6:   // double
            return _accumPlus<double, vdit>( pyvec, dtype, start, end, errstr);
        case 24:   // int
            return _accumPlus<int, viit>( pyvec, dtype, start, end, errstr);
        case 25:   // unsigned 
            return _accumPlus<unsigned, vuit>( pyvec, dtype, start, end, errstr);
        default:
            errstr << "Unrecognized datatype. Recognized datatypes for this fn:\n"
                "    5......float\n"
                "    6.....double\n"
                "    int........24\n"
                "    unsigned...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.str().c_str());
            return 0;
        } // switch(...)
        // unreachable!
    } // average
}




namespace 
{
    template <typename NumT>
    size_t _callSize( PyObject *pyvec, int dtype)
    {
        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        if (pvec == 0) 
        {
            std::string errstr("unwrapVector failed");
            throw errstr;
        }

        return pvec -> size();
    }
} // anonymous::


namespace stdVector
{
    char size__name__[] = "size";
    char size__doc__[] =
    "size( StdVector_handle) -> size of vector"
    "Inputs: \n"
    "    wrapped StdVector PyCObject\n"
    "    datatype (see below for supported types)."
    "Output: \n"
    "    number of elements (long integer)\n"
    "Exceptions: ValueError"
    "Recognized datatypes:\n"
    "    char........4\n"
    "    float.......5\n"
    "    double......6\n"
    "    int........24\n"
    "    unsigned...25\n";

    PyObject * size(PyObject *, PyObject *args)
    {
        journal::debug_t debug("ARCSStdVector");

        PyObject *pyvec = 0;
        int dtype = 0;
        int ok = PyArg_ParseTuple( args, "Oi", &pyvec, &dtype);
        if (!ok) return 0;

        std::string errstr("pystdVector_size() ");
        size_t sz = 0;

        try
        {
            switch( dtype)
            {
            case 4:   // char
                sz = _callSize<char>( pyvec, dtype);
                break;
            case 5:   // float
                sz = _callSize<float>( pyvec, dtype);
                break;
            case 6:   // double
                sz = _callSize<double>( pyvec, dtype);
                break;
            case 24:  // int
                sz = _callSize<int>( pyvec, dtype);
                break;
            case 25:  // unsigned int 
                sz = _callSize<unsigned>( pyvec, dtype);
                break;
            default:
                errstr +="unrecognized or unallowed datatype. Allowed datatypes:\n"
                    "          char........4\n"
                    "          float.......5\n"
                    "          double......6\n"
                    "          int........24\n"
                    "          unsigned...25\n";
                debug << at(__HERE__) << errstr;
                debug.newline();
                debug << "Datatype = " << dtype << endl;
                PyErr_SetString( PyExc_ValueError, errstr.c_str());
                return 0;
            } // switch( dtype) ...

            PyObject *pysz = PyLong_FromUnsignedLong( sz);
            return pysz;
        }
        catch (std::string & errstr)
        {
            return 0;
        }

    } // pystdVector_size( ...)

} // stdVector::

namespace
{
    template <typename NumT>
    void *_getPointer( PyObject *pyvec,
                       int dtype,
                       unsigned int offset,
                       std::string & errstr)
    {
        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector< NumT>( pyvec, dtype);
        // Unwrap vector sets Python's error indicator if necessary
        if (pvec == 0) return 0;

        if( offset >=  (*pvec).size())
        {
            errstr += "index too large";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }

        std::vector<NumT> & vec( *pvec);

//         return (void *) &(*pvec)[offset];
        NumT *pnt = &vec[offset];
        return (void *)pnt;
    } // _getPointer

} // anonymous::


namespace stdVector
{
    char voidPtr__name__[] = "voidPtr";
    char voidPtr__doc__[] = 
    "voidPtr( vector, datatype, offset)\n"
    "get a void ptr to the c-array part of a vector\n"
    "inputs:\n"
    "    vector (PyCObject/void ptr to vector object)\n"
    "    datatype (type of data stored in vector; int)\n"
    "    offset (index into c-array; int>=0)\n"
    "output: PyCObject w/ void pointer to &c_array[offset]\n"
    "Exceptions: ValueError";


    PyObject * voidPtr(PyObject *, PyObject *args)
    {
        int dtype = 0, soffset = 0;
        PyObject *pyvec = 0;
        int ok  = PyArg_ParseTuple( args, "Oii", &pyvec, &dtype, &soffset);
        if(!ok) return 0; 

        std::string errstr("pyreduction_vectorVoidPtr() ");

        if( soffset < 0 )
        {
            errstr += "index less than 0";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }

        unsigned int offset = static_cast<unsigned int>(soffset);
        void *ptr = 0;
        switch (dtype)
        {
        case 4:   // char
            ptr = _getPointer<char>( pyvec, dtype, offset, errstr);
            break;
        case 5:   // float
            ptr = _getPointer<float>( pyvec, dtype, offset, errstr);
            break;
        case 6:   // double
            ptr = _getPointer<double>( pyvec, dtype, offset, errstr);
            break;
        case 24:  // int
            ptr = _getPointer<int>( pyvec, dtype, offset, errstr);
            break;
        case 25:  // unsigned int
            ptr = _getPointer<unsigned>( pyvec, dtype, offset, errstr);
            break;
        default:
            errstr += "unrecognized datatype. Recognized datatypes:\n"
                "          char.....4\n"
                "          float....5\n"
                "          double...6\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        } // switch

        journal::debug_t debug(journalname);

        // exception context set in _getPointer<>()
        if (ptr == 0) 
        {
            debug << at(__HERE__) << "null pointer from _getPointer" << endl;
            return 0;
        }
        else return PyCObject_FromVoidPtr( ptr, 0);
    } // voidPtr
} // stdVector::

namespace
{
    /// _recoverVal: dig a C number out of a Python number object.
    template <typename NumT>
    NumT _recoverVal( PyObject *pyval)
    {
        return PyFloat_AsDouble( pyval);
    }
    template <> float _recoverVal<float>( PyObject *pynum)
    { 
        return (float)PyFloat_AsDouble( pynum); 
    }
    template <> int _recoverVal<int>( PyObject *pynum)
    { 
        return PyInt_AsLong( pynum); 
    }
    template <> unsigned _recoverVal<unsigned>( PyObject *pynum)
    { 
        return (unsigned)PyInt_AsLong( pynum); 
    }

    template <typename NumT>
    bool _callAssign( PyObject *pyvec, int dtype, unsigned count, 
                      PyObject *pyval)
    {
        journal::debug_t debug("ARCSStdVector");

        debug << at(__HERE__) << "before unwrapVector" << endl;

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        // Unwrap vector sets Python's error indicator if necessary
        if (pvec == 0) return false;

        debug << at(__HERE__) << "after unwrap" << endl;

        NumT val = _recoverVal<NumT>( pyval);

        debug << at(__HERE__) << "val = " << val << endl;

        pvec -> assign( count, val);
        return true;
    }

} // anonymous::


namespace stdVector
{
// assign
    char assign1__name__[] = "assign";
    char assign1__doc__[] = 
    "assign( vector, datatype, count, val) --> None\n"
    "Invokes std::vector::assign on the vector\n"
    "inputs:\n"
    "    vector ..(PyCObject/void ptr to vector object)\n"
    "    datatype (type of data stored in vector; int)\n"
    "    count (number of copies of value to insert)\n"
    "    value ...(float)\n"
    "output: PyCObject w/ void pointer to &c_array[offset]\n"
    "Exceptions: ValueError";


    PyObject * assign1(PyObject *, PyObject *args)
    {
        journal::debug_t debug("ARCSStdVector");

        std::string errstr("pystdVector_assign1() ");

        PyObject *pyvec = 0, *pyval = 0;
        int dtype = 0, scount = 0;

        int ok = PyArg_ParseTuple( args, "OiiO", &pyvec, &dtype, &scount, 
                                   &pyval);
        if (!ok) return 0;

        if (scount < 0)
        {
            errstr += "must assign 0 or more elements";
            debug << at(__HERE__) << errstr.c_str() << endl;
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        unsigned count = static_cast<unsigned>( scount);

        bool assignOK = false;

        switch( dtype)
        {
        case 5:  // float
            assignOK = _callAssign<float>( pyvec, dtype, count, pyval);
            break;
        case 6:  // double
            assignOK = _callAssign<double>( pyvec, dtype, count, pyval);
            break;
        case 24:  // int
            assignOK = _callAssign<int>( pyvec, dtype, count, pyval);
            break;
        case 25:  // unsigned
            assignOK = _callAssign<unsigned>( pyvec, dtype, count, pyval);
            break;
        default:
            errstr += "unrecognized data type. Recognized types: "           
                "          float.......5\n"
                "          double......6\n"
                "          int........24\n"
                "          unsigned...25\n";
            debug << at(__HERE__) << errstr.c_str();
            debug.newline();
            debug << "Data type = " << dtype << endl;
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        } // switch( dtype) ...

        if (assignOK)
        {
            Py_INCREF( Py_None);
            return Py_None;
        }
        else return 0;
    }

} // stdVector::


// ----------------------------- square ------------------------------
namespace
{
    template <typename NumT>
    bool _square( PyObject *pyinvec, PyObject *pyoutvec, int dtype, 
                  std::string & errstr)
    {
        journal::debug_t debug("ARCSStdVector");

        std::vector<NumT> *pinvec = 
            ARCSStdVector::unwrapVector<NumT>( pyinvec, dtype);
        std::vector<NumT> *poutvec = 
            ARCSStdVector::unwrapVector<NumT>( pyoutvec, dtype);
        
        if ( pinvec == 0 || poutvec == 0)
        {
            errstr += "ARCSStdVector::unwrapVector returned null pointer(s)";
            debug << at(__HERE__) << errstr << ": pinvec = " << pinvec 
                  << ", poutvec = " << poutvec << endl;
            return false;
        } 
        // convenience:
        std::vector<NumT> const & invec( *pinvec);
        std::vector<NumT> & outvec( *poutvec);

        if(outvec.size() != invec.size())
        {
            debug << at(__HERE__) << "resizing outvec from " << outvec.size() 
                  << " to " << invec.size() << endl;
            outvec.resize( invec.size());
        }
        
        for (size_t i=0; i < invec.size(); ++i)
        {
            outvec[i] = invec[i]*invec[i];
        }
        return true;
    } // _square()
} // anonymous::


namespace stdVector
{
    char square__name__[] = "square";
    char square__doc__[] =
    "square( invector, outvector, dtype) -> square input, store in output.\n"
    "Inputs:\n"
    "    invector: std::vector<dtype>\n"
    "    outvector: std::vector<dtype>\n"
    "    dtype: datatype, one of 5....float, 6....double\n"
    "Output:\n"
    "    None\n"
    "Exceptions: ValueError\n"
    "Notes: input and output vectors must be same type.";

    PyObject * square(PyObject *, PyObject *args)
    {
        int dtype = 0;
        PyObject *pyinvec = 0, *pyoutvec = 0;
        int ok = PyArg_ParseTuple( args, "OOi", &pyinvec, &pyoutvec, &dtype);

        if(!ok) return 0;

        std::string errstr("stdVector::square");

        bool aok = false;

        switch(dtype)
        {
        case 5: //float
            aok = _square<float>( pyinvec, pyoutvec, dtype, errstr);
            break;
        case 6: //double
            aok = _square<double>( pyinvec, pyoutvec, dtype, errstr);
            break;
        default:
            errstr += "Unrecognized datatype. Recognized datatypes for this "
                "function are:\n"
                "    5......float\n"
                "    6.....double\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        if(aok)
        {
            Py_INCREF( Py_None);
            return Py_None;
        }
        else
        {
            return 0;
        }
    }//square()

}   //stdVector::


// ---------------------------------- sqrt ------------------------------------
namespace
{
    template <typename NumT>
    bool _sqrt( PyObject *pyinvec, PyObject *pyoutvec, int dtype, 
                  std::string & errstr)
    {
        journal::debug_t debug("ARCSStdVector");

        std::vector<NumT> *pinvec = 
            ARCSStdVector::unwrapVector<NumT>( pyinvec, dtype);
        std::vector<NumT> *poutvec = 
            ARCSStdVector::unwrapVector<NumT>( pyoutvec, dtype);
        
        if ( pinvec == 0 || poutvec == 0)
        {
            errstr += "ARCSStdVector::unwrapVector returned null pointer(s)";
            debug << at(__HERE__) << errstr << ": pinvec = " << pinvec 
                  << ", poutvec = " << poutvec << endl;
                  // Error context set by unwrapVector
            return false;
        } 
        // convenience:
        std::vector<NumT> const & invec( *pinvec);
        std::vector<NumT> & outvec( *poutvec);

        if(outvec.size() < invec.size())
        {
            debug << at(__HERE__) << "resizing outvec from " << outvec.size() 
                  << " to " << invec.size() << endl;
            outvec.resize( invec.size());
        }
        
        for (size_t i=0; i < invec.size(); ++i)
        {
            outvec[i] = sqrt( invec[i]);
        }
        return true;
    } // _sqrt()
} // anonymous::


namespace stdVector
{
    char sqrt__name__[] = "sqrt";
    char sqrt__doc__[] =
    "sqrt( invector, outvector, dtype) -> sqrt input, store in output.\n"
    "Inputs:\n"
    "    invector: std::vector<dtype>\n"
    "    outvector: std::vector<dtype>\n"
    "    dtype: datatype, one of 5....float, 6....double\n"
    "Output:\n"
    "    None\n"
    "Exceptions: ValueError\n"
    "Notes: input and output vectors must be same type.";

    PyObject * sqrrt(PyObject *, PyObject *args)
    {
        journal::debug_t debug("ARCSStdVector");

        int dtype = 0;
        PyObject *pyinvec = 0, *pyoutvec = 0;
        int ok = PyArg_ParseTuple( args, "OOi", &pyinvec, &pyoutvec, &dtype);

        if(!ok)
        {
            debug << at(__HERE__) << "PyArg_ParseTupleFailed, unknown" << endl;
            return 0;
        }

        std::string errstr("stdVector::sqrt");

        bool aok = false;

        switch(dtype)
        {
        case 5: //float
            aok = _sqrt<float>( pyinvec, pyoutvec, dtype, errstr);
            break;
        case 6: //double
            aok = _sqrt<double>( pyinvec, pyoutvec, dtype, errstr);
            break;
        default:
            errstr += "Unrecognized datatype. Recognized datatypes for this "
                "function are:\n"
                "    5......float\n"
                "    6.....double\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        if(aok)
        {
            Py_INCREF( Py_None);
            return Py_None;
        }
        else
        {
            debug << at(__HERE__) << endl;
            return 0;
        }
    }//sqrt()

}   //stdVector::



// version
// $Id: ufuncs.cc 97 2005-07-27 01:54:40Z tim $

// End of file
