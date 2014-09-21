#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"
#include "histogram/NdArraySlice.h"


void test1()
{

  USING_HISTOGRAM_NAMESPACE;

  unsigned int counts [ 4*6 ];
  unsigned int shape[2];

  shape[0] = 4; shape[1] = 6;

  typedef NdArray<unsigned int *, unsigned int, unsigned int, size_t, 2> Array_2D;
  Array_2D arr(counts, shape);
  for (int i=0; i<4*6; i++) counts[i] = i;

  typedef NdArraySlice< Array_2D, unsigned int > Slice;
  std::vector< int > s(2);

  s[0] = 2; s[1] = -1;

  Slice slice( arr, s );

  std::vector< unsigned int > indexes(1);
  indexes[0] = 3;
  assert (slice[ indexes ] == 15);
  assert (((const Slice &)slice).operator[] ( indexes ) == 15 );
}


int main()
{
  test1();
}

