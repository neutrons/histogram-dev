// -*- C++ -*-
//
// Jiao Lin
// for connecting raw pycobject with pointer to stdvector to Tim's stdVector

#ifndef H_STDVECTOR_VECTORPROXY
#define H_STDVECTOR_VECTORPROXY

#include "Python.h"
#include <vector>


#include "utils.h"

namespace ARCSStdVector {
  
  //! VectorProxy should have the same structure as Tim's VectorWrapper
  /*! The only difference is VectorProxy does not hold onto the underlying 
    pointer.
  */
  template <typename NumT>
  struct VectorProxy : public VectorWrapper<NumT> {
    PyObject * m_underlying_vector_pycobject;
    /// ctor
    /// pvec is the pointer extracted from underlying_vector_pycobject
    /// don't call this ctor directly! only use the following function,
    /// createVectorProxy to create instances of VectorProxy
    VectorProxy( std::vector<NumT> *pvec, int type, PyObject *underlying_vector_pycobject);
    ~VectorProxy();
  };
  
  /// create a proxy for a given vector
  template <typename NumT>
  PyObject *createVectorProxy( PyObject *vector_pycobject, int type);

}


#include "VectorProxy.icc"

#endif // H_STDVECTOR_VECTORPROXY



// version
// $Id: utils.h 141 2005-07-08 22:32:11Z linjiao $

// End of file
