#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"


int main()

{

  using namespace DANSE;

  unsigned int counts [ 4*6 ];
  for (int i=0; i<4*6; i++) counts[i] = 0;
  short shape[2];

  shape[0] = 4; shape[1] = 6;

  NdArray<unsigned int *, unsigned int, short, size_t> arr(counts, shape, 2);

  short indexes[2];
  indexes[0] = 2; indexes[1] = 3;

  std::cout << arr[ indexes ] << std::endl;
  assert (arr[indexes] == 0);

  arr[indexes] += 10;

  std::cout << arr[ indexes ] << std::endl;
  assert (arr[indexes] == 10);

  counts[10] = 5;
  indexes[0] = 1; indexes[1] = 4;
  assert (arr[indexes] == 5);

  std::cout << "test of NdArray passed" << std::endl;
  return 0;
}
