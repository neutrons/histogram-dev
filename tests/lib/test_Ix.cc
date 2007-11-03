#include <cstring>
#include <iostream>

#include "histogram/Ix.h"


using namespace DANSE;

typedef Ix<double, unsigned int> Itof;



int test1()
{
  Itof::idatatype a;

  Itof  itof( 1000., 10000, 1000. );

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );

  delete [] itof.intensities;

  return 0;
}

int test2()
{
  Itof::idatatype I[10];

  Itof  itof( 1000., 10000, 1000., I);

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );

  return 0;
}

int main()
{
  test1();
  test2();
}
