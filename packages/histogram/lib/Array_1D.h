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

#ifndef HISTOGRAM_ARRAY_1D_H
#define HISTOGRAM_ARRAY_1D_H


#include "OutOfBound.h"
#include "_macros.h"

HISTOGRAM_NAMESPACE_START

  /// 1-dimensional array.
  /// template class for 1-dimensional array
  /// This 1-D array takes a 1D array iterator and implement array interface.
  /// 
  /// tempalate parameters:
  ///  Iterator: 1D array iterator type
  ///  DataType: data type of array elements
  ///  Size: type of the shape array
  /// 
  /// CAUTION:
  ///  This class is not responsible for checking if the given iterator is sane.
  ///  If the iterator does not have the right size, core dump will happen.
  ///
  /// Implementation:
  ///  The input 1D array is treated as mD array by the convention that
  ///  the last index runs the fastest.
  ///
  template <typename Iterator, typename DataType, typename Size>
  class Array_1D {

  public:
    
    typedef DataType datatype;
    
    /// ctor.
    ///
    /// Parameters:
    ///   it: 1D array iterator. The 1D array must have been allocated with sufficient
    ///       memory.
    ///   size: length of the array.
    ///
    Array_1D( Iterator it, Size size ) :
      m_it(it) 
    {
      m_size = size;
    }
    
    /// dtor.
    ~Array_1D() { }
    
    /// get element.
    const DataType & operator [] ( const Size & index ) const
    {
      if (index<0 or index>m_size) _throw_out_of_bound( index );
      return *(m_it+index);
    }
    
    /// set element.
    DataType & operator [] ( const Size &index ) 
    {
      if (index<0 or index>m_size) _throw_out_of_bound( index );
      return *(m_it+index);
    }

    /// set all elements to zero.
    void clear() 
    {
      for (Iterator it = m_it; it < m_it + m_size; it++ ) 
	*it = 0;
    }
    
  private:
    Iterator m_it;
    Size m_size;
    void _throw_out_of_bound(const Size & index) const throw (OutOfBound) ;

  }; // Array_1D:

HISTOGRAM_NAMESPACE_END


#define HISTOGRAM_ARRAY_1D_ICC
#include "Array_1D.icc"
#undef HISTOGRAM_ARRAY_1D_ICC


#endif // HISTOGRAM_ARRAY_1D_H


// version
// $Id$

// End of file 
