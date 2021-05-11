// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com
//


#ifndef HISTOGRAM_EVENLYSPACEDGRIDDATA_3D_H
#define HISTOGRAM_EVENLYSPACEDGRIDDATA_3D_H

#include <cassert>
#include "NdArray.h"
#include "EvenlySpacedAxisMapper.h"
#include "GridData_3D.h"


HISTOGRAM_NAMESPACE_START

    /// f(x1,x2,x3) on evenly spaced axis {xi}, i=1,2,3.
    /// A template struct to hold f(x1,x2,x3) histogram-like data object.
    /// x1,x2,x3 are evenly spaced axes.
    /// The values of z are stored in an array.
    /// template arguments:
    ///   X1DataType: data type of x1. usually int or float
    ///   X2DataType: data type of x2. usually int or float
    ///   X3DataType: data type of x3. usually int or float
    ///   ZDataType: data type of z. usually int or float
    ///   ZIterator: iterator of z array
    ///   IndexType: data type of index for indexling the z array. Usually unsigned integers.
    /// CAUTION:
    ///
    template <typename X1DataType,
              typename X2DataType,
              typename X3DataType,
              typename ZDataType, typename ZIterator = ZDataType *,
              typename IndexType=unsigned int >

    struct EvenlySpacedGridData_3D {

      typedef ZDataType zdatatype;
      typedef X1DataType x1datatype;
      typedef X2DataType x2datatype;
      typedef X3DataType x3datatype;

      ZIterator zarray_begin;
      IndexType size, shape[3];
      X1DataType x1begin, x1end, x1step;
      X2DataType x2begin, x2end, x2step;
      X3DataType x3begin, x3end, x3step;

      /// ctor.
      /// This constructor accepts an iterator that points to the beginning
      /// of the z array.
      /// The zarray_begin array must have consistent shape with that defined
      /// by parameters {xibegin, xiend, xistep}.
      ///
      ///   size(zarray) = \Pi_{i} [(xiend-xibegin)/xistep] 
      ///
      /// zarray is a 1D array, but it can be seen as a 3D array of shape
      ///
      ///    [ (xiend-xibegin)/xistep ], i=1..3
      ///
      /// Note: the x2 index runs faster x1 index.
      ///
      /// The parameters x1begin, x1end, and x1step define the x1 bin boundaries:
      ///
      ///   x1begin, x1begin+x1step, x1begin+2*x1step, ..., x1end
      ///
      EvenlySpacedGridData_3D
      ( X1DataType i_x1begin, X1DataType i_x1end, X1DataType i_x1step,
        X2DataType i_x2begin, X2DataType i_x2end, X2DataType i_x2step,
        X3DataType i_x3begin, X3DataType i_x3end, X3DataType i_x3step,
        ZIterator i_zarray_begin)
        : x1begin(i_x1begin), x1end( i_x1end ), x1step( i_x1step ),
          x2begin(i_x2begin), x2end( i_x2end ), x2step( i_x2step ),
          x3begin(i_x3begin), x3end( i_x3end ), x3step( i_x3step )
      {
        assert(x1end > x1begin+x1step*2);
        assert(x2end > x2begin+x2step*2);
        assert(x3end > x3begin+x3step*2);

        shape[0] = IndexType( (x1end-x1begin)/x1step );
        shape[1] = IndexType( (x2end-x2begin)/x2step );
        shape[2] = IndexType( (x3end-x3begin)/x3step );

        size = shape[0] * shape[1] * shape[2];
        zarray_begin = i_zarray_begin;

        m_x1mapper = new X1Mapper( x1begin, x1end, x1step );
        m_x2mapper = new X2Mapper( x2begin, x2end, x2step );
        m_x3mapper = new X3Mapper( x3begin, x3end, x3step );
        m_zarray = new ZArray(zarray_begin, shape);
        m_dg = new DG( *m_x1mapper, *m_x2mapper, *m_x3mapper, *m_zarray );
      } 

  ZDataType operator ()
	( const X1DataType & x1,
	  const X2DataType & x2,
	  const X3DataType & x3)
    const
      {
        if (isOutofbound(x1,x2,x3)) {
          return 0;
        }
        return (*m_dg)( x1,x2,x3 ) ;
      }

  ZDataType & operator ()
	( const X1DataType & x1,
	  const X2DataType & x2,
	  const X3DataType & x3)
      {
        if (isOutofbound(x1,x2,x3)) {
          std::ostringstream oss;
          oss << "**set** EvenlySpacedGridData_3D["
              << x1 << ", " << x2 << ", " << x3 << "]";
          throw OutOfBound(oss.str().c_str());
        }
        return (*m_dg)( x1,x2,x3 ) ;
      }

      bool isOutofbound
	( const X1DataType & x1,
	  const X2DataType & x2,
	  const X3DataType & x3)
	const
      {
        return x1 < x1begin || x1 >= x1end || \
          x2 < x2begin || x2 >= x2end ||        \
          x3 < x3begin || x3 >= x3end ;
      }

      void clear() {
        m_dg->clear();
      }

      ~EvenlySpacedGridData_3D()
      {
        delete m_x1mapper; delete m_x2mapper; delete m_x3mapper;
        delete m_zarray;
        delete m_dg;
      }

    private:
      typedef NdArray< ZIterator, ZDataType, IndexType, size_t, 3> ZArray;
      typedef EvenlySpacedAxisMapper< X1DataType, IndexType > X1Mapper;
      typedef EvenlySpacedAxisMapper< X2DataType, IndexType > X2Mapper;
      typedef EvenlySpacedAxisMapper< X3DataType, IndexType > X3Mapper;
      typedef GridData_3D<X1DataType, X1Mapper, 
			  X2DataType, X2Mapper,
			  X3DataType, X3Mapper,
			  ZDataType, ZArray,
			  IndexType > DG;
      ZArray *m_zarray; // NdArray
      X1Mapper *m_x1mapper;
      X2Mapper *m_x2mapper;
      X3Mapper *m_x3mapper;
      DG *m_dg;
    };

HISTOGRAM_NAMESPACE_END


#endif // HISTOGRAM_EVENLYSPACEDGRIDDATA_3D_H

// End of file
