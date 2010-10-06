// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "iterators.h"
#include "stdVector/utils.h"
#include <string>
#include "journal/info.h"
#include "journal/debug.h"

namespace 
{
//    journal::debug_t debug("ARCSStdVector");
    using journal::at;
    using journal::endl;
} // anonymous namespace

char pystdVector_iterator__name__[] = "iterator";
char pystdVector_iterator__doc__[] = 
"vector_iterator( vector, datatype, offset) -> new vector_iterator\n"
"inputs: \n"
"    vectorWrapper (PyCObject)\n"
"    datatype (integer, one of the following recognized codes:\n"
"        float...........5\n"
"        double..........6\n"
"        int.........24\n"
"        unsigned....25\n"
"    offset (location in the vector at which you'd like the iterator\n"
"output: vectorIteratorWrapper object, wrapped in PyCObject\n"
"Exceptions: TypeError, ValueError\n";

namespace 
{
    template <typename NumT, typename Iterator>
    PyObject *fetchIterator( PyObject *pyvec, int dtype, size_t offset)
    {
        journal::debug_t debug("ARCSStdVector");
        
        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);

        debug << at(__HERE__) << __FUNCTION__ << " after unwrapVector" << endl;

        Iterator *pit = new Iterator( pvec -> begin());
        (*pit) += offset;

        debug << at(__HERE__) << __FUNCTION__ << "about to return" << endl;

        return ARCSStdVector::wrapIterator( pit, dtype);
    }
} // anonymous::


PyObject * pystdVector_iterator(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    std::string errstr("pystdVector_vector_iterator() ");

    PyObject *pyvec = 0;
    int dtype = 0, soffset = 0;
    int ok = PyArg_ParseTuple( args, "Oii", &pyvec, &dtype, &soffset);
    if (!ok) return 0;

    if( soffset < 0)
    {
        errstr += "offset must be >= 0";
        PyErr_SetString( PyExc_IndexError, errstr.c_str());
        return 0;
    }
    size_t offset = static_cast<size_t>( soffset);

    switch( dtype)
    {
    case 5: // float
        return fetchIterator<float, std::vector<float>::iterator>( 
            pyvec, dtype, offset);
        break;
    case 6:   // double
        return fetchIterator<double, std::vector<double>::iterator>( 
            pyvec, dtype, offset);
        break;
    case 24:  // int
        return fetchIterator<int, std::vector<int>::iterator>( 
            pyvec, dtype, offset);
        break;
    case 25:  // unsigned
        return fetchIterator<unsigned, std::vector<unsigned>::iterator>( 
            pyvec, dtype, offset);
        break;
    default:
        errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
            "          float.......5\n"
            "          double......6\n"
            "          int........24\n"
            "          unsigned...25\n";
        debug << at(__HERE__) << errstr;
        debug.newline();
        debug << "Datatype = " << dtype << endl;

        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }
    errstr += "Reached \"unreachable\" segment!!!";
    PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
    return 0;
} // pystdVector_iterator::

//================================ begin ==================================
namespace 
{
    template <typename VecNumTIt, typename NumT>
    PyObject * _callBegin( PyObject *pyvec, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");
        
        debug << at(__HERE__) << "before unwrapVector" << endl;

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        
        debug << at(__HERE__) << "after unwrap" << endl;

        VecNumTIt *pit = new VecNumTIt( pvec->begin());

        debug << at(__HERE__) << "Address of pointer to it: " 
              << pit << endl;

        debug << "Value at pvec->begin(): " << **pit << endl;

        return ARCSStdVector::wrapIterator( pit, dtype);//wrapIterator
    } //_callBegin
}// anonymous::

char pystdVector_begin__name__[] = "begin";
char pystdVector_begin__doc__[] = 
"begin( vector, datatype) --> StdVectorIterator\n"
"Invokes std::vector::begin on the vector\n"
"inputs:\n"
"    vector ..(PyCObject/void ptr to vector object)\n"
"    datatype (type of data stored in vector; int)\n"
"output: StdVectorIterator instance wrapping PyCObject w/ void pointer to iterator at beginning of vector\n"
"Exceptions: ValueError";


PyObject * pystdVector_begin(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    std::string errstr("pystdVector_begin() ");

    PyObject *pyvec = 0;
    int dtype = 0;

    int ok = PyArg_ParseTuple( args, "Oi", &pyvec, &dtype);
    if (!ok) return 0;

    switch( dtype)
    {
    case 5:  // float
        return 
            _callBegin<std::vector<float>::iterator, float>( pyvec, dtype);
        break;
    case 6:  // double
        return _callBegin<std::vector<double>::iterator, double>( pyvec, dtype);
        break;
    case 24:  // int
        return _callBegin<std::vector<int>::iterator, int>( pyvec, dtype);
        break;
    case 25:  // unsigned
        return _callBegin<std::vector<unsigned>::iterator, unsigned>( pyvec, dtype);
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

    errstr += "WARNING: REACHED \"UNREACHABLE\" CODE";
    PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
    return 0;
} // pystdVector_begin(...)

//============================== end =================================
namespace 
{
    template <typename VecNumTIt, typename NumT>
    PyObject * _callEnd( PyObject *pyvec, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");
        
        debug << at(__HERE__) << "before unwrapVector" << endl;

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyvec, dtype);
        
        debug << at(__HERE__) << "after unwrap" << endl;

        VecNumTIt *pit = new VecNumTIt( pvec->end());

        return ARCSStdVector::wrapIterator( pit, dtype);//wrapIterator
    } //_callEnd
}// anonymous::

