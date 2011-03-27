#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/Array_1D.h"
#include "histogram/EvenlySpacedAxisMapper.h"
#include "histogram/GridData_1D.h"


int main()

{

  USING_HISTOGRAM_NAMESPACE;

  unsigned int counts [ 10 ];
  for (int i=0; i<10; i++) counts[i] = 0;

  typedef Array_1D<unsigned int *, unsigned int, size_t> YArray;
  YArray yarr(counts, 10);

  typedef EvenlySpacedAxisMapper< double, short > XMapper;
  XMapper xmapper( 3., 13., 1. );
  
  GridData_1D< double, XMapper, unsigned int, YArray > g( xmapper, yarr );

  assert ( g(5.5) == 0. );
  counts[2] = 1;

  assert ( g(5.5) == 1. );
  
  g(6.5) = 3;
  assert (counts[3] = 3);
  return 0;
}
