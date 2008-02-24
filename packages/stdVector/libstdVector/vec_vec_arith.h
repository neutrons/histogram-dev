// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef VEC_VEC_ARITH_H
#define VEC_VEC_ARITH_H

#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif
 
namespace ARCSStdVector
{
    template <typename NumT>
    void vec_plusEquals( std::vector<NumT> const & input, 
                         size_t inputBegin, 
                         size_t inputEnd,
                         std::vector<NumT> & output,
                         size_t outputBegin);

    template <typename NumT>
    void vec_minusEquals( std::vector<NumT> const & input, 
                          size_t inputBegin, 
                          size_t inputEnd,
                          std::vector<NumT> & output,
                          size_t outputBegin);

    template <typename NumT>
    void vec_timesEquals( std::vector<NumT> const & input, 
                          size_t inputBegin, 
                          size_t inputEnd,
                          std::vector<NumT> & output,
                          size_t outputBegin);

    template <typename NumT>
    void vec_divideEquals( std::vector<NumT> const & input, 
                           size_t inputBegin, 
                           size_t inputEnd,
                           std::vector<NumT> & output,
                           size_t outputBegin);

    template <typename IOIterator, typename NumT>
    void it_plusEquals( IOIterator inStart, IOIterator inEnd,
                        IOIterator outStart);        

    template <typename NumT>
    void vec_plus( std::vector<NumT> const & input1, 
                   std::vector<NumT> const & input2, 
                   size_t inputBegin, 
                   size_t inputEnd,
                   std::vector<NumT> & output,
                   size_t outputBegin);

    template <typename NumT>
    void vec_minus( std::vector<NumT> const & input1, 
                   std::vector<NumT> const & input2, 
                   size_t inputBegin, 
                   size_t inputEnd,
                   std::vector<NumT> & output,
                   size_t outputBegin);

    template <typename NumT>
    void vec_times( std::vector<NumT> const & input1, 
                    std::vector<NumT> const & input2, 
                    size_t inputBegin, 
                    size_t inputEnd,
                    std::vector<NumT> & output,
                    size_t outputBegin);

    template <typename NumT>
    void vec_divide( std::vector<NumT> const & input1, 
                     std::vector<NumT> const & input2, 
                     size_t inputBegin, 
                     size_t inputEnd,
                     std::vector<NumT> & output,
                     size_t outputBegin);
}
#endif



// version
// $Id: vec_vec_arith.h 72 2005-05-17 23:35:08Z tim $

// End of file
