// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef HISTOGRAM_NDARRAYSLICE_H
#define HISTOGRAM_NDARRAYSLICE_H


#include <vector>


#include "_macros.h"



/// Slice of an NdArray. Match the interface to NdArray
/// Now we only do array[x,:,:] or array[:,y,:] or array[:,y]
/// Cannot do array[a:b, y, z] yet


HISTOGRAM_NAMESPACE_START

    template <typename NdArray, typename DataType = double, typename IndexType = unsigned int>
    class NdArraySlice {
      
    public:

      // types
      typedef DataType datatype;
      typedef IndexType index_t;

      // meta methods
      NdArraySlice( NdArray & data, const std::vector<int> & indexes );

      // shape methods
      index_t dimension() const;
      const index_t * shape() const;

      // item access
      const DataType & operator [] ( const std::vector<index_t> & ) const;
      DataType & operator [] ( const std::vector<index_t> & ) ;
      
    private:
      
      // data
      NdArray & m_data;
      // implementation
      std::vector< index_t >  m_axismap, m_shape, m_t_indexes;
    };

HISTOGRAM_NAMESPACE_END

#include "NdArraySlice.icc"

#endif //HISTOGRAM_NDARRAYSLICE_H

// version
// $Id$

// End of file 
