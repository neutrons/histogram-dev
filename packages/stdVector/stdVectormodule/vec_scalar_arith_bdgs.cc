// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vec_scalar_arith_bdgs.h"
#include "stdVector/vec_scalar_arith.h"
#include "stdVector/utils.h"
#include <string>
#include "journal/info.h"
#include "journal/debug.h"

using namespace ARCSStdVector;

namespace 
{
//    journal::debug_t debug("ARCSStdVector");
} // anonymous namespace

using journal::at;
using journal::endl;

char pystdVector_add_scalar_vec__name__[] = "add_scalar_vec";
char pystdVector_add_scalar_vec__doc__[] = 
"add_scalar_vec( inputVector, outputVector, input_datatype, scalar)->None\n"
"inputs:\n"
"    inputvector  (PyCObject wrapping vectorWrapper)\n"
"    outputvector  (PyCObject wrapping vectorWrapper)\n"
"    datatype (type of data stored in vectors, same for both; int)\n"
"    scalar (number; MUST BE FLOAT)\n"
"output: None\n"
"Exceptions: ValueError\n";

namespace
{
    template <typename NumT>
    void _callAddScalar( PyObject *pyinvec,
                                PyObject *pyoutvec,
                                NumT scalar, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");

        std::vector<NumT> *pinput = 
            ARCSStdVector::unwrapVector<NumT>( pyinvec, dtype);
        std::vector<NumT> *poutput = 
            ARCSStdVector::unwrapVector<NumT>( pyoutvec, dtype);
        add_scalar_vec<NumT>( *pinput, *poutput, scalar);
        debug << at(__HERE__) << "_callAddScalar complete" << endl;
        return;
    }
}


PyObject * pystdVector_add_scalar_vec(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    PyObject *pyinvec = 0, *pyoutvec = 0;
    int dtype = 0;
    double scalar = 0.0;

    std::string errstr("pyreduction_vectorAddScalar() ");

    debug << at(__HERE__) << errstr << " top" << endl;

    int ok  = PyArg_ParseTuple( args, "OOid", &pyinvec, &pyoutvec, 
                                &dtype, &scalar);
    if(!ok) return 0;

    switch (dtype)
    {
    case 5:   // float
        _callAddScalar<float>( pyinvec, pyoutvec, 
                               static_cast<float>(scalar), dtype);
        break;
    case 6:   // double
        _callAddScalar<double>( pyinvec, pyoutvec, scalar, dtype);
        break;
    case 24:  // int
        _callAddScalar<int>( pyinvec, pyoutvec, static_cast<int>(scalar), 
                             dtype);
 		break;
    case 25:  // unsigned int 
        _callAddScalar<unsigned>( pyinvec,pyoutvec, 
                                  static_cast<unsigned>(scalar), dtype);
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
    Py_INCREF(Py_None);
    debug << at(__HERE__) << " bottom" << endl;
    return Py_None;
}

char pystdVector_mult_scalar_vec__name__[] = "mult_scalar_vec";
char pystdVector_mult_scalar_vec__doc__[] = 
"mult_scalar_vec( inputVector, outputVector, input_datatype, scalar) -> None\n"
"inputs:\n"
"    inputvector  (PyCObject wrapping vectorWrapper)\n"
"    outputvector  (PyCObject wrapping vectorWrapper)\n"
"    datatype (type of data stored in vectors, same for both; int)\n"
"    scalar (number; MUST BE FLOAT)\n"
"output: None\n"
"Exceptions: ValueError\n";


namespace
{
    template <typename NumT>
    void _callMultScalar( PyObject *pyinvec, PyObject *pyoutvec,
                                 NumT scalar, int dtype)
    {
        journal::debug_t debug("ARCSStdVector");

        std::vector<NumT> *pvec = 
            ARCSStdVector::unwrapVector<NumT>( pyinvec, dtype);
        std::vector<NumT> *poutvec = 
            ARCSStdVector::unwrapVector<NumT>( pyoutvec, dtype);
        mult_scalar_vec<NumT>( *pvec, *poutvec, scalar);
        debug << at(__HERE__) << "_callMultScalar complete" << endl;
        return;
    }
}

PyObject * pystdVector_mult_scalar_vec(PyObject *, PyObject *args)
{
    journal::debug_t debug("ARCSStdVector");

    PyObject *pyvec = 0, *pyoutvec = 0;
    int dtype = 0;
    double scalar = 0.0;
    std::string errstr("pyreduction_vectorAddScalar() ");
    debug << at(__HERE__) << errstr << " top" << endl;
    
    int ok  = PyArg_ParseTuple( args, "OOid", &pyvec, &pyoutvec, 
                                &dtype, &scalar);
    if(!ok) return 0;

    switch (dtype)
    {
    case 5:   // float
        _callMultScalar<float>( pyvec, pyoutvec, static_cast<float>(scalar), 
                                dtype);
        break;
    case 6:   // double
        _callMultScalar<double>( pyvec, pyoutvec, scalar, dtype);
        break;
    case 24:  // int
        _callMultScalar<int>( pyvec, pyoutvec, static_cast<int>(scalar), dtype);
 		break;
    case 25:  // unsigned int 
        _callMultScalar<unsigned>( pyvec, pyoutvec, 
                                   static_cast<unsigned>(scalar), dtype);
 		break;
    default:
        errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
            "          float....5\n"
            "          double...6\n"
            "          int........24\n"
            "          unsigned...25\n";
        debug << at(__HERE__) << errstr;
        debug.newline();
        debug << "Datatype = " << dtype << endl;
        PyErr_SetString( PyExc_ValueError, errstr.c_str());
        return 0;
    }
    Py_INCREF(Py_None);
    debug << at(__HERE__) << errstr << " bottom" << endl;
    return Py_None;	
}
// version
// $Id: vec_scalar_arith_bdgs.cc 85 2005-06-17 16:54:43Z tim $

// End of file
