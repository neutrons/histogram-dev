// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "vec_vec_arith.h"
#include <string>
#include <algorithm>
#ifdef WIN32
#include <functional>  // for std::plus & co on win32
#endif

namespace
{
    template <typename NumT>
    void checkInputsA( std::string & errstr, 
                       std::vector<NumT> const & input, 
                       size_t inBegin, size_t inEnd, 
                       std::vector<NumT> output, 
                       size_t outBegin)
    {
        if (inEnd < inBegin)
        {
            errstr += "end < begin";
            throw errstr;
        }
        if (inEnd > input.size())
        {
            errstr += " inputEnd > input size";
            throw errstr;
        }
        size_t sz = inEnd - inBegin;
        if (sz + outBegin > output.size())
        {
            errstr += "size too great for output";
            throw errstr;
        }
        return;
    } // checkInputsA(...)


    template <typename NumT>
    void checkInputsB( std::string & errstr, 
                       std::vector<NumT> const & input1, 
                       std::vector<NumT> const & input2, 
                       size_t inBegin, size_t inEnd, 
                       std::vector<NumT> output, 
                       size_t outBegin)
    {
        if (inEnd < inBegin)
        {
            errstr += "end < begin";
            throw errstr;
        }
        if (inEnd > input1.size())
        {
            errstr += " inputEnd > input1 size";
            throw errstr;
        }
        if (inEnd > input1.size())
        {
            errstr += " inputEnd > input2 size";
            throw errstr;
        }
        size_t sz = inEnd - inBegin;
        if (sz + outBegin > output.size())
        {
            errstr += "size too great for output";
            throw errstr;
        }
        return;
    } // checkInputsB(...)
} // anonymous::


namespace ARCSStdVector
{
    template <typename NumT>
    void vec_plusEquals( std::vector<NumT> const & input, 
                         size_t inputBegin, 
                         size_t inputEnd,
                         std::vector<NumT> & output,
                         size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_plusEquals() ");
        checkInputsA( errstr, input, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input[inputBegin], &input[inputEnd], 
                        &output[outputBegin],
                        &output[outputBegin], std::plus<NumT>());
        return;
    }


    template <typename NumT>
    void vec_minusEquals( std::vector<NumT> const & input, 
                         size_t inputBegin, 
                         size_t inputEnd,
                         std::vector<NumT> & output,
                         size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_minusEquals() ");
        checkInputsA( errstr, input, inputBegin, inputEnd, output,
                      outputBegin);
        size_t sz = inputEnd - inputBegin;
        std::transform( &output[outputBegin], &output[outputBegin+sz], 
                        &input[inputBegin],
                        &output[outputBegin], std::minus<NumT>());
        return;
    }

    template <typename NumT>
    void vec_timesEquals( std::vector<NumT> const & input, 
                         size_t inputBegin, 
                         size_t inputEnd,
                         std::vector<NumT> & output,
                         size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_timesEquals() ");
        checkInputsA( errstr, input, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input[inputBegin], &input[inputEnd], 
                        &output[outputBegin], &output[outputBegin], 
                        std::multiplies<NumT>());
        return;
    }


    template <typename NumT>
    void vec_divideEquals( std::vector<NumT> const & input, 
                           size_t inputBegin, 
                           size_t inputEnd,
                           std::vector<NumT> & output,
                           size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_divideEquals() ");
        checkInputsA( errstr, input, inputBegin, inputEnd, output,
                      outputBegin);
        size_t sz = inputEnd - inputBegin;
        std::transform( &output[outputBegin], &output[outputBegin+sz], 
                        &input[inputBegin], &output[outputBegin], 
                        std::divides<NumT>());
        return;
    }


    template <typename IOIterator, typename NumT>
    void it_plusEquals( IOIterator startin, IOIterator endin,
                        IOIterator startout)
    {
        std::transform( startin, endin, startout, startout, 
                        std::plus<NumT>());
        return;
    }


