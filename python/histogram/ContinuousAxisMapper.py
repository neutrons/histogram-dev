#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


## \package histogram::ContinuousAxisMapper
##
## provides an axis mapper that maps value to axis index for continous axis
##
## The axis bins are not necessarily evenly spaced.


from AxisMapper import AxisMapper

class ContinuousAxisMapper(AxisMapper):

    """
    map a value in an continuous Axis to a index.

    The axis bins are not necessarily evenly spaced.
    """

    def __init__(self, binBoundaries=None):
        self._bb = binBoundaries
        return
    

    def __call__(self, value):
        return findCellIndex( value, self._bb )
        

    pass # end of ContinuousAxisMapper



class SmallArrayError(Exception): pass
class OutOfBoundError(Exception): pass


def findCellIndex( value, arr ):
    
    if (len(arr) < 2 ) : raise SmallArrayError
    if (value< arr[0] or value > arr[-1]):  raise OutOfBoundError
    if (arr[-1] < arr[0]) : raise ValueError, "array must be ascending" 

    n = len( arr )

    i,j,k =0, n/2, n-1

    while (i!=j and j!=k) :
	middle = arr[j]
        if (middle < value) : i = j; j = (i+k)/2
        elif (value < middle):  k = j; j = (i+k)/2
        else : return j
        continue
      
    if (i==j):  return i
    return j



def testFindCellIndex( ):

    arr=[1,3,5,7]

    assert findCellIndex( 4, arr ) == 1

    arr=[1,3,5,8, 10]
    
    assert findCellIndex( 9, arr ) == 3
    return


def test():
    testFindCellIndex()
    return


if __name__ == "__main__": test()
