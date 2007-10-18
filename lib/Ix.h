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


#ifndef H_DANSE_HISTOGRAM_IX
#define H_DANSE_HISTOGRAM_IX

#include <cassert>

#include "NdArray.h"
#include "EvenlySpacedAxisMapper.h"
#include "DataGrid1D.h"


namespace DANSE {

  /// Ix
  /// A template struct to hold I(x) histogram
  /// x is a evenly spaced axis.
  /// I is intensity-like quantity
  /// A new array is created and kept in the data object;
  /// please remember to delete it!!!
  template <typename XDataType, 
	    typename IDataType, typename IIterator=IDataType *,
	    typename IndexType=unsigned int >
  struct Ix {

    typedef IDataType idatatype;
    typedef XDataType xdatatype;
    
    typedef DataGrid1D< IndexType, XDataType, EvenlySpacedAxisMapper< XDataType, IndexType >, 
			IDataType, NdArray< IIterator, IDataType, IndexType, size_t> > 
    DG;

    IIterator intensities;
    IndexType size;
    XDataType xbegin, xend, xstep;

    Ix( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep )
      : xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep )
    {
      assert(xend > xbegin+xstep*2);
    
      size = IndexType( (xend-xbegin)/xstep );


      IndexType shape[1]; shape[0] = size;
      intensities = new IDataType[ size ];

      m_xmapper = new XMapper( xbegin, xend, xstep );
      m_Iarray = new IArray(intensities, shape, 1);
      m_dg = new DG( *m_xmapper, *m_Iarray );
    }    

    /// ctor
    /// This constructor accepts an iterator that points to a 1D array to hold
    /// intensities.
    /// The intensities array must have consistent shape with that defined
    /// by parameters xbegin, xend, and xstep.
    Ix( XDataType i_xbegin, XDataType i_xend, XDataType i_xstep, IIterator i_intensities)
      : xbegin(i_xbegin), xend( i_xend ), xstep( i_xstep )
    {
      assert(xend > xbegin+xstep*2);
    
      size = IndexType( (xend-xbegin)/xstep );

      IndexType shape[1]; shape[0] = size;
      intensities = i_intensities;

      m_xmapper = new XMapper( xbegin, xend, xstep );
      m_Iarray = new IArray(intensities, shape, 1);
      m_dg = new DG( *m_xmapper, *m_Iarray );
    }

    const IDataType & operator () ( const XDataType & x ) const
    { return (*m_dg)( x ) ; }

    IDataType & operator () ( const XDataType & x ) 
    { return (*m_dg)( x ) ; }

    void clear() {m_dg->clear();}

    ~Ix() { delete m_xmapper; delete m_Iarray; delete m_dg; }
    
  private:
    typedef NdArray< IIterator, IDataType, IndexType, size_t> IArray;
    typedef EvenlySpacedAxisMapper< XDataType, IndexType > XMapper;
    IArray *m_Iarray; // NdArray 
    XMapper *m_xmapper;
    DG *m_dg;
    
  };

} // namespace DANSE


#endif



// version
// $Id$

// End of file 
