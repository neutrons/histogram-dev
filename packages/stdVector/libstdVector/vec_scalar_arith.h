// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef VEC_SCALAR_ARITH_H
#define VEC_SCALAR_ARITH_H

#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif

/// Routines for vector-scalar arithmetic
namespace ARCSStdVector
{
    /// add a scalar to every element of a vector. Explicit instantiations
    /// for float, double, int, unsigned.
    template <typename NumT>
    void add_scalar_vec( std::vector<NumT> & input, 
                         std::vector<NumT> & output,
                         NumT scalar);

    /// add a scalar to every element of some iterator range. Explicit
    /// instantiations for float, double, int, unsigned.
    template <typename InputIterator, typename OutputIterator, 
              typename NumT>
    void add_scalar_vecIt( InputIterator startin, InputIterator endin, 
                           OutputIterator output,
                           NumT scalar);

    /// multiply every element of a vector by a scalar. Explicit 
    /// instantiations for float, double, int, unsigned.
    template <typename NumT>
    void mult_scalar_vec( std::vector<NumT> & input, 
                          std::vector<NumT> & output,
                          NumT scalar);

    /// multiply every element of an iterator range by a scalar. Explicit 
    /// instantiations for float, double, int, unsigned.
    template <typename InputIterator, typename OutputIterator, 
              typename NumT>
    void mult_scalar_vecIt( InputIterator startin, InputIterator endin, 
                            OutputIterator output,
                            NumT scalar);
} // ARCSStdVector

#endif



// version
// $Id: vec_scalar_arith.h 2 2004-10-01 18:15:11Z tim $

// End of file
