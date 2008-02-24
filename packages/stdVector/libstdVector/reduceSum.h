// Timothy M. Kelley Copyright (c) 2005 All rights reserved
#ifndef REDUCESUM_H
#define REDUCESUM_H

#include <vector>

namespace ARCSStdVector
{
    template <typename NumT>
    void reduceSum2d( std::vector<NumT> const &vec2d,
                       std::vector<NumT> & vec1d,
                       std::vector<size_t> const & sizes,
                       size_t axis);

    template <typename NumT>
    void reduceSum3d( std::vector<NumT> const & vec3d,
                      std::vector<NumT> & vec2d,
                      std::vector<size_t> const & sizes,
                      size_t axis);
} // ARCSStdVector::
#endif



// version
// $Id: reduceSum.h 101 2005-07-31 21:39:07Z tim $

// End of file
