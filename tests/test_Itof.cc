#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/DataGrid1D.h"


using namespace DANSE;

class Itof {

public:
  Itof( double tofbegin, double tofend, double tofstep )
  {

    assert(tofend > tofbegin+tofstep*2);
    
    m_size = (tofend-tofbegin)/tofstep ;
    m_counts = new unsigned int[ m_size ];
    m_shape[0] = m_size;
    m_mapper = new TofMapper( tofbegin, tofend, tofstep );
    m_Iarray = new IArray(m_counts, m_shape, 1);
    m_dg = new DG( *m_mapper, *m_Iarray );
  }

  ~Itof() 
  {
    delete [] m_counts;
    delete m_mapper;
    delete m_Iarray;
    delete m_dg;
  }

  const unsigned int & operator () (const double &tof) const 
  {
    return (*m_dg)( tof );
  }
  
  unsigned int & operator () (const double &tof) 
  {
    return (*m_dg)( tof );
  }
  
private:
  size_t m_size;
		   unsigned int m_shape[1];	   
  unsigned int *m_counts;
  typedef NdArray< unsigned int *, unsigned int, unsigned int, size_t> IArray;
  typedef EvenlySpacedAxisMapper< double, unsigned int > TofMapper;
  typedef DataGrid1D< unsigned int, double, TofMapper, 
		      unsigned int, IArray> DG;
  TofMapper *m_mapper;
  IArray *m_Iarray;
  DG *m_dg;
};



int main()

{
  Itof  itof( 1000., 10000, 1000. );

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );

  return 0;
}
