#include <cstring>
#include <iostream>

#include "histogram/EvenlySpacedGridData_2D.h"


int test2()
{
  USING_HISTOGRAM_NAMESPACE;

  typedef EvenlySpacedGridData_2D<double, double, unsigned int> Iqe;

  Iqe::zdatatype intensities[ 9*100 ];

  Iqe  iqe( 1.0, 10.0, 1.0,
	    -50, 50, 1. ,
	    intensities);
  const Iqe & ciqe = iqe;

  assert (sizeof(intensities)/sizeof(Iqe::zdatatype) == iqe.size );
  
  iqe.clear();
  assert( ciqe(5., 10) == 0 );

  iqe( 5., 10 ) = 5;
  assert( ciqe(5., 10) == 5 );

  return 0;
}


int main()
{
  test2();
}