char pystdVector_end__name__[] = "end";
char pystdVector_end__doc__[] = 
"end( vector, datatype) --> StdVectorIterator\n"
"Invokes std::vector::end on the vector\n"
"inputs:\n"
"    vector ..(PyCObject/void ptr to vector object)\n"
"    datatype (type of data stored in vector; int)\n"
"output: StdVectorIterator instance wrapping PyCObject w/ void pointer to "
"    iterator at ending of vector\n"
"Exceptions: ValueError";


PyObject * pystdVector_end(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    std::string errstr("pystdVector_end() ");

    PyObject *pyvec = 0;
    int dtype = 0;

    int ok = PyArg_ParseTuple( args, "Oi", &pyvec, &dtype);
    if (!ok) return 0;

    switch( dtype)
    {
    case 5:  // float
        return _callEnd<std::vector<float>::iterator, float>( pyvec, dtype);
        break;
    case 6:  // double
        return _callEnd<std::vector<double>::iterator, double>( pyvec, dtype);
        break;
    case 24:  // int
        return _callEnd<std::vector<int>::iterator, int>( pyvec, dtype);
        break;
    case 25:  // unsigned
        return _callEnd<std::vector<unsigned>::iterator, unsigned>( pyvec, dtype);
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


    errstr += "WARNING: REACHED \"UNREACHABLE\" CODE";
    PyErr_SetString( PyExc_RuntimeError, errstr.c_str());
    return 0;
} // pystdVector_end(...)


//============================== equal =================================
namespace 
{
    template <typename VecNumTIt, typename NumT>
    bool _callEqual( PyObject *pyit1, PyObject *pyit2, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");
        
        debug << at(__HERE__) << "before unwrapVector" << endl;

        VecNumTIt *pit1 = 
            ARCSStdVector::unwrapIterator<VecNumTIt>( pyit1, dtype);
        
        VecNumTIt *pit2 = 
            ARCSStdVector::unwrapIterator<VecNumTIt>( pyit2, dtype);
        
        debug << at(__HERE__) << "after unwrap" << endl;

        return *pit1 == *pit2;
    } //_callEnd
}// anonymous::

char pystdVector_iteratorEqual__name__[] = "iteratorsEqual";
char pystdVector_iteratorEqual__doc__[] = 
"iteratorsEqual( StdVectorIterator1, StdVectorIterator2, datatype) --> 1 or 0\n"
"Invokes == on the two iterators\n"
"inputs:\n"
"    StdVectorIterator1 .. (PyCObject/void ptr to iterator object)\n"
"    StdVectorIterator2 .. (PyCObject/void ptr to iterator object)\n"
"    datatype ............ (type of data stored in vector; int)\n"
"output: 0 if false, 1 if true\n"
"Exceptions: ValueError";


PyObject * pystdVector_iteratorEqual(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    std::string errstr("pystdVector_iteratorsEqual() ");

    PyObject *pyit1 = 0, *pyit2 = 0;
    int dtype = 0;

    int ok = PyArg_ParseTuple( args, "OOi", &pyit1, &pyit2, &dtype);
    if (!ok) return 0;

    bool isEqual = false;

    switch( dtype)
    {
    case 5:  // float
        isEqual = _callEqual<std::vector<float>::iterator, float>( 
            pyit1, pyit2, dtype);
        break;
    case 6:  // double
        isEqual = _callEqual<std::vector<double>::iterator, double>( 
            pyit1, pyit2, dtype);
        break;
    case 24:  // int
        isEqual = _callEqual<std::vector<int>::iterator, int>( 
            pyit1, pyit2, dtype);
        break;
    case 25:  // unsigned
        isEqual = _callEqual<std::vector<unsigned>::iterator, unsigned>( 
            pyit1, pyit2, dtype);
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
    return isEqual ? Py_BuildValue( "i", 1) :  Py_BuildValue( "i", 0);
} // equal


//============================== increment ===============================
namespace 
{
    template <typename VecNumTIt, typename NumT>
    void _callIncrement( PyObject *pyit, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");
        
        debug << at(__HERE__) << "before unwrapVector" << endl;

        VecNumTIt *pit = 
            ARCSStdVector::unwrapIterator<VecNumTIt>( pyit, dtype);
        (*pit)++;
        return;
    } 
}// anonymous::

char pystdVector_increment__name__[] = "increment";
char pystdVector_increment__doc__[] = 
"increment( StdVectorIterator, datatype)->None\n"
"Increment your iterator\n"
"inputs:\n"
"    StdVectorIterator .. (PyCObject/void ptr to iterator object)\n"
"    datatype ............ (type of data stored in vector; int)\n"
"output: None\n"
"Exceptions: ValueError";


PyObject * pystdVector_increment(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    std::string errstr("pystdVector_iteratorsIncrement() ");

    PyObject *pyit = 0;
    int dtype = 0;

    int ok = PyArg_ParseTuple( args, "Oi", &pyit, &dtype);
    if (!ok) return 0;

    switch( dtype)
    {
    case 5:  // float
        _callIncrement<std::vector<float>::iterator, float>( pyit, dtype);
        break;
    case 6:  // double
        _callIncrement<std::vector<double>::iterator,double>( pyit, dtype);
        break;
    case 24:  // int
        _callIncrement<std::vector<int>::iterator, int>( pyit, dtype);
        break;
    case 25:  // unsigned
        _callIncrement<std::vector<unsigned>::iterator, unsigned>( 
            pyit, dtype);
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
    Py_INCREF(Py_None);
    return Py_None;
} // increment



// version
// $Id: iterators.cc 85 2005-06-17 16:54:43Z tim $

// End of file
