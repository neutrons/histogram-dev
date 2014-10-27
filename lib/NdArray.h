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

#ifndef HISTOGRAM_NDARRAY_H
#define HISTOGRAM_NDARRAY_H


#include <vector>
#include "OutOfBound.h"

#include "journal/debug.h"


HISTOGRAM_NAMESPACE_START

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
  template <typename Iterator, typename DataType,
	    typename Size, typename SuperSize,
	    unsigned int NDimension>
  class NdArray {

  public:
    
    typedef DataType datatype;
    typedef Size index_t;

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
    NdArray( Iterator it, const Size shape[NDimension] ) :
      m_it(it) 
    {
      m_size1D = 1;
#ifdef DEBUG
      journal::debug_t debug("NdArray");
      debug << journal::at(__HERE__)
	    << "dimension: " << dimension() << journal::endl
	    << "shape: " ;
#endif
      
      for (unsigned int i=0; i<NDimension; i++) {
	m_shape[i] = shape[i];
	m_size1D *= shape[i];
#ifdef DEBUG
      debug 
	<< shape[i] << ", ";
#endif
      }
#ifdef DEBUG
      debug << journal::endl; 
#endif
    }
    
    /// dtor.
    ~NdArray() { }
    
    /// shape
    Size dimension() const { return NDimension; }
    const Size * shape() const { return m_shape; }
    
    
    /// get element.
    /// indexes must have 'NDimension' elements
    const DataType & operator [] ( const Size *indexes ) const
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }
    const DataType & operator [] ( const std::vector<Size> & indexes ) const
    {
      assert (indexes.size() == NDimension);
      return this->operator[]( &(indexes[0]) );
    }
    
    /// set element.
    /// indexes must have 'NDimension' elements
    DataType & operator [] ( const Size *indexes ) 
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }
    DataType & operator [] ( const std::vector<Size> & indexes ) 
    {
      assert (indexes.size() == NDimension);
      return this->operator[]( &(indexes[0]) );
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
    SuperSize _1dindex( const Size *indexes ) const throw (OutOfBound) ;
    void _throw_out_of_bound(const Size * indexes) const throw (OutOfBound) ;

  }; // NdArray:


HISTOGRAM_NAMESPACE_END


#define HISTOGRAM_NDARRAY_ICC
#include "NdArray.icc"
#undef HISTOGRAM_NDARRAY_ICC


#endif // HISTOGRAM_NDARRAY_H


// version
// $Id$

// End of file 
