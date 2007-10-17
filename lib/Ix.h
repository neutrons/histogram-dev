#ifndef H_DANSE_HISTOGRAM_IX
#define H_DANSE_HISTOGRAM_IX

#include <cassert>

#include "NdArray.h"
#include "EvenlySpacedAxisMapper.h"
#include "DataGrid1D.h"


using namespace DANSE;


///Ix
///A template to create I(x) histogram
///x is a evenly spaced axis.
///I is intensity-like quantity
template <typename XDataType, typename IDataType>
class Ix {

public:
  Ix( XDataType xbegin, XDataType xend, XDataType xstep )
  {

    assert(xend > xbegin+xstep*2);
    
    m_size = (xend-xbegin)/xstep ;
    m_intensity = new IDataType[ m_size ];
    m_shape[0] = m_size;
    m_mapper = new XMapper( xbegin, xend, xstep );
    m_Iarray = new IArray(m_intensity, m_shape, 1);
    m_dg = new DG( *m_mapper, *m_Iarray );

  }

  ~Ix() 
  {
    delete [] m_intensity;
    delete m_mapper;
    delete m_Iarray;
    delete m_dg;
  }

  const unsigned int & operator () (const XDataType &x) const 
  {
    return (*m_dg)( x );
  }
  
  unsigned int & operator () (const XDataType &x) 
  {
    return (*m_dg)( x );
  }

  void clear() { m_dg->clear(); }

  IDataType * Iarray() { return m_intensity; }
  
private:
  size_t m_size;
  unsigned int m_shape[1]; 
  IDataType *m_intensity;
  typedef unsigned int IndexType;
  typedef NdArray< IDataType *, IDataType, IndexType, size_t> IArray;
  typedef EvenlySpacedAxisMapper< XDataType, IndexType > XMapper;
  typedef DataGrid1D< IndexType, XDataType, XMapper, 
		      IndexType, IArray> DG;
  XMapper *m_mapper;
  IArray *m_Iarray;
  DG *m_dg;
};



#endif
