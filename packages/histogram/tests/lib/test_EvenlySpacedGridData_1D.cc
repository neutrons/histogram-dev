#include <cstring>
#include <iostream>

#include "histogram/EvenlySpacedGridData_1D.h"


USING_HISTOGRAM_NAMESPACE;

typedef EvenlySpacedGridData_1D<double, unsigned int> Itof;



int test2()
{
  Itof::ydatatype I[10];

  Itof  itof( 1000., 10000, 1000., I);

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );

  return 0;
}

int main()
{
  test2();
}
