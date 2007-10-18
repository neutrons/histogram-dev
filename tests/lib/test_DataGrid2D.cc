#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/DataGrid2D.h"


int main()

{

  using namespace DANSE;

  unsigned int counts [ 4*6 ];
  for (int i=0; i<4*6; i++) counts[i] = 0;

  short shape[2];
  shape[0] = 6; shape[1] = 4;

  typedef NdArray<unsigned int *, unsigned int, short, size_t> ZArray;
  ZArray zarr(counts, shape, 2);

  typedef EvenlySpacedAxisMapper< double, short > XMapper;
  XMapper xmapper( 3., 9., 1. );

  typedef EvenlySpacedAxisMapper< int, short > YMapper;
  YMapper ymapper( 100, 500, 100 );
  
  
  DataGrid2D< short, 
    double, XMapper, 
    int, YMapper,
    unsigned int, ZArray > g( xmapper, ymapper, zarr );

  assert ( g(5.5, 100) == 0 );

  counts [20] = 20;
  assert ( g(8.5, 150) == 20 );
  return 0;
}
