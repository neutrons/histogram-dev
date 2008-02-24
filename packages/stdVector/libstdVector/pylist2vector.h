// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef PYLIST2VECTOR_H
#define PYLIST2VECTOR_H

#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace ARCSStdVector
{
    /// Load a Python list into a std::vector< NumT>. 
    /// Explicit instantiations for double, float, int, unsigned.
    template <typename NumT>
    void pylist2vector( PyObject *pylist, std::vector<NumT> &vec);
} // ARCSStdVector::


#endif



// version
// $Id: pylist2vector.h 2 2004-10-01 18:15:11Z tim $

// End of file
