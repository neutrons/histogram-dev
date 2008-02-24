// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef ARCSSLICE_H
#define ARCSSLICE_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif
#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif
// valarray included for std::slice
#ifndef VALARRAY_INCLUDED
#define VALARRAY_INCLUDED
#include <valarray>
#endif

namespace ARCSStdVector
{
    template <typename NumT>
    void extractSlice( std::vector<NumT> const & source,
                       std::vector<NumT> & target,
                       std::slice const & slice);
}

// include template function bodies, no instantiations!
#define ARCSSLICE_ICC
#include "slice.icc"
#undef ARCSSLICE_ICC

#endif // include guard

// version
// $Id: slice.h 84 2005-06-17 16:49:36Z tim $

// End of file
