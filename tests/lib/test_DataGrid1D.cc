#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/DataGrid1D.h"


int main()

{

  using namespace DANSE;

  unsigned int counts [ 10 ];
  for (int i=0; i<10; i++) counts[i] = 0;

  short shape[1];
  shape[0] = 10;

  typedef NdArray<unsigned int *, unsigned int, short, size_t> YArray;
  YArray yarr(counts, shape, 1);

  typedef EvenlySpacedAxisMapper< double, short > XMapper;
  XMapper xmapper( 3., 13., 1. );
  
  DataGrid1D< short, double, XMapper, unsigned int, YArray > g( xmapper, yarr );

  assert ( g(5.5) == 0. );
  counts[2] = 1;

  assert ( g(5.5) == 1. );
  
  g(6.5) = 3;
  assert (counts[3] = 3);
  return 0;
}
