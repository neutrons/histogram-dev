#include <cstring>
#include <iostream>

#include "histogram/Ixy.h"


int test1()
{
  using namespace DANSE;

  typedef Ixy<double, double, unsigned int> Iqe;

  Iqe::idatatype a;

  Iqe  iqe( 1.0, 10.0, 1.0,
	    -50, 50, 1. );
  
  iqe.clear();
  assert( iqe(5., 10) == 0 );

  iqe( 5., 10 ) = 5;
  assert( iqe(5., 10) == 5 );

  delete [] iqe.intensities;
  return 0;
}


int test2()
{
  using namespace DANSE;

  typedef Ixy<double, double, unsigned int> Iqe;

  Iqe::idatatype intensities[ 9*100 ];

  Iqe  iqe( 1.0, 10.0, 1.0,
	    -50, 50, 1. ,
	    intensities);

  assert (sizeof(intensities)/sizeof(Iqe::idatatype) == iqe.size );
  
  iqe.clear();
  assert( iqe(5., 10) == 0 );

  iqe( 5., 10 ) = 5;
  assert( iqe(5., 10) == 5 );

  return 0;
}


int main()
{
  test1();
  test2();
}