    template <typename NumT>
    void vec_plus( std::vector<NumT> const & input1,  
                   std::vector<NumT> const & input2, 
                   size_t inputBegin, 
                   size_t inputEnd,
                   std::vector<NumT> & output,
                   size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_plusEquals() ");
        checkInputsB( errstr, input1, input2, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input1[inputBegin], &input1[inputEnd], 
                        &input2[outputBegin],
                        &output[outputBegin], std::plus<NumT>());
        return;
    }


    template <typename NumT>
    void vec_minus( std::vector<NumT> const & input1,  
                    std::vector<NumT> const & input2, 
                    size_t inputBegin, 
                    size_t inputEnd,
                    std::vector<NumT> & output,
                    size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_plusEquals() ");
        checkInputsB( errstr, input1, input2, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input2[inputBegin], &input2[inputEnd], 
                        &input1[outputBegin],
                        &output[outputBegin], std::minus<NumT>());
        return;
    }


    template <typename NumT>
    void vec_times( std::vector<NumT> const & input1,  
                    std::vector<NumT> const & input2, 
                    size_t inputBegin, 
                    size_t inputEnd,
                    std::vector<NumT> & output,
                    size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_plusEquals() ");
        checkInputsB( errstr, input1, input2, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input1[inputBegin], &input1[inputEnd], 
                        &input2[outputBegin],
                        &output[outputBegin], std::multiplies<NumT>());
        return;
    }


    template <typename NumT>
    void vec_divide( std::vector<NumT> const & input1,  
                     std::vector<NumT> const & input2, 
                     size_t inputBegin, 
                     size_t inputEnd,
                     std::vector<NumT> & output,
                     size_t outputBegin)
    {
        std::string errstr("ARCSStdVector::vec_plusEquals() ");
        checkInputsB( errstr, input1, input2, inputBegin, inputEnd, output,
                      outputBegin);
        std::transform( &input1[inputBegin], &input1[inputEnd], 
                        &input2[outputBegin],
                        &output[outputBegin], std::divides<NumT>());
        return;
    }


    // it_plusEquals explicit instantiations
    template void it_plusEquals<std::vector<double>::iterator, double>
    ( std::vector<double>::iterator, 
      std::vector<double>::iterator, 
      std::vector<double>::iterator);
    
    template void it_plusEquals<std::vector<float>::iterator, float>
    ( std::vector<float>::iterator, 
      std::vector<float>::iterator, 
      std::vector<float>::iterator);
    
    template void it_plusEquals<std::vector<int>::iterator, int>
    ( std::vector<int>::iterator, 
      std::vector<int>::iterator, 
      std::vector<int>::iterator);

    template void it_plusEquals<std::vector<unsigned>::iterator, unsigned>
    ( std::vector<unsigned>::iterator, 
      std::vector<unsigned>::iterator, 
      std::vector<unsigned>::iterator);

    // explicit instantiations, vector
    // +=
    template 
    void vec_plusEquals<float>( std::vector<float> const &, size_t, size_t,
                                std::vector<float> &, size_t);
    template
    void vec_plusEquals<double>( std::vector<double> const &, size_t,
                                 size_t, std::vector<double> &, size_t);
    template
    void vec_plusEquals<int>( std::vector<int> const &, size_t, size_t,
                              std::vector<int> &, size_t);
    template
    void vec_plusEquals<unsigned>(std::vector<unsigned> const &, size_t, 
                                  size_t, std::vector<unsigned> &, size_t);
    // -=
    template 
    void vec_minusEquals<float>( std::vector<float> const &, size_t, 
                                 size_t, std::vector<float> &, size_t);
    template
    void vec_minusEquals<double>( std::vector<double> const &, size_t, 
                                  size_t, std::vector<double> &, size_t);
    template
    void vec_minusEquals<int>( std::vector<int> const &, size_t, 
                               size_t, std::vector<int> &, size_t);
    template
    void vec_minusEquals<unsigned>( std::vector<unsigned> const &, size_t, 
                                    size_t, std::vector<unsigned> &, size_t);
    // *=

