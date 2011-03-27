#include <cassert>
#include <cstring>
#include <iostream>

#include "histogram/NdArray.h"


void test1()
{

  USING_HISTOGRAM_NAMESPACE;

  unsigned int counts [ 4*6 ];
  short shape[2];

  shape[0] = 4; shape[1] = 6;

  NdArray<unsigned int *, unsigned int, short, size_t, 2> arr(counts, shape);

  // test method "clear"
  for (int i=0; i<4*6; i++) counts[i] = 1;
  arr.clear();
  for (int i=0; i<4*6; i++) assert(counts[i]==0);

  short indexes[2];

  indexes[0] = 2; indexes[1] = 3;

  assert (arr[indexes] == 0);
  arr[indexes] += 10;

  assert (arr[indexes] == 10);

  counts[10] = 5;
  indexes[0] = 1; indexes[1] = 4;
  assert (arr[indexes] == 5);

  indexes[0] = 1; indexes[1] = 100;
  try {
    arr[indexes];
  }
  catch (OutOfBound &o) {
    std::cout << "good. catch exception: " << o.what() << std::endl;
  }

  std::cout << "test of NdArray passed" << std::endl;
}



void test2()
{

  USING_HISTOGRAM_NAMESPACE;

  unsigned int counts [ 4*6 ];
  short shape[2];

  shape[0] = 4; shape[1] = 6;

  NdArray<unsigned int *, unsigned int, short, size_t, 2> arr(counts, shape);

  // test method "clear"
  for (int i=0; i<4*6; i++) counts[i] = 1;
  arr.clear();
  for (int i=0; i<4*6; i++) assert(counts[i]==0);

  std::vector<short> indexes(2);

  indexes[0] = 2; indexes[1] = 3;

  assert (arr[indexes] == 0);
  arr[indexes] += 10;

  assert (arr[indexes] == 10);

  counts[10] = 5;
  indexes[0] = 1; indexes[1] = 4;
  assert (arr[indexes] == 5);

  indexes[0] = 1; indexes[1] = 100;
  try {
    arr[indexes];
  }
  catch (OutOfBound &o) {
    std::cout << "good. catch exception: " << o.what() << std::endl;
  }

  std::cout << "test of NdArray passed" << std::endl;
}






int main()
{
  test1();
  test2();
  return 0;
}
