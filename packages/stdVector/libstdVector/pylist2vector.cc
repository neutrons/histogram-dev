// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "pylist2vector.h"
//#include "journal/debug.h"

namespace
{
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

} // anonymous::

namespace ARCSStdVector
{
    template <typename NumT>
    void pylist2vector( PyObject *pylist, std::vector<NumT> &vec)
    {
        size_t len = (size_t) PyList_Size( pylist);
        if( vec.size() != len) vec.resize(len);

        for(size_t i=0; i<len; ++i)
        {
            PyObject *pynum = PyList_GetItem( pylist, i);
            NumT num = _convertPyNum<NumT>( pynum);
            vec[i] = num;
        }
        return;
    } // PyObject *_list2NewVec( ...

    template void pylist2vector( PyObject *, std::vector<double> &);
    template void pylist2vector( PyObject *, std::vector<float> &);
    template void pylist2vector( PyObject *, std::vector<int> &);
    template void pylist2vector( PyObject *, std::vector<unsigned> &);

} // ARCSStdVector::

// version
// $Id: pylist2vector.cc 2 2004-10-01 18:15:11Z tim $

// End of file
