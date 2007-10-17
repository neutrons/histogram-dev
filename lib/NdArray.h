// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef H_DANSE_NDARRAY
#define H_DANSE_NDARRAY


namespace DANSE {

  template <typename Iterator, typename DataType, typename Size, typename SuperSize>
  class NdArray {

  public:
    
    typedef DataType datatype;
    
    // array shape must have 'ndim' elements
    NdArray( Iterator it, Size * shape, int ndim) :
      m_it(it), m_ndim( ndim ), m_shape( new Size[ndim] ) {

      m_size1D = 1;

      for (int i=0; i<ndim; i++) {
	m_shape[i] = shape[i];
	m_size1D *= shape[i];
      }
    }

    ~NdArray() { delete [] m_shape; }

    // indexes must have 'ndim' elements
    const DataType & operator [] ( Size *indexes ) const
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }

    DataType & operator [] ( Size *indexes ) 
    {
      SuperSize ind = _1dindex( indexes );
      return *(m_it+ind);
    }

    void clear() 
    {
      for (Iterator it = m_it; it < m_it + m_size1D; it++ ) 
	*it = 0;
    }

  private:
    Iterator m_it;
    int  m_ndim;
    Size *m_shape;
    SuperSize m_size1D;
    SuperSize _1dindex( Size *indexes ) const 
    {
      SuperSize ind = 0; // what if this get out of bound of largest integer?
      SuperSize N = 1;
      for (int i=m_ndim-1; i>=0; i--  ) {
        ind += N * indexes[ i ]; 
        N *= m_shape[ i ];
      }
      return ind;
    }
};

}

#endif


// version
// $Id$

// End of file 
