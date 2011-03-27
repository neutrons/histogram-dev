#include <cstring>
#include <iostream>

#include "histogram/EvenlySpacedGridData_4D.h"


int test2()
{
  USING_HISTOGRAM_NAMESPACE;

  typedef EvenlySpacedGridData_4D<int, int, int, double, unsigned int> Ipdpt;

  Ipdpt::zdatatype *intensities = new Ipdpt::zdatatype[ 115*8*128*100 ];

  Ipdpt  ipdpt
    ( 1,116,1,
      0,8,1,
      0,128,1,
      1000, 2000, 10.,
      intensities);

  const Ipdpt & cipdpt = ipdpt;

  assert (115*8*128*100 == ipdpt.size);
  
  ipdpt.clear();

  assert(cipdpt(6, 3, 77, 1005) == 0);

  ipdpt( 6,3,77,1005 ) = 5;
  assert(cipdpt(6,3,77,1005) == 5);

  delete [] intensities;

  return 0;
}


int main()
{
  test2();
}
