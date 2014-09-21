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


#ifndef HISTOGRAM_EVENLYSPACEDGRIDDATA_1D_H
#define HISTOGRAM_EVENLYSPACEDGRIDDATA_1D_H

#include <cassert>

#include "EvenlySpacedAxisMapper.h"
#include "Array_1D.h"
#include "GridData_1D.h"


HISTOGRAM_NAMESPACE_START
    
    /// f(x) on an evenly spaced x axis.
    /// A template struct to hold f(x) histogram-like object.
    /// x is a evenly spaced axis. The values of y are store in an array.
    /// template arguments:
    ///   XDataType: data type of x. usually int or float
    ///   YDataType: data type of y. usually int or float
    ///   YIterator: iterator of y array
    ///   IndexType: data type of index for indexling the y array. Usually unsigned integers.
    /// CAUTION:
    ///
    template <typename XDataType, 
	      typename YDataType, typename YIterator=YDataType *,
	      typename IndexType=unsigned int >
    
    struct EvenlySpacedGridData_1D {
      
      typedef YDataType ydatatype;
      typedef XDataType xdatatype;
      
      YIterator yarray_begin;
      IndexType size;
      XDataType xbegin, xend, xstep;
      
      /// ctor.
      /// This constructor accepts an iterator that points to the beginning of
      /// the y array.
      /// The y array must have a size consistent with that defined
      /// by parameters xbegin, xend, and xstep:
      ///
      ///   size(yarray) = (xend-xbegin)/xstep
      ///
      /// The parameters xbegin, xend, and xstep define the bin boundaries:
      ///
      ///   xbegin, xbegin+xstep, xbegin+2*xstep, ..., xend
      ///
      EvenlySpacedGridData_1D
      ( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep, YIterator i_yarray_begin)
	: xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep )
      {
	assert(xend > xbegin+xstep*2);
	
	size = IndexType( (xend-xbegin)/xstep );
	
	yarray_begin = i_yarray_begin;
	
	m_xmapper = new XMapper( xbegin, xend, xstep );
	m_yarray = new YArray(yarray_begin, size);
	m_dg = new DG( *m_xmapper, *m_yarray );
      }
      
      const YDataType & operator () ( const XDataType & x ) const
      { return (*m_dg)( x ) ; }
      
      YDataType & operator () ( const XDataType & x ) 
      { return (*m_dg)( x ) ; }

      bool isOutofbound(const XDataType &x) const {
	return x<xbegin || x >= xend;
      }
      
      void clear() {m_dg->clear();}
      
      ~EvenlySpacedGridData_1D() { delete m_xmapper; delete m_yarray; delete m_dg; }
      
    private:
      typedef Array_1D< YIterator, YDataType, IndexType> YArray;
      typedef EvenlySpacedAxisMapper< XDataType, IndexType > XMapper;
      typedef GridData_1D< XDataType, EvenlySpacedAxisMapper< XDataType, IndexType >, 
			   YDataType, Array_1D< YIterator, YDataType, IndexType> > DG;
    
      YArray *m_yarray; // Array_1D
      XMapper *m_xmapper;
      DG *m_dg;
    };
    
HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_EVENLYSPACEDGRIDDATA_1D_H


// version
// $Id$

// End of file 