    template 
    void vec_timesEquals<float>( std::vector<float> const &, size_t, 
                                 size_t, std::vector<float> &, size_t);
    template
    void vec_timesEquals<double>( std::vector<double> const &, size_t, 
                                  size_t, std::vector<double> &, size_t);
    template
    void vec_timesEquals<int>( std::vector<int> const &, size_t, 
                               size_t, std::vector<int> &, size_t);
    template
    void vec_timesEquals<unsigned>( std::vector<unsigned> const &, size_t, 
                                    size_t, std::vector<unsigned> &, size_t);

    // /=
    template 
    void vec_divideEquals<float>( std::vector<float> const &, size_t, 
                                  size_t, std::vector<float> &, size_t);
    template
    void vec_divideEquals<double>( std::vector<double> const &, size_t, 
                                   size_t, std::vector<double> &, size_t);
    template
    void vec_divideEquals<int>( std::vector<int> const &, size_t, 
                                size_t, std::vector<int> &, size_t);
    template
    void vec_divideEquals<unsigned>( std::vector<unsigned> const &, size_t,
                                     size_t, std::vector<unsigned> &, 
                                     size_t);

    // +
    template 
    void vec_plus<float>( std::vector<float> const &, 
                          std::vector<float> const &,
                          size_t, size_t,
                          std::vector<float> &, size_t);
    template
    void vec_plus<double>( std::vector<double> const &, 
                           std::vector<double> const &,
                           size_t, size_t, 
                           std::vector<double> &, size_t);
    template
    void vec_plus<int>( std::vector<int> const &, 
                        std::vector<int> const &, 
                        size_t, size_t, 
                        std::vector<int> &, size_t);
    template
    void vec_plus<unsigned>(std::vector<unsigned> const &, 
                            std::vector<unsigned> const &, 
                            size_t, size_t, 
                            std::vector<unsigned> &, size_t);

    // -
    template 
    void vec_minus<float>( std::vector<float> const &, 
                           std::vector<float> const &,
                           size_t, size_t,
                           std::vector<float> &, size_t);
    template
    void vec_minus<double>( std::vector<double> const &, 
                            std::vector<double> const &,
                            size_t, size_t, 
                            std::vector<double> &, size_t);
    template
    void vec_minus<int>( std::vector<int> const &, 
                         std::vector<int> const &, 
                         size_t, size_t, 
                         std::vector<int> &, size_t);
    template
    void vec_minus<unsigned>(std::vector<unsigned> const &, 
                             std::vector<unsigned> const &, 
                             size_t, size_t, 
                             std::vector<unsigned> &, size_t);

    // *
    template 
    void vec_times<float>( std::vector<float> const &, 
                           std::vector<float> const &,
                           size_t, size_t,
                           std::vector<float> &, size_t);
    template
    void vec_times<double>( std::vector<double> const &, 
                            std::vector<double> const &,
                            size_t, size_t, 
                            std::vector<double> &, size_t);
    template
    void vec_times<int>( std::vector<int> const &, 
                         std::vector<int> const &, 
                         size_t, size_t, 
                         std::vector<int> &, size_t);
    template
    void vec_times<unsigned>(std::vector<unsigned> const &, 
                             std::vector<unsigned> const &, 
                             size_t, size_t, 
                             std::vector<unsigned> &, size_t);

    // /
    template 
    void vec_divide<float>( std::vector<float> const &, 
                           std::vector<float> const &,
                           size_t, size_t,
                           std::vector<float> &, size_t);
    template
    void vec_divide<double>( std::vector<double> const &, 
                            std::vector<double> const &,
                            size_t, size_t, 
                            std::vector<double> &, size_t);
    template
    void vec_divide<int>( std::vector<int> const &, 
                         std::vector<int> const &, 
                         size_t, size_t, 
                         std::vector<int> &, size_t);
    template
    void vec_divide<unsigned>(std::vector<unsigned> const &, 
                             std::vector<unsigned> const &, 
                             size_t, size_t, 
                             std::vector<unsigned> &, size_t);


} // ARCSStdVector::

// version
// $Id: vec_vec_arith.cc 110 2005-08-09 17:48:39Z tim $

// End of file
