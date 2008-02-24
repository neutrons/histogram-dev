// Timothy M. Kelley Copyright (c) 2005 All rights reserved

#include "reduceSum.h"
#include <iostream>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <string>
#ifdef WIN32
#include <functional>
#endif


namespace ARCSStdVector
{
    /// reduceSum2d: Reduce a 2d vector to a 1d vector. axis means which axis 
/// gets summed over. Axis 1 means slowest running index, which is the 
/// innermost index in a C world, and outermost in a FORTRAN world.

    template <typename NumT>
    static void _reduceSum2d_checkinput( std::vector<NumT> const & invec,
                                         std::vector<NumT> const & outvec,
                                         std::vector< size_t> const & szs,
                                         size_t axnum)
    {
        std::string errstr("ARCS::reduceSum2d() ");

        // check for valid axis number
        if (axnum > 2 || axnum < 1)
        {
            errstr += "Invalid axis number";
            throw errstr;
        }

        // check size of vec2d
        size_t length = 1;
        for(size_t i=0; i<szs.size(); ++i) length *= szs[i];
        
        if (length != invec.size())
        {
            errstr += "dimen. sizes don't match total size of input vector.";
            std::cerr<<errstr<<"\nsizes: ";
            for (size_t i=0; i<szs.size(); ++i) std::cerr<<szs[i]<<" ";
            std::cerr<<"; inputVec.size(): "<<invec.size()<<"\n";
            throw errstr;
        }
        // check size of vec1d
        if ( axnum == 1) length = szs[1];
        else if ( axnum == 2) length = szs[0];
        if (outvec.size() != length)
        {
            errstr += "dimen. sizes don't match total size of output vector.";
            std::cerr<<errstr<<"\nsizes: ";
            for (size_t i=0; i<szs.size(); ++i) std::cerr<<szs[i]<<" ";
            std::cerr<<"; outputVec.size(): "<<outvec.size()<<"\n";
            throw errstr;
        }
        return;
    } // _reduceSum2d_checkinput(...)


    template <typename NumT>
    void reduceSum2d( std::vector<NumT> const &vec2d,
                      std::vector<NumT> & vec1d,
                      std::vector<size_t> const & sizes,
                      size_t axis)
    {
        _reduceSum2d_checkinput( vec2d, vec1d, sizes, axis);
        size_t l1 = sizes[0], l2 = sizes[1];

        switch(axis)
        {
        case 1:
            // Cache coherence!
            for( size_t i1=0; i1 < l1; i1++)
                std::transform( &vec2d[ i1*l2],
                                &vec2d[ (i1+1)*l2],
                                vec1d.begin(),
                                vec1d.begin(),
                                std::plus<NumT>() );
            break;
        case 2:
            // Less coherence...
            for( size_t i1 = 0; i1< l1; ++i1)
                vec1d[ i1] = std::accumulate( &vec2d[i1*l2], 
                                              &vec2d[(i1+1)*l2], 
                                              static_cast<NumT>(0.0));
            break;
        default:
            std::string errstr("ARCS::reduceSum2d(): invalid axis.");
            throw errstr;
        }
        return;
    } //reduceSum2d(...)

    template void reduceSum2d<float>( std::vector<float> const &vec2d,
                                      std::vector<float> & vec1d,
                                      std::vector<size_t> const & sizes,
                                      size_t axis);
    template void reduceSum2d<double>( std::vector<double> const &vec2d,
                                        std::vector<double> & vec1d,
                                        std::vector<size_t> const & sizes,
                                       size_t axis);
    template void reduceSum2d<int>( std::vector<int> const &vec2d,
                                     std::vector<int> & vec1d,
                                     std::vector<size_t> const & sizes,
                                     size_t axis);
    template void reduceSum2d<unsigned int>( std::vector<unsigned int> const &vec2d,
                                             std::vector<unsigned int> & vec1d,
                                             std::vector<size_t> const & sizes,
                                             size_t axis);


