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


#ifndef H_DANSE_DATAGRID2D
#define H_DANSE_DATAGRID2D


namespace DANSE {

  // associate a 1d data array and 1d axis
  template < typename IndexType, 
	     typename XDataType, typename XAxisMapper, 
	     typename YDataType, typename YAxisMapper,
	     typename ZDataType, typename NdArray>
  class DataGrid2D {

    /// how to assert AxisMapper::IndexType == NdArray::Size?

  public:

    DataGrid2D( const XAxisMapper & xmapper, 
		const YAxisMapper & ymapper,
		NdArray & zarray ) :
      m_xmapper( xmapper ),  m_ymapper( ymapper ),
      m_zarray( zarray )
    {
    }

    void clear() { m_zarray.clear(); }

    // 
    const ZDataType & operator () ( const XDataType & x, const YDataType &y ) const
    {
      m_indexes[0] = m_xmapper( x );
      m_indexes[1] = m_ymapper( y );

      return m_zarray[ m_indexes ];
    }

    ZDataType & operator () ( const XDataType & x, const YDataType & y )
    {
      m_indexes[0] = m_xmapper( x );
      m_indexes[1] = m_ymapper( y );

      return m_zarray[ m_indexes ];
    }

  private:
    const XAxisMapper & m_xmapper;
    const YAxisMapper & m_ymapper;
    NdArray & m_zarray;

    // temp data
    IndexType m_indexes[2];

  };

}

#endif


// version
// $Id$

// End of file 
