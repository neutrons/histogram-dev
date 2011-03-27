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


#ifndef HISTOGRAM_GRIDDATA_2D_H
#define HISTOGRAM_GRIDDATA_2D_H


#include "_macros.h"


HISTOGRAM_NAMESPACE_START
    
    /// 2-dimensional grid data.
    /// This class associates a 2D data array and two axis mappers.
    /// For example, say we have an axis detectorID=[10, 11, ..., 20],
    /// and an axis pixelID=[0,1,2,3]
    /// and an array of shape 11 X 4. 
    /// Together they represent a histogram.
    /// The most important usage of this kind of grid data is to return
    /// value of f(x,y) given values of x and y.
    /// This class decomposes to three things: an axis mapper that maps
    /// x value to index, and another axis mapper that maps y value to
    /// index, and an array that maps two indexes to a value.
    /// This class is not intended to be used by users of this library.
    /// Classes in this library use this class, however, and provide
    /// easier-to-use interfaces.
    /// 
    /// template arguments:
    ///   XAxisMapper: functor class to map x value to index
    ///   YAxisMapper: functor class to map y value to index
    ///   ZArray: 2-dimensional array class.
    template < typename XDataType, typename XAxisMapper, 
	       typename YDataType, typename YAxisMapper,
	       typename ZDataType, typename ZArray,
	       typename IndexType = unsigned int>
    class GridData_2D {
      
    public:
      /// ctor.
      GridData_2D( const XAxisMapper & xmapper, 
		   const YAxisMapper & ymapper,
		   ZArray & zarray ) :
	m_xmapper( xmapper ),  m_ymapper( ymapper ),
	m_zarray( zarray )
      {
      }

      void clear() { m_zarray.clear(); }

      /// function-like interface. get value.
      ///  f(x,y) --> z
      const ZDataType & operator () ( const XDataType & x, const YDataType &y ) const
      {
	static IndexType indexes[2];
	indexes[0] = m_xmapper( x );
	indexes[1] = m_ymapper( y );
	
	return m_zarray[ indexes ];
      }

      /// function-like interface. set value.
      ///  f(x,y) = z
      ZDataType & operator () ( const XDataType & x, const YDataType & y )
      {
	static IndexType indexes[2];
	indexes[0] = m_xmapper( x );
	indexes[1] = m_ymapper( y );

	return m_zarray[ indexes ];
      }

    private:
      const XAxisMapper & m_xmapper;
      const YAxisMapper & m_ymapper;
      ZArray & m_zarray;

    };

HISTOGRAM_NAMESPACE_END
    

#endif // HISTOGRAM_GRIDDATA_2D_H


// version
// $Id$

// End of file 
