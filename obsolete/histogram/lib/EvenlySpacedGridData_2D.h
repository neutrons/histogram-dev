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


#ifndef HISTOGRAM_EVENLYSPACEDGRIDDATA_2D_H
#define HISTOGRAM_EVENLYSPACEDGRIDDATA_2D_H

#include <cassert>

#include "NdArray.h"
#include "EvenlySpacedAxisMapper.h"
#include "GridData_2D.h"


HISTOGRAM_NAMESPACE_START

    /// f(x,y) on evenly spaced axis x and y.
    /// A template struct to hold f(x,y) histogram-like data object.
    /// x,y are evenly spaced axes.
    /// The values of z are stored in an array.
    /// template arguments:
    ///   XDataType: data type of x. usually int or float
    ///   YDataType: data type of y. usually int or float
    ///   ZDataType: data type of z. usually int or float
    ///   ZIterator: iterator of z array
    ///   IndexType: data type of index for indexling the z array. Usually unsigned integers.
    /// CAUTION:
    ///
    template <typename XDataType, 
	      typename YDataType, 
	      typename ZDataType, typename ZIterator = ZDataType *,
	      typename IndexType=unsigned int >
    
    struct EvenlySpacedGridData_2D {
      
      typedef ZDataType zdatatype;
      typedef XDataType xdatatype;
      typedef YDataType ydatatype;
      
      ZIterator zarray_begin;
      IndexType size, shape[2];
      XDataType xbegin, xend, xstep;
      YDataType ybegin, yend, ystep;  

    
      /// ctor.
      /// This constructor accepts an iterator that points to the beginning
      /// of the z array.
      /// The zarray_begin array must have consistent shape with that defined
      /// by parameters xbegin, xend, xstep, ybegin, yend, ystep.
      ///
      ///   size(yarray) = [(xend-xbegin)/xstep]  *  [(yend-ybegin)/ystep]
      ///
      /// zarray is a 1D array, but it can be seen as a 2D array of shape
      ///
      ///   (xend-xbegin)/xstep,  (yend-ybegin)/ystep
      ///
      /// Note: the y index runs faster x index.
      ///
      /// The parameters xbegin, xend, and xstep define the x bin boundaries:
      ///
      ///   xbegin, xbegin+xstep, xbegin+2*xstep, ..., xend
      ///
      EvenlySpacedGridData_2D
      ( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep,
	YDataType i_ybegin, YDataType i_yend, YDataType i_ystep,
	ZIterator i_zarray_begin)
	: xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep ),
	  ybegin(i_ybegin), yend( i_yend ), ystep( i_ystep )
      {
	assert(xend > xbegin+xstep*2);
	assert(yend > ybegin+ystep*2);
    
	shape[0] = IndexType( (xend-xbegin)/xstep );
	shape[1] = IndexType( (yend-ybegin)/ystep );

	size = shape[0] * shape[1];
	
	zarray_begin = i_zarray_begin;

	m_xmapper = new XMapper( xbegin, xend, xstep );
	m_ymapper = new YMapper( ybegin, yend, ystep );
	m_zarray = new ZArray(zarray_begin, shape);
	m_dg = new DG( *m_xmapper, *m_ymapper, *m_zarray );
      } 

      const ZDataType & operator () ( const XDataType & x, const YDataType & y ) const 
      { return (*m_dg)( x,y ) ; }

      ZDataType & operator () ( const XDataType & x, const YDataType & y ) 
      { return (*m_dg)( x,y ) ; }

      bool isOutofbound(const XDataType &x, const YDataType & y) const {
	return x < xbegin || x >= xend || \
	  y < ybegin || y >= yend;
      }
      
      void clear() {m_dg->clear();}

      ~EvenlySpacedGridData_2D() 
      { delete m_xmapper; delete m_ymapper, delete m_zarray; delete m_dg; }
    
    private:
      typedef NdArray< ZIterator, ZDataType, IndexType, size_t, 2> ZArray;
      typedef EvenlySpacedAxisMapper< XDataType, IndexType > XMapper;
      typedef EvenlySpacedAxisMapper< YDataType, IndexType > YMapper;
      typedef GridData_2D<XDataType, XMapper, 
			  YDataType, YMapper,
			  ZDataType, ZArray,
			  IndexType > DG;
  
      ZArray *m_zarray; // NdArray 
      XMapper *m_xmapper;
      YMapper *m_ymapper;
      DG *m_dg;
      
    };

HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_EVENLYSPACEDGRIDDATA_2D_H



// version
// $Id$

// End of file 
