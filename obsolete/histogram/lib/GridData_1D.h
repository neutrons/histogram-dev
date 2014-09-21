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


#ifndef HISTOGRAM_GRIDDATA_1D_H
#define HISTOGRAM_GRIDDATA_1D_H


#include "_macros.h"


HISTOGRAM_NAMESPACE_START

  /// 1-dimensional grid data.
  /// This class associates a 1D data array and 1d axis mapper.
  /// For example, say we have an axis detectorID=[10, 11, ..., 20],
  /// and an array [3, 15, ..., 9]. Together they represent a histogram.
  /// The most important usage of this kind of grid data is to return
  /// value of f(x) given a value of x.
  /// This class decomposes to two things: an axis mapper that maps
  /// x value to index, and an array that maps index to value.
  /// This class is not intended to be used by users of this library.
  /// Classes in this library use this class, however, and provide
  /// easier-to-use interfaces.
  /// 
  /// template arguments:
  ///   XAxisMapper: functor class to map x value to index
  ///   YArray: 1-dimensional array class.
  template < typename XDataType, typename XAxisMapper,
	     typename YDataType, typename YArray>
  class GridData_1D {

  public:

    /// ctor.
    GridData_1D( const XAxisMapper & xmapper, YArray & yarray ) :
      m_xmapper( xmapper ),
      m_yarray( yarray )
    {
    }

    /// function-like interface. get value.
    ///  f(x) --> y
    const YDataType & operator () ( const XDataType & x ) const
    {
      return m_yarray[ m_xmapper(x) ];
    }

    /// function-like interface. set value.
    ///  f(x) = y
    YDataType & operator () ( const XDataType & x )
    {
      return m_yarray[ m_xmapper(x) ];
    }

    void clear() { m_yarray.clear(); }

  private:
    const XAxisMapper & m_xmapper;
    YArray & m_yarray;
  };

HISTOGRAM_NAMESPACE_END


#endif //HISTOGRAM_GRIDDATA_1D_H


// version
// $Id$

// End of file 
