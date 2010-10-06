#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


__doc__ = """

NAME:
  arrShapeUtils
  
PURPOSE:
  utilities dealing with vector shapes

DESCRIPTION:
  datasets are read/write in the form of multi-dimensional matrixes (vectors).
  we need to implement methods that calculate the size of matrix shape,
  verify that indexes are not out of bounds, etc. etc.

HISTORY:
  many methods in here were extracted, combined, reshaped from VectorReader,
  simulation.common.utils

RELATED:

TODOs:
"""


def volume(shape):
    from operator import mul
    return reduce(mul, shape)


def checkLength( vector, length):
    """make sure vector is large enough.
    """
    if vector.size() < length:
        msg = "vector size (%s) is smaller than the requested size (%s)" % \
              ( vector.size(), length)
        raise IndexError, msg
    return 


def checkShape( shape1, shape2 ):
    """check if shape1 is contained in shape2
    """
    if len(shape1) != len(shape2): raise IndexError, "%s and %s do not have the same rank" % (shape1, shape2)
    msg = ''; ok = True

    for i, size in enumerate( shape1):
        if size > shape2[i]:
            ok = False
            msg += 'dimension %s: shape1 size (%s) > shape2 size (%s)\n' % \
                   ( i, size, shape2[i])
    if not ok:
        raise IndexError, msg
    return
