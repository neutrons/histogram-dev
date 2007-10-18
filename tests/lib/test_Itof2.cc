#include <cstring>
#include <iostream>

#include "histogram/Ix.h"

int main()
{
  using namespace DANSE;

  typedef Ix<double, unsigned int> Itof;

  Itof::idatatype a;

  Itof  itof( 1000., 10000, 1000. );

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );

  delete [] itof.intensities;
  return 0;
}
