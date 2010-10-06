// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vec_vec_arith_bdgs.h"
#include "stdVector/vec_vec_arith.h"
#include "stdVector/utils.h"
#include <string>
#include "journal/info.h"
#include "journal/debug.h"

using namespace ARCSStdVector;

namespace 
{
//    journal::debug_t debug("ARCSStdVector");
    using journal::at;
    using journal::endl;

} // anonymous namespace

namespace stdVector
{

    char vectorPlusEquals__name__[] = "vectorPlusEquals";
    char vectorPlusEquals__doc__[] = 
    "vectorPlusEquals( rhs_vector, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Add rhs_vector[start_rhs:end_rhs) to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs))\n"
    "inputs:\n"
    "    rhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "3) LHS and RHS vectors must be same type."
    "is myVector[b-1]\n";

    namespace
    {
        template <typename NumT>
        void _callVecPlusEqual( PyObject *pyrhs,
                                PyObject *pylhs,
                                size_t start_rhs,
                                size_t end_rhs,
                                size_t start_lhs, 
                                int dtype)
        {
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);
            vec_plusEquals<NumT>( *prhs, start_rhs, end_rhs, *plhs, start_lhs);
            debug << at(__HERE__) << "_callVecPlusEquals complete" << endl;
            return;
        }
    }


    PyObject * vectorPlusEquals(PyObject *, PyObject *args)
    {
        journal::debug_t debug("ARCSStdVector");

        PyObject *pyrhs = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;

        std::string errstr("pyreduction_vectorPlusEquals() ");

//     debug << at(__HERE__) << errstr << " top" << endl;

        int ok = PyArg_ParseTuple( args, "OiOiii", &pyrhs, &dtype, &pylhs,
                                   &sstart_rhs, &send_rhs, &sstart_lhs);
        if(!ok) return 0;

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        switch (dtype)
        {
        case 5:   // float
            _callVecPlusEqual<float>( pyrhs, pylhs, start_rhs, end_rhs, 
                                      start_lhs, dtype);
            break;
        case 6:   // double
            _callVecPlusEqual<double>( pyrhs, pylhs, start_rhs, end_rhs, 
                                       start_lhs, dtype);
            break;
        case 24:  // int
            _callVecPlusEqual<int>( pyrhs, pylhs, start_rhs, end_rhs, 
                                    start_lhs, dtype);
            break;
        case 25:  // unsigned int 
            _callVecPlusEqual<unsigned>( pyrhs,pylhs, start_rhs, end_rhs, 
                                         start_lhs, dtype);
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
    } // vectorPlusEquals( ...)


// //========================== minusEquals ==========================
    namespace 
    {
        template <typename NumT>
        void _callVecMinusEquals( PyObject *pyrhs, 
                                  PyObject *pylhs,
                                  int dtype,
                                  size_t start_rhs,
                                  size_t end_rhs,
                                  size_t start_lhs)
        {
            std::vector<NumT> *prhs = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);
            ARCSStdVector::vec_minusEquals( *prhs, start_rhs, end_rhs, *plhs, 
                                            start_lhs);
            return;
        } 
    }// anonymous::

    char vectorMinusEquals__name__[] = "vectorMinusEquals";
    char vectorMinusEquals__doc__[] =
    "vectorMinusEquals( rhs_vector, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Subtract rhs_vector[start_rhs:end_rhs) from lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs))\n"
    "inputs:\n"
    "    rhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";



    PyObject * vectorMinusEquals(PyObject *, PyObject *args)
    {

        PyObject *pyrhs = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OiOiii", &pyrhs, &dtype, &pylhs,
                                   &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("pyreduction_vectorMinusEquals() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);
        switch( dtype)
        {
        case 5:   // float
            _callVecMinusEquals<float> ( pyrhs, pylhs, dtype, start_rhs, 
                                         end_rhs, start_lhs);
            break;
        case 6:   // double
            _callVecMinusEquals<double>( pyrhs, pylhs, dtype, start_rhs, 
                                         end_rhs, start_lhs);
            break;
        case 24:  // int
            _callVecMinusEquals<int>( pyrhs, pylhs, dtype, start_rhs, 
                                      end_rhs, start_lhs);
            break;
        case 25:  // unsigned int 
            _callVecMinusEquals<unsigned>( pyrhs, pylhs, dtype, start_rhs, 
                                           end_rhs, start_lhs);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        Py_INCREF(Py_None);
        return Py_None;	
    } // vectorMinusEquals( ...)


    //----------------------------- times equals --------------------------------
    namespace
    {
        template <typename NumT>
        void _callVecTimesEquals( PyObject *pyrhs, 
                                  PyObject *pylhs,
                                  size_t start_rhs,
                                  size_t end_rhs,
                                  size_t start_lhs,
                                  int dtype)
        {
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);
            ARCSStdVector::vec_timesEquals( *prhs, start_rhs, end_rhs, *plhs, 
                                            start_lhs);
            debug << at(__HERE__) << "_callVecTimesEquals complete" << endl;
            return;
        }
    } // anonymous::


    char vectorTimesEquals__name__[] = "vectorTimesEquals";
    char vectorTimesEquals__doc__[] = 
    "vectorTimesEquals( rhs_vector, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Multiply  lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)) by rhs_vector[start_rhs:end_rhs)\n"
    "inputs:\n"
    "    rhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";

    PyObject * vectorTimesEquals(PyObject *, PyObject *args)
    {
        PyObject *pyrhs = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OiOiii", &pyrhs, &dtype, &pylhs,
                                   &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("pyreduction_vectorTimesEquals() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        switch( dtype)
        {
        case 5:   // float
            _callVecTimesEquals<float> ( pyrhs, pylhs, start_rhs, end_rhs, 
                                         start_lhs, dtype);
            break;
        case 6:   // double
            _callVecTimesEquals<double>( pyrhs, pylhs, start_rhs, end_rhs, 
                                         start_lhs, dtype);
            break;
        case 24:  // int
            _callVecTimesEquals<int>( pyrhs, pylhs, start_rhs, end_rhs, start_lhs, 
                                      dtype);
            break;
        case 25:  // unsigned int 
            _callVecTimesEquals<unsigned int>( pyrhs, pylhs, start_rhs, end_rhs, 
                                               start_lhs, dtype);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        Py_INCREF(Py_None);
        return Py_None;	
    } // timesEquals( ...)


//----------------------------- divide equals -----------------------------
    namespace 
    {
        template <typename NumT>
        void _callVecDivideEquals( PyObject *pyrhs, 
                                   PyObject *pylhs,
                                   size_t start_rhs,
                                   size_t end_rhs,
                                   size_t start_lhs, 
                                   int dtype)
        {    
            std::vector<NumT> *prhs = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);
            ARCSStdVector::vec_divideEquals( *prhs, start_rhs, end_rhs, 
                                             *plhs, start_lhs);
            return;
        }
    } // anonymous::

    char vectorDivideEquals__name__[] = "vectorDivideEquals";
    char vectorDivideEquals__doc__[] = 
    "vectorDivideEquals( rhs_vector, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Divide lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)) by rhs_vector[start_rhs:end_rhs)\n"
    "inputs:\n"
    "    rhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";

    PyObject * vectorDivideEquals(PyObject *, PyObject *args)
    {
        PyObject *pyrhs = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OiOiii", &pyrhs, &dtype, &pylhs,
                                   &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("vectorDivideEquals() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);
        switch( dtype)
        {
        case 5:   // float
            _callVecDivideEquals<float> ( pyrhs, pylhs, start_rhs, end_rhs, start_lhs, dtype);
            break;
        case 6:   // double
            _callVecDivideEquals<double>( pyrhs, pylhs, start_rhs, end_rhs, start_lhs, dtype);
            break;
        case 24:  // int
            _callVecDivideEquals<int>( pyrhs, pylhs, start_rhs, end_rhs, start_lhs, dtype);
            break;
        case 25:  // unsigned int 
            _callVecDivideEquals<unsigned int>( pyrhs, pylhs, start_rhs, end_rhs, start_lhs, dtype);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        Py_INCREF(Py_None);
        return Py_None;	
    }


//---------------------------- straight arithmetic ------------------------------


    //--------------------------------- plus --------------------------------

    char vectorPlus__name__[] = "vectorPlus";
    char vectorPlus__doc__[] = 
    "vectorPlus( rhs_vector1, rhs_vector2, lhs_vector, datatype, start_rhs, end_rhs, startlhs) --> None\n"
    "Add rhs_vector1[start_rhs:end_rhs) to rhs_vector2[start_rhs:end_rhs), \n"
    "assigning to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs))\n"
    "inputs:\n"
    "    rhs_vector1 (std::vector<datatype>, PyCObject)\n"
    "    rhs_vector2 (std::vector<datatype>, PyCObject)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last is \n"
    "myVector[b-1]\n"
    "3) LHS and RHS vectors must be same type.";

    namespace
    {
        template <typename NumT>
        bool _callVecPlus( PyObject *pyrhs1,
                           PyObject *pyrhs2,
                           PyObject *pylhs,
                           size_t start_rhs,
                           size_t end_rhs,
                           size_t start_lhs, 
                           int dtype)
        {
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs1 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs1, dtype);
            std::vector<NumT> *prhs2 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs2, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);

            if(prhs1 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs1 vector" << endl;
                return false;
            }
            if(prhs2 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs2 vector" << endl;
                return false;
            }
            if(plhs == 0)
            {
                debug << at(__HERE__) << "failed to unwrap lhs vector" << endl;
                return false;
            }

            try
            {
                vec_plus<NumT>( *prhs1, *prhs2, start_rhs, end_rhs, *plhs, start_lhs);
            }

            catch( std::string &errstr)
            {
                debug << at(__HERE__) << "Caught exception from libstdVector: "
                      << errstr << endl;
                errstr += " Caught in _callVecPlus()";
                PyErr_SetString( PyExc_IndexError, errstr.c_str());
                return false;
            }
            debug << at(__HERE__) << "_callVecPlus complete" << endl;

            return true;
        } // _callVecPlus(...)
    } // anonymous::


    PyObject * vectorPlus(PyObject *, PyObject *args)
    {
        journal::debug_t debug("ARCSStdVector");

        PyObject *pyrhs1 = 0, *pyrhs2 = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;

        std::string errstr("pyreduction_vectorPlus() ");

//     debug << at(__HERE__) << errstr << " top" << endl;

        int ok = PyArg_ParseTuple( args, "OOOiiii", &pyrhs1, &pyrhs2, &pylhs,
                                   &dtype, &sstart_rhs, &send_rhs, &sstart_lhs);
        if(!ok) return 0;

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        bool okay = true;

        switch (dtype)
        {
        case 5:   // float
            okay = _callVecPlus<float>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                        end_rhs, start_lhs, dtype);
            break;
        case 6:   // double
            okay = _callVecPlus<double>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                         end_rhs, start_lhs, dtype);
            break;
        case 24:  // int
            okay = _callVecPlus<int>( pyrhs1, pyrhs2, pylhs, start_rhs, end_rhs, 
                                      start_lhs, dtype);
            break;
        case 25:  // unsigned int 
            okay = _callVecPlus<unsigned>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                           end_rhs, start_lhs, dtype);
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
        }  // switch

        if(!okay) return 0; // exception context set in _callVecPlus<T>

        debug << at(__HERE__) << " bottom" << endl;

        Py_INCREF(Py_None);
        return Py_None;
    } // vectorPlus( ...)


    //--------------------------------- minus ----------------------------------
    namespace 
    {
        template <typename NumT>
        bool _callVecMinus( PyObject *pyrhs1, 
                            PyObject *pyrhs2, 
                            PyObject *pylhs,
                            int dtype,
                            size_t start_rhs,
                            size_t end_rhs,
                            size_t start_lhs)
        {
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs1 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs1, dtype);
            std::vector<NumT> *prhs2 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs2, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);

            if(prhs1 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs1 vector" << endl;
                return false;
            }
            if(prhs2 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs2 vector" << endl;
                return false;
            }
            if(plhs == 0)
            {
                debug << at(__HERE__) << "failed to unwrap lhs vector" << endl;
                return false;
            }

            try
            {
                ARCSStdVector::vec_minus( *prhs1, *prhs2, start_rhs, end_rhs, 
                                          *plhs, start_lhs);
            }
            catch( std::string &errstr)
            {
                debug << at(__HERE__) << "Caught exception from libstdVector: "
                      << errstr << endl;
                errstr += " Caught in _callVecMinus()";
                PyErr_SetString( PyExc_IndexError, errstr.c_str());
                return false;
            }
            debug << at(__HERE__) << "_callVecMinus complete" << endl;

            return true;
        }
 
    }// anonymous::

    char vectorMinus__name__[] = "vectorMinus";
    char vectorMinus__doc__[] =
    "vectorMinus( rhs_vector1, rhs_vector2, lhs_vector, datatype, start_rhs, end_rhs, startlhs) --> None\n"
    "Subtract rhs_vector1[start_rhs:end_rhs) from rhs_vector2[start_rh:end_rh)\n"
    "storing in lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs))\n"
    "inputs:\n"
    "    rhs_vector1 (std::vector<datatype>, PyCObject)\n"
    "    rhs_vector2 (std::vector<datatype>, PyCObject)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";



    PyObject * vectorMinus(PyObject *, PyObject *args)
    {

        PyObject *pyrhs1 = 0, *pyrhs2 = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OOOiiii", &pyrhs1, &pyrhs2, &pylhs, 
                                   &dtype, &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("pyreduction_vectorMinus() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        bool okay = true;
        
        switch( dtype)
        {
        case 5:   // float
            okay = _callVecMinus<float> ( pyrhs1, pyrhs2, pylhs, dtype, 
                                          start_rhs, end_rhs, start_lhs);
            break;
        case 6:   // double
            okay = _callVecMinus<double>( pyrhs1, pyrhs2, pylhs, dtype, 
                                          start_rhs, end_rhs, start_lhs);
            break;
        case 24:  // int
            okay = _callVecMinus<int>( pyrhs1, pyrhs2, pylhs, dtype, 
                                       start_rhs, end_rhs, start_lhs);
            break;
        case 25:  // unsigned int 
            okay = _callVecMinus<unsigned>( pyrhs1, pyrhs2, pylhs, dtype, 
                                            start_rhs, end_rhs, start_lhs);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        
        if(!okay) return 0;  // exception context set in _callVecMinus
        
        Py_INCREF(Py_None);
        return Py_None;	
    } // vectorMinus( ...)


    //--------------------------------- times -----------------------------------

    namespace
    {
        template <typename NumT>
        bool _callVecTimes( PyObject *pyrhs1, 
                            PyObject *pyrhs2, 
                            PyObject *pylhs,
                            size_t start_rhs,
                            size_t end_rhs,
                            size_t start_lhs,
                            int dtype)
        {
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs1 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs1, dtype);
            std::vector<NumT> *prhs2 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs2, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);

            if(prhs1 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs1 vector" << endl;
                return false;
            }
            if(prhs2 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs2 vector" << endl;
                return false;
            }
            if(plhs == 0)
            {
                debug << at(__HERE__) << "failed to unwrap lhs vector" << endl;
                return false;
            }

            try
            {
                ARCSStdVector::vec_times( *prhs1, *prhs2, start_rhs, end_rhs, 
                                          *plhs, start_lhs);
            }

            catch( std::string &errstr)
            {
                debug << at(__HERE__) << "Caught exception from libstdVector: "
                      << errstr << endl;
                errstr += " Caught in _callVecTimes()";
                PyErr_SetString( PyExc_IndexError, errstr.c_str());
                return false;
            }
            debug << at(__HERE__) << "_callVecTimes complete" << endl;

            return true;
        }  // _callVecTimes(...)

    } // anonymous::


    char vectorTimes__name__[] = "vectorTimes";
    char vectorTimes__doc__[] = 
    "vectorTimes( rhs_vector1, rhs_vector2, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Multiply rhs_vector2[start_rhs:end_rhs) by rhs_vector1[start_rhs:end_rhs)\n"
    "store result in lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs))\n."
    "inputs:\n"
    "    rhs_vector1 (std::vector<datatype>, PyCObject)\n"
    "    rhs_vector2 (std::vector<datatype>, PyCObject)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";

    PyObject * vectorTimes(PyObject *, PyObject *args)
    {
        PyObject *pyrhs1 = 0, *pyrhs2 = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OOOiiii", &pyrhs1, &pyrhs2, &pylhs, 
                                   &dtype, &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("pyreduction_vectorTimes() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        bool okay = true;

        switch( dtype)
        {
        case 5:   // float
            okay = _callVecTimes<float> ( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                          end_rhs, start_lhs, dtype);
            break;
        case 6:   // double
            okay = _callVecTimes<double>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                          end_rhs, start_lhs, dtype);
            break;
        case 24:  // int
            okay = _callVecTimes<int>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                       end_rhs, start_lhs, dtype);
            break;
        case 25:  // unsigned int 
            okay = _callVecTimes<unsigned>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                            end_rhs, start_lhs, dtype);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        Py_INCREF(Py_None);
        return Py_None;	
    } // times( ...)


