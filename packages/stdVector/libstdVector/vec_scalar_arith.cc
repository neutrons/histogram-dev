// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vec_scalar_arith.h"
#include <numeric>
// transform should be in <algorithm>
#include <algorithm>

namespace ARCSStdVector
{
    //--------------------------- add_scalar ----------------------------
    template < typename NumT>
    void add_scalar_vec( std::vector<NumT> & input, 
                         std::vector<NumT> & output,
                         NumT scalar)
    {
//         std::transform( input.begin(), input.end(), //scalarr.begin(), 
//                         output.begin(), std::bind1st( std::plus<NumT>(),
//                                                       scalar));
        for(size_t i=0; i<input.size(); ++i) output[i] = input[i] + scalar;
    }

    // explicit instantiations
    template void add_scalar_vec<float> ( std::vector<float> & vec, 
                                          std::vector<float> & output,
                                          float scalar);
    template void add_scalar_vec<double>( std::vector<double> & vec, 
                                          std::vector<double> & output,
                                          double scalar);
    template void add_scalar_vec<int>   ( std::vector<int> & vec,
                                          std::vector<int> & output,
                                          int scalar);
    template void add_scalar_vec<unsigned>( std::vector<unsigned> & vec, 
                                            std::vector<unsigned> & output,
                                            unsigned scalar);

    template <typename InputIterator, typename OutputIterator, 
              typename NumT>
    void add_scalar_vecIt( InputIterator startin, InputIterator endin, 
                           OutputIterator output,
                           NumT scalar)
    {
        while(startin != endin) *output++ = (*startin++) + scalar;
    }

    // explicit instantiations
    template void add_scalar_vecIt( std::vector<double>::iterator,
                                    std::vector<double>::iterator,
                                    std::vector<double>::iterator,
                                    double);
    template void add_scalar_vecIt( std::vector<float>::iterator,
                                    std::vector<float>::iterator,
                                    std::vector<float>::iterator,
                                    float);
    template void add_scalar_vecIt( std::vector<int>::iterator,
                                    std::vector<int>::iterator,
                                    std::vector<int>::iterator,
                                    int);
    template void add_scalar_vecIt( std::vector<unsigned>::iterator,
                                    std::vector<unsigned>::iterator,
                                    std::vector<unsigned>::iterator,
                                    unsigned);

    //----------------------------- mult_scalar --------------------------
    
    template <typename NumT>
    void mult_scalar_vec( std::vector<NumT> & input, 
                          std::vector<NumT> & output,
                          NumT scalar)
    {
        for(size_t i=0; i<input.size(); ++i) output[i] = input[i]*scalar;
        return;
    }
    
    template void mult_scalar_vec( std::vector<float> &, 
                                   std::vector<float> &,
                                   float);
    template void mult_scalar_vec( std::vector<double> &, 
                                   std::vector<double> &,
                                   double);
    template void mult_scalar_vec( std::vector<int> &,
                                   std::vector<int> &,
                                   int);
    template void mult_scalar_vec( std::vector<unsigned> &, 
                                   std::vector<unsigned> &,
                                   unsigned);

    template <typename InputIterator, typename OutputIterator, 
              typename NumT>
    void mult_scalar_vecIt( InputIterator startin, InputIterator endin, 
                            OutputIterator output,
                            NumT scalar)
    {
        while(startin != endin) *output++ = (*startin++)*scalar;
    }
   
    // explicit instantiations
    template void mult_scalar_vecIt( std::vector<double>::iterator,
                                     std::vector<double>::iterator,
                                     std::vector<double>::iterator,
                                     double);
    template void mult_scalar_vecIt( std::vector<float>::iterator,
                                     std::vector<float>::iterator,
                                     std::vector<float>::iterator,
                                     float);
    template void mult_scalar_vecIt( std::vector<int>::iterator,
                                     std::vector<int>::iterator,
                                     std::vector<int>::iterator,
                                     int);
    template void mult_scalar_vecIt( std::vector<unsigned>::iterator,
                                     std::vector<unsigned>::iterator,
                                     std::vector<unsigned>::iterator,
                                     unsigned);

} // ARCSStdVector::

// version
// $Id: vec_scalar_arith.cc 42 2005-02-02 22:49:14Z tim $

// End of file
