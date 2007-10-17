#include <cstring>
#include <iostream>

#include "histogram/Ix.h"

int main()

{
  using namespace DANSE;

  Ix<double, unsigned int>  itof( 1000., 10000, 1000. );

  itof(3000)=0.;
  assert( itof(3000) == 0 );

  itof(3000)+=5.;
  assert( itof(3000) == 5 );
  
  return 0;
}
