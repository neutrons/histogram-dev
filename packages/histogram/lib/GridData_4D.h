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


#ifndef HISTOGRAM_GRIDDATA_4D_H
#define HISTOGRAM_GRIDDATA_4D_H


#include "_macros.h"

HISTOGRAM_NAMESPACE_START
    
    /// 4-dimensional grid data.
    /// This class associates a 4D data array and 4 axis mappers.
    /// For example, say we have 4 axes:
    ///   packID=[1, ..., 115]
    ///   detectorID=[0,..., 7]
    ///   pixelID=[0,...,127]
    ///   tof=[3000,3001,...,6000]
    /// and an array of shape 116 X 8 X 128 X 3001. 
    /// Together they represent a histogram.
    /// The most important usage of this kind of grid data is to return
    /// value of f(x1,x2,x3,x4) given values of {xi}.
    /// This class decomposes to two kinds of things: 
    ///   axis mappers that map xi value to index for ith axis, 
    ///   an array that maps four indexes to a value.
    /// This class is not intended to be used by users of this library.
    /// Classes in this library use this class, however, and provide
    /// easier-to-use interfaces.
    /// 
    /// template arguments:
    ///   X1AxisMapper: functor class to map x1 value to index
    ///   X2AxisMapper: functor class to map x2 value to index
    ///   X3AxisMapper: functor class to map x3 value to index
    ///   X4AxisMapper: functor class to map x4 value to index
    ///   ZArray: 4-dimensional array class.
    template < typename X1DataType, typename X1AxisMapper, 
	       typename X2DataType, typename X2AxisMapper,
	       typename X3DataType, typename X3AxisMapper,
	       typename X4DataType, typename X4AxisMapper,
	       typename ZDataType, typename ZArray,
	       typename IndexType = unsigned int>
    class GridData_4D {
      
    public:
      /// ctor.
      GridData_4D( const X1AxisMapper & x1mapper, 
		   const X2AxisMapper & x2mapper,
		   const X3AxisMapper & x3mapper,
		   const X4AxisMapper & x4mapper,
		   ZArray & zarray ) :
	m_x1mapper( x1mapper ),  
	m_x2mapper( x2mapper ),
	m_x3mapper( x3mapper ),
	m_x4mapper( x4mapper ),
	m_zarray( zarray )
      {
      }

      void clear() { m_zarray.clear(); }

      /// function-like interface. get value.
      ///  f(x1,x2,x3,x4) --> z
      const ZDataType & operator () 
	( const X1DataType & x1,
	  const X2DataType & x2,
	  const X3DataType & x3,
	  const X4DataType & x4 )
	const
      {
	static IndexType indexes[4];
	indexes[0] = m_x1mapper( x1 );
	indexes[1] = m_x2mapper( x2 );
	indexes[2] = m_x3mapper( x3 );
	indexes[3] = m_x4mapper( x4 );
	
	return m_zarray[ indexes ];
      }

      /// function-like interface. set value.
      ///  f(x,y) = z
      ZDataType & operator () 
	( const X1DataType & x1,
	  const X2DataType & x2,
	  const X3DataType & x3,
	  const X4DataType & x4 )
      {
	static IndexType indexes[4];
	indexes[0] = m_x1mapper( x1 );
	indexes[1] = m_x2mapper( x2 );
	indexes[2] = m_x3mapper( x3 );
	indexes[3] = m_x4mapper( x4 );
	
	return m_zarray[ indexes ];
      }

    private:
      const X1AxisMapper & m_x1mapper;
      const X2AxisMapper & m_x2mapper;
      const X3AxisMapper & m_x3mapper;
      const X4AxisMapper & m_x4mapper;
      ZArray & m_zarray;

    };

HISTOGRAM_NAMESPACE_END    

#endif // HISTOGRAM_GRIDDATA_4D_H


// version
// $Id$

// End of file 
