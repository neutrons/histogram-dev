// -*- C++ -*-
// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef ARCSSTDVECTORUTILS_H
#define ARCSSTDVECTORUTILS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif
#ifndef VECTOR_INCLUDED
#define VECTOR_INCLUDED
#include <vector>
#endif

namespace ARCSStdVector
{
    struct ObjectWrapper
    {
        int m_magicNumber;
        int m_type;
        ObjectWrapper( int magicNumber, int type);
        virtual ~ObjectWrapper(){}
    };


    template <typename NumT>
    struct VectorWrapper : public ObjectWrapper
    {
        std::vector<NumT> *m_pvec;
      /// does this object own the underlying std::vector?
      /// if yes, we need to destroy that vector in the dtor
      /// if not, we leave it alone.
      /// take a look at the subclass VectorProxy 
        bool m_isowner; 
        VectorWrapper( std::vector<NumT> *pvec, int type, bool isowner = true);
        ~VectorWrapper();
    };

    template <typename Iterator>
    struct IteratorWrapper : public ObjectWrapper
    {
        Iterator *m_pit;
        IteratorWrapper( Iterator *pit, int type);
        ~IteratorWrapper();
    };


    /// Wrap a vector along with a magic number encoding type info
    template <typename NumT>
    PyObject *wrapVector( std::vector<NumT> *pvec, int type);

    /// Unwrap a vector, checking magic number to make sure it's the
    /// expected type. If not expected type, sets Python exception
    /// and returns 0, so CHECK THE RETURNED POINTER please.
    template <typename NumT>
    std::vector<NumT> *unwrapVector( PyObject *pycobj, int type);

    /// Wrap an iterator, tuck in a magic number encoding type info.
    template <typename Iterator>
    PyObject *wrapIterator( Iterator *pit, int type);

    /// Unwrap an iterator pointer, checking magic number to make sure
    /// it's the expected type. If not expected type, sets Python exception
    /// and returns 0, so CHECK THE RETURNED POINTER please.
    template <typename Iterator>
    Iterator *unwrapIterator( PyObject *pypit, int type);

}

#include "utils.icc"

#endif



// version
// $Id: utils.h 118 2006-04-17 06:41:49Z jiao $

// End of file
