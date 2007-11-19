#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/GridData_2D.h"


int main()
{

  using namespace DANSE::Histogram;

  unsigned int counts [ 4*6 ];
  for (int i=0; i<4*6; i++) counts[i] = 0;

  unsigned int shape[2];
  shape[0] = 6; shape[1] = 4;

  typedef NdArray<unsigned int *, unsigned int, unsigned int, size_t, 2> ZArray;
  ZArray zarr(counts, shape);

  typedef EvenlySpacedAxisMapper< double, short > XMapper;
  XMapper xmapper( 3., 9., 1. );

  typedef EvenlySpacedAxisMapper< int, short > YMapper;
  YMapper ymapper( 100, 500, 100 );
  
  
  GridData_2D< 
    double, XMapper, 
    int, YMapper,
    unsigned int, ZArray > g( xmapper, ymapper, zarr );

  assert ( g(5.5, 100) == 0 );

  counts [20] = 20;
  assert ( g(8.5, 150) == 20 );

  g(8.5, 150) = 30;
  return 0;
}