    template <typename NumT>
    static void _reduceSum3d_checkinput( std::vector<NumT> const & invec,
                                         std::vector<NumT> const & outvec,
                                         std::vector< size_t> const & szs,
                                         size_t axnum)
    {
        std::string errstr("ARCS::reduceSum3d() ");
     
        // check valid axis number
        if ( axnum < 1 || axnum > 3)
        {
            errstr += "Invalid axis number";
            throw errstr;
        }

        // check size of vec3d
        size_t length = 1;
        for(size_t i=0; i<szs.size(); ++i) length *= szs[i];
        
        if (length != invec.size())
        {
            errstr += "dimen. sizes don't match total size of input vector.";
            std::cerr<<errstr<<"\nsizes: ";
            for (size_t i=0; i<szs.size(); ++i) std::cerr<<szs[i]<<" ";
            std::cerr<<"; inputVec.size(): "<<invec.size()<<"\n";
            throw errstr;
        }
        // check size of vec2d
        if ( axnum == 1) length = szs[1]*szs[2];
        else if ( axnum == 2) length = szs[0]*szs[2];
        else if ( axnum == 3) length = szs[1]*szs[0];
        if (outvec.size() != length)
        {
            errstr += "dimen. sizes don't match total size of output vector.";
            std::cerr<<errstr<<"\nsizes: ";
            for (size_t i=0; i<szs.size(); ++i) std::cerr<<szs[i]<<" ";
            std::cerr<<"; outputVec.size(): "<<outvec.size()<<"\n";
            throw errstr;
        }

        return;
    } // _reduceSum3d_checkinput(...)


    template <typename NumT>
    void reduceSum3d( std::vector<NumT> const & vec3d,
                      std::vector<NumT> & vec2d,
                      std::vector<size_t> const & sizes,
                      size_t axis)
    {
        _reduceSum3d_checkinput( vec3d, vec2d, sizes, axis);

        size_t l1 = sizes[0], l2 = sizes[1], l3 = sizes[2];

        switch(axis)
        {
        case 1:
            // Cache coherence!
            for( size_t i1=0; i1 < l1; i1++)
                std::transform( &vec3d[ i1*l2*l3],
                                &vec3d[ (i1+1)*l2*l3],
                                vec2d.begin(),
                                vec2d.begin(),
                                std::plus<NumT>() );
            break;
        case 2:
            // Less coherence...
            for( size_t i1 = 0; i1< l1; ++i1)
                for( size_t i2 = 0; i2 < l2; ++i2)
                    std::transform( &vec3d[ (i1*l2 + i2)*l3],
                                    &vec3d[ (i1*l2 + i2 + 1)*l3],
                                    &vec2d[ i1*l3],
                                    &vec2d[ i1*l3],
                                    std::plus<NumT>());
            break;
        case 3:
            // :(
            for( size_t i1 = 0; i1 < l1; ++i1)
                for( size_t i2 = 0; i2 < l2; ++i2)
                {
                    vec2d[i1*l2+i2] = 
                        static_cast<NumT>(
                            std::accumulate( &vec3d[(i1*l2+i2)*l3],
                                             &vec3d[(i1*l2+i2+1)*l3],
                                             0.0) );
                    // Alt. method (faster?)
                    // NumT temp = static_cast<NumT>(0.0);
                    // for( size_t i3 = 0; i3<l3; ++i3)
                    //     temp += vec3d[(i1*l2+i2)*l3+i3];
                    // vec2d[i1*l2 + i2] = temp;
                }
            break;
        default:
            std::string errstr("ARCS::reduceSum3d(): invalid axis.");
            throw errstr;
        }
        return;
    } // reduceSum3d


    template void reduceSum3d<double>( std::vector<double> const & vec3d,
                                       std::vector<double> & vec2d,
                                       std::vector<size_t> const & sizes,
                                       size_t axis);
    template void reduceSum3d<float>( std::vector<float> const & vec3d,
                                      std::vector<float> & vec2d,
                                      std::vector<size_t> const & sizes,
                                      size_t axis);
    template void reduceSum3d<int>( std::vector<int> const & vec3d,
                                    std::vector<int> & vec2d,
                                    std::vector<size_t> const & sizes,
                                    size_t axis);
    template void reduceSum3d<unsigned int>( std::vector<unsigned int> const & vec3d,
                                             std::vector<unsigned int> & vec2d,
                                             std::vector<size_t> const & sizes,
                                             size_t axis);
} // ARCSStdVector

// version
// $Id: reduceSum.cc 101 2005-07-31 21:39:07Z tim $

// End of file