//----------------------------- divide  -----------------------------
    namespace 
    {
        template <typename NumT>
        bool _callVecDivide( PyObject *pyrhs1, 
                             PyObject *pyrhs2,
                             PyObject *pylhs,
                             size_t start_rhs,
                             size_t end_rhs,
                             size_t start_lhs, 
                             int dtype)
        {    
            journal::debug_t debug("ARCSStdVector");

            std::vector<NumT> *prhs1 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs1, dtype);
            std::vector<NumT> *prhs2 = 
                ARCSStdVector::unwrapVector<NumT>( pyrhs2, dtype);
            std::vector<NumT> *plhs = 
                ARCSStdVector::unwrapVector<NumT>( pylhs, dtype);

            if(prhs1 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs1 vector" << endl;
                return false;
            }
            if(prhs2 == 0)
            {
                debug << at(__HERE__) << "failed to unwrap rhs2 vector" << endl;
                return false;
            }
            if(plhs == 0)
            {
                debug << at(__HERE__) << "failed to unwrap lhs vector" << endl;
                return false;
            }
            try
            {
                ARCSStdVector::vec_divide( *prhs1, *prhs2, start_rhs, end_rhs, 
                                           *plhs, start_lhs);
            }
            catch( std::string &errstr)
            {
                debug << at(__HERE__) << "Caught exception from libstdVector: "
                      << errstr << endl;
                errstr += " Caught in _callVecTimes()";
                PyErr_SetString( PyExc_IndexError, errstr.c_str());
                return false;
            }

            debug << at(__HERE__) << "_callVecDivide complete" << endl;

            return true;
        }
    } // anonymous::

    char vectorDivide__name__[] = "vectorDivide";
    char vectorDivide__doc__[] = 
    "vectorDivide( rhs_vector, datatype, lhs_vector, start_rhs, end_rhs, startlhs) --> None\n"
    "Divide lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)) by rhs_vector[start_rhs:end_rhs)\n"
    "inputs:\n"
    "    rhs_vector (std::vector<datatype>, PyCObject)\n"
    "    datatype (int, see below for supported types)\n"
    "    lhs_vector (std::vector<datatype>, PyCObject)\n"
    "    start_rhs (start of rhs range)\n"
    "    end_rhs   (one-past the end of the rhs range)\n"
    "    start_lhs (start of lhs range)\n"
    "outputs: None\n"
    "Exceptions: ValueError, IndexError\n"
    "Notes:\n"
    "1) Supported datatype:\n"
    "      float...........5\n"
    "      double..........6\n"
    "      int............24\n"
    "      unsigned int...25\n"
    "2) Read myVector[a:b) as first in range is myVector[a], last included"
    "is myVector[b-1]\n";

    PyObject * vectorDivide(PyObject *, PyObject *args)
    {
        PyObject *pyrhs1 = 0, *pyrhs2 = 0, *pylhs = 0;
        int dtype = 0, sstart_rhs = 0, send_rhs = 0, sstart_lhs = 0;
        int ok = PyArg_ParseTuple( args, "OOOiiii", &pyrhs1, &pyrhs2, &pylhs, 
                                   &dtype, &sstart_rhs, &send_rhs, &sstart_lhs);
        if (!ok) return 0;
    
        std::string errstr("vectorDivide() ");

        if( sstart_rhs < 0 )
        {
            errstr += "start_rhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (send_rhs <= sstart_rhs)
        {
            errstr += "end_rhs <= start_rhs";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        if (sstart_lhs < 0)
        {
            errstr += "start_lhs < 0";
            PyErr_SetString( PyExc_IndexError, errstr.c_str());
            return 0;
        }
        size_t start_rhs = static_cast< size_t>( sstart_rhs);
        size_t end_rhs = static_cast< size_t>( send_rhs);
        size_t start_lhs = static_cast< size_t>( sstart_lhs);

        bool okay = true;

        switch( dtype)
        {
        case 5:   // float
            okay = _callVecDivide<float> ( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                           end_rhs, start_lhs, dtype);
            break;
        case 6:   // double
            okay = _callVecDivide<double>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                           end_rhs, start_lhs, dtype);
            break;
        case 24:  // int
            okay = _callVecDivide<int>( pyrhs1, pyrhs2, pylhs, start_rhs, 
                                        end_rhs, start_lhs, dtype);
            break;
        case 25:  // unsigned int 
            okay = _callVecDivide<unsigned>( pyrhs1, pyrhs2, pylhs,
                                             start_rhs, end_rhs, start_lhs, dtype);
            break;
        default:
            errstr += "unrecognized or unallowed datatype. Allowed datatypes:\n"
                "      float....5\n"
                "      double...6\n"
                "      int............24\n"
                "      unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }

        if(!okay) return 0;

        Py_INCREF(Py_None);
        return Py_None;	
    }


} // stdVector::


// version
// $Id: vec_vec_arith_bdgs.cc 85 2005-06-17 16:54:43Z tim $

// End of file
