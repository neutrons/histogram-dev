// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vector2pylist.h"
#include "journal/debug.h"

namespace
{
//    journal::debug_t debug("stdVector");
    using journal::at;
    using journal::endl;


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

} // anonymous::


namespace ARCSStdVector
{
    //------------------ Load vector -> Python list ---------------------
    template <typename NumT>
    PyObject *vec2NewList( std::vector<NumT> const &vec, 
                           std::string & errstr)
    {
        journal::debug_t debug("stdVector");

        size_t len = vec.size();
        PyObject *pylist = PyList_New( (int)len);

        int ok = 0;
        for( size_t i=0; i<len; ++i)
        {
            ok = PyList_SetItem( pylist, i, _convertNum<NumT>(vec[i]));
            if( ok != 0)
            {
                errstr += "unknown problem loading list in _vec2NewList";
                debug << at(__HERE__) << errstr << endl;
                return 0;
            }
        }
        return pylist;
    }// PyObject *vec2NewList( ...

    template PyObject *vec2NewList(std::vector<double> const &, std::string &);
    template PyObject *vec2NewList(std::vector<float> const &, std::string &);
    template PyObject *vec2NewList(std::vector<int> const &, std::string &);
    template PyObject *vec2NewList(std::vector<unsigned> const &, std::string &);
    
} // ARCSStdVector::

// version
// $Id: vector2pylist.cc 45 2005-04-05 23:14:26Z tim $

// End of file
