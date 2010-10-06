// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef VECTOR2PYLIST_H
#define VECTOR2PYLIST_H

#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif
#ifndef STRING_INCLUDED
#define STRING_INCLUDED
#include <string>
#endif
#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif


namespace ARCSStdVector
{
    /// Convert a std::vector< NumT> to a Python list. User must check
    /// for non-NULL pointer. NULL pointer means conversion FAILED,
    /// check errstr.
    /// Explicit instantiations for double, float, int, unsigned.

    template <typename NumT>
    PyObject *vec2NewList( std::vector<NumT> const &vec, 
                           std::string & errstr);

} // ARCSStdVector::


#endif



// version
// $Id: vector2pylist.h 35 2005-01-28 01:03:18Z tim $

// End of file
