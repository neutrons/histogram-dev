// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               T. M. Kelley
//                        California Institute of Technology
//                        (C) 2004-2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <portinfo>
#include <Python.h>

#include "bindings.h"
#include "ctor_bdgs.h"
#include "proxy_bdgs.h"
#include "iterators.h"
#include "misc.h"      
#include "numarray_bdgs.h"
#include "pylist2vector.h"
#include "reduceSum_bdgs.h"
#include "slice_bdgs.h"
#include "ufuncs.h"
#include "vector2pylist.h"
#include "vectorCast_bdgs.h"
#include "vec_scalar_arith_bdgs.h"
#include "vec_vec_arith_bdgs.h"

// the method table

struct PyMethodDef pystdVector_methods[] = {

    // ctor
    {stdVector::stdVector_ctor__name__, stdVector::stdVector_ctor, 
     METH_VARARGS, stdVector::stdVector_ctor__doc__},
    {stdVector::stdVector_copy_ctor1__name__, stdVector::stdVector_copy_ctor1, 
     METH_VARARGS, stdVector::stdVector_copy_ctor1__doc__},

    {stdVector::stdVector_copy__name__, stdVector::stdVector_copy, 
     METH_VARARGS, stdVector::stdVector_copy__doc__},

    // for external std::vector
    {stdVector::stdVector_proxy__name__, stdVector::stdVector_proxy,
     METH_VARARGS, stdVector::stdVector_proxy__doc__},

    // utils, tests, etc.
    {pystdVector_copyright__name__, pystdVector_copyright,
     METH_VARARGS, pystdVector_copyright__doc__},
    {pystdVector_testcobj__name__, pystdVector_testcobj,
     METH_VARARGS, pystdVector_testcobj__doc__},
    {pystdVector_printCArray__name__, pystdVector_printCArray,
     METH_VARARGS, pystdVector_printCArray__doc__},
    {pystdVector_printIterator__name__, pystdVector_printIterator,
     METH_VARARGS, pystdVector_printIterator__doc__},

    // iterators
    {pystdVector_iterator__name__, pystdVector_iterator,
     METH_VARARGS, pystdVector_iterator__doc__},
    {pystdVector_begin__name__, pystdVector_begin,
     METH_VARARGS, pystdVector_begin__doc__},
    {pystdVector_end__name__, pystdVector_end,
     METH_VARARGS, pystdVector_end__doc__},
    {pystdVector_iteratorEqual__name__, pystdVector_iteratorEqual,
     METH_VARARGS, pystdVector_iteratorEqual__doc__},
    {pystdVector_increment__name__, pystdVector_increment,
     METH_VARARGS, pystdVector_increment__doc__},

    // ufuncs
    {stdVector::accumPlus__name__, stdVector::accumPlus,
     METH_VARARGS, stdVector::accumPlus__doc__},
    {stdVector::size__name__, stdVector::size,
     METH_VARARGS, stdVector::size__doc__},
    {stdVector::voidPtr__name__, stdVector::voidPtr,
     METH_VARARGS, stdVector::voidPtr__doc__},
    {stdVector::assign1__name__, stdVector::assign1,
     METH_VARARGS, stdVector::assign1__doc__},
    {stdVector::square__name__, stdVector::square,
     METH_VARARGS, stdVector::square__doc__},
    {stdVector::sqrt__name__, stdVector::sqrrt,
     METH_VARARGS, stdVector::sqrt__doc__},

    {stdVector::ReduceSum2d__name__, stdVector::ReduceSum2d, 
     METH_VARARGS, stdVector::ReduceSum2d__doc__},
    {stdVector::ReduceSum3d__name__, stdVector::ReduceSum3d, 
     METH_VARARGS, stdVector::ReduceSum3d__doc__},

    // castVector
    {stdVector::vectorCast__name__, stdVector::vectorCast,
     METH_VARARGS, stdVector::vectorCast__doc__},

    // convert vector <--> list
    {pystdVector_pylist2vector__name__, pystdVector_pylist2vector,
     METH_VARARGS, pystdVector_pylist2vector__doc__},
    {pystdVector_vector2pylist__name__, pystdVector_vector2pylist,
     METH_VARARGS, pystdVector_vector2pylist__doc__},

    // vector-scalar arithmetic
    {pystdVector_add_scalar_vec__name__, pystdVector_add_scalar_vec,
     METH_VARARGS, pystdVector_add_scalar_vec__doc__},
    {pystdVector_mult_scalar_vec__name__, pystdVector_mult_scalar_vec,
     METH_VARARGS, pystdVector_mult_scalar_vec__doc__},

    // vector-vector arithmetic
    {stdVector::vectorPlusEquals__name__, stdVector::vectorPlusEquals,
     METH_VARARGS, stdVector::vectorPlusEquals__doc__},
    {stdVector::vectorMinusEquals__name__, stdVector::vectorMinusEquals,
     METH_VARARGS, stdVector::vectorMinusEquals__doc__},
    {stdVector::vectorTimesEquals__name__, stdVector::vectorTimesEquals,
     METH_VARARGS, stdVector::vectorTimesEquals__doc__},
    {stdVector::vectorDivideEquals__name__, stdVector::vectorDivideEquals,
     METH_VARARGS, stdVector::vectorDivideEquals__doc__},

    {stdVector::vectorPlus__name__, stdVector::vectorPlus,
     METH_VARARGS, stdVector::vectorPlus__doc__},
    {stdVector::vectorMinus__name__, stdVector::vectorMinus,
     METH_VARARGS, stdVector::vectorMinus__doc__},
    {stdVector::vectorTimes__name__, stdVector::vectorTimes,
     METH_VARARGS, stdVector::vectorTimes__doc__},
    {stdVector::vectorDivide__name__, stdVector::vectorDivide,
     METH_VARARGS, stdVector::vectorDivide__doc__},

    // numarray
    {stdVector::asNumarray__name__, stdVector::asNumarray,
     METH_VARARGS, stdVector::asNumarray__doc__},

    // slice bindings
    {stdVector::extractSlice__name__, stdVector::extractSlice,
     METH_VARARGS, stdVector::extractSlice__doc__},
    {stdVector::slice_ctor3__name__, stdVector::slice_ctor3,
     METH_VARARGS, stdVector::slice_ctor3__doc__},
    {stdVector::slice_magicNumber__name__, stdVector::slice_magicNumber,
     METH_VARARGS, stdVector::slice_magicNumber__doc__},
    {stdVector::slice_start__name__, stdVector::slice_start,
     METH_VARARGS, stdVector::slice_start__doc__},
    {stdVector::slice_size__name__, stdVector::slice_size,
     METH_VARARGS, stdVector::slice_size__doc__},
    {stdVector::slice_stride__name__, stdVector::slice_stride,
     METH_VARARGS, stdVector::slice_stride__doc__},


// Sentinel
    {0, 0}
};

// version
// $Id: bindings.cc 118 2006-04-17 06:41:49Z jiao $

// End of file
