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

#ifndef DANSE_HISTOGRAM_NDARRAY_H
#define DANSE_HISTOGRAM_NDARRAY_H


#include "OutOfBound.h"


namespace DANSE {

namespace Histogram{

  /// Multiple dimensional array.
  /// template class for multiple-dimensional array
  /// This m-D array takes a 1D array iterator and pretend it to be a 
  /// m-D array.
  /// This is probably not flexible enough, but it should be doing quite well
  /// for many forseeable applications.
  /// 
  /// tempalate parameters:
  ///  Iterator: 1D array iterator type
  ///  DataType: data type of 1D array elements
  ///  Size: type of the shape array
  ///  SuperSize: type of the size of the array if casted to 1D
  ///  NDimension: number of dimensions
  /// 
  /// CAUTION:
  ///  This class is not responsible for checking if the given iterator is sane.
  ///  If the iterator does not have the right size, core dump will happen.
  ///
  /// Implementation:
  ///  The input 1D array is treated as mD array by the convention that
  ///  the last index runs the fastest.
  ///
  template <typename Iterator, typename DataType, typename Size, typename SuperSize,
	    unsigned int NDimension>
  class NdArray {

  public:
    
    typedef DataType datatype;
    
    /// ctor.
    ///
    /// Parameters:
    ///   it: 1D array iterator. The 1D array must have been allocated with sufficient
    ///       memory.
    ///   shape: an array of integers specifiying the size of each dimension
    ///
    /// CAUTION:
    ///   array shape must have 'NDimension' elements
    ///
    NdArray( Iterator it, Size shape[NDimension] ) :
      m_it(it) 
    {
      m_size1D = 1;
      
      for (unsigned int i=0; i<NDimension; i++) {
	m_shape[i] = shape[i];
	m_size1D *= shape[i];
      }
    }
    
    /// dtor.
    ~NdArray() { }
    
    /// get element.
    /// indexes must have 'NDimension' elements
    const DataType & operator [] ( Size indexes[NDimension] ) const
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }
    
    /// set element.
    /// indexes must have 'NDimension' elements
    DataType & operator [] ( Size indexes[NDimension] ) 
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }

    /// set all elements to zero.
    void clear() 
    {
      for (Iterator it = m_it; it < m_it + m_size1D; it++ ) 
	*it = 0;
    }
    
  private:
    Iterator m_it;
    Size m_shape[NDimension];
    SuperSize m_size1D;
    SuperSize _1dindex( Size indexes[NDimension] ) const throw (OutOfBound) ;
    void _throw_out_of_bound(Size indexes[NDimension]) const throw (OutOfBound) ;

  }; // NdArray:

} // Histogram:  
} // DANSE:


#define DANSE_HISTOGRAM_NDARRAY_ICC
#include "NdArray.icc"
#undef DANSE_HISTOGRAM_NDARRAY_ICC


#endif // DANSE_HISTOGRAM_NDARRAY_H


// version
// $Id$

// End of file 
