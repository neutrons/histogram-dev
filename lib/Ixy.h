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


#ifndef H_DANSE_HISTOGRAM_IXY
#define H_DANSE_HISTOGRAM_IXY

#include <cassert>

#include "NdArray.h"
#include "EvenlySpacedAxisMapper.h"
#include "DataGrid2D.h"


namespace DANSE {

  /// Ixy
  /// A template struct to hold I(x,y) histogram
  /// x,y are evenly spaced axes.
  /// I is intensity-like quantity
  /// A new array is created and kept in the data object;
  /// please remember to delete it!!!
  template <typename XDataType, typename YDataType, 
	    typename IDataType, typename IIterator = IDataType *,
	    typename IndexType=unsigned int >
  struct Ixy {

    typedef IDataType idatatype;
    typedef XDataType xdatatype;
    typedef YDataType ydatatype;
    
    typedef DataGrid2D< IndexType, 
			XDataType, EvenlySpacedAxisMapper< XDataType, IndexType >, 
			YDataType, EvenlySpacedAxisMapper< YDataType, IndexType >, 
			IDataType, NdArray< IIterator, IDataType, IndexType, size_t> > DG;
  
    IIterator intensities;
    IndexType size, shape[2];
    XDataType xbegin, xend, xstep;
    YDataType ybegin, yend, ystep;  

    Ixy( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep,
	 YDataType i_ybegin, YDataType i_yend, YDataType i_ystep)
      : xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep ),
	ybegin(i_ybegin), yend( i_yend ), ystep( i_ystep )
    {
      assert(xend > xbegin+xstep*2);
      assert(yend > ybegin+ystep*2);
    
      //std::cout << xend << ", " << xbegin << ", " << xstep << ", "
      //<<  (xend-xbegin)/xstep  << std::endl;
      
      shape[0] = IndexType( (xend-xbegin)/xstep );
      shape[1] = IndexType( (yend-ybegin)/ystep );

      size = shape[0] * shape[1];

      intensities = new IDataType[ size ];

      m_xmapper = new XMapper( xbegin, xend, xstep );
      m_ymapper = new YMapper( ybegin, yend, ystep );
      m_Iarray = new IArray(intensities, shape, 2);
      m_dg = new DG( *m_xmapper, *m_ymapper, *m_Iarray );
    }    

    
    /// ctor
    /// This constructor accepts an iterator that points to a 1D array to hold
    /// intensities.
    /// The intensities array must have consistent shape with that defined
    /// by parameters xbegin, xend, xstep, ybegin, yend, ystep.
    Ixy( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep,
	 YDataType i_ybegin, YDataType i_yend, YDataType i_ystep,
	 IIterator i_intensities)
      : xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep ),
	ybegin(i_ybegin), yend( i_yend ), ystep( i_ystep )
    {
      assert(xend > xbegin+xstep*2);
      assert(yend > ybegin+ystep*2);
    
      shape[0] = IndexType( (xend-xbegin)/xstep );
      shape[1] = IndexType( (yend-ybegin)/ystep );

      size = shape[0] * shape[1];

      intensities = i_intensities;

      m_xmapper = new XMapper( xbegin, xend, xstep );
      m_ymapper = new YMapper( ybegin, yend, ystep );
      m_Iarray = new IArray(intensities, shape, 2);
      m_dg = new DG( *m_xmapper, *m_ymapper, *m_Iarray );
    }    

    const IDataType & operator () ( const XDataType & x, const YDataType & y ) const
    { return (*m_dg)( x,y ) ; }

    IDataType & operator () ( const XDataType & x, const YDataType & y ) 
    { return (*m_dg)( x,y ) ; }

    void clear() {m_dg->clear();}

    ~Ixy() { delete m_xmapper; delete m_ymapper, delete m_Iarray; delete m_dg; }
    
  private:
    typedef NdArray< IIterator, IDataType, IndexType, size_t> IArray;
    typedef EvenlySpacedAxisMapper< XDataType, IndexType > XMapper;
    typedef EvenlySpacedAxisMapper< YDataType, IndexType > YMapper;
    IArray *m_Iarray; // NdArray 
    XMapper *m_xmapper;
    YMapper *m_ymapper;
    DG *m_dg;
    
  };

} // namespace DANSE


#endif



// version
// $Id$

// End of file 
