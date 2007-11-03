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


#ifndef H_DANSE_DATAGRID1D
#define H_DANSE_DATAGRID1D


namespace DANSE {

  // associate a 1d data array and 1d axis
  template < typename IndexType, 
	     typename XDataType, typename AxisMapper, 
	     typename YDataType, typename NdArray>
  class DataGrid1D {


    /// how to assert AxisMapper::IndexType == NdArray::Size?

  public:

    DataGrid1D( const AxisMapper & xmapper, NdArray & yarray ) :
      m_xmapper( xmapper ),
      m_yarray( yarray )
    {
    }

    // 
    const YDataType & operator () ( const XDataType & x ) const
    {
      m_indexes[0] = m_xmapper( x );
      return m_yarray[ m_indexes ];
    }

    YDataType & operator () ( const XDataType & x )
    {
      m_indexes[0] = m_xmapper( x );
      return m_yarray[ m_indexes ];
    }

    void clear() { m_yarray.clear(); }

  private:
    const AxisMapper & m_xmapper;
    NdArray & m_yarray;

    // temp data
    IndexType m_indexes[1];

  };

}

#endif


// version
// $Id$

// End of file 
