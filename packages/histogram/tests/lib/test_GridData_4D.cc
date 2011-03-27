#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/GridData_4D.h"


int main()
{

  USING_HISTOGRAM_NAMESPACE;

  unsigned int counts [ 3*4*5*6 ];
  for (int i=0; i<3*4*5*6; i++) counts[i] = 0;

  unsigned int shape[4];
  shape[0] = 3; shape[1] = 4; shape[2] = 5; shape[3] = 6;

  typedef NdArray<unsigned int *, unsigned int, unsigned int, size_t, 4> ZArray;
  ZArray zarr(counts, shape);

  typedef EvenlySpacedAxisMapper< double, short > X1Mapper;
  X1Mapper x1mapper( 3., 6., 1. );

  typedef EvenlySpacedAxisMapper< int, short > X2Mapper;
  X2Mapper x2mapper( 1, 5, 1 );
  
  typedef EvenlySpacedAxisMapper< int, short > X3Mapper;
  X3Mapper x3mapper( 100, 600, 100 );
  
  typedef EvenlySpacedAxisMapper< double, short > X4Mapper;
  X4Mapper x4mapper( 3000., 9000., 1000 );
  
  
  typedef GridData_4D<double, X1Mapper, int, X2Mapper, int, X3Mapper, double, X4Mapper,
    unsigned int, ZArray > GD4;
  GD4 g( x1mapper, x2mapper, x3mapper, x4mapper, zarr );
  const GD4 & cg = g;

  assert ( cg(5.5, 1, 105, 3000) == 0 );

  counts [120] = 20;
  assert ( cg(4.5, 1, 100, 3000) == 20 );

  g(4.5, 1, 100, 3000) = 30;
  assert ( cg(4.5, 1, 100, 3000) == 30 );
  assert ( counts[120] == 30 );
  return 0;

}

