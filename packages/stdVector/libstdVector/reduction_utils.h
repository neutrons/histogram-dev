// T. M. Kelley tkelley@caltech.edu (c) 2004
#ifndef ARCSREDUCTIONUTILS_H
#define ARCSREDUCTIONUTILS_H

#ifndef PYTHON_INCLUDED
#define PYTHON_INCLUDED
#include "Python.h"
#endif

namespace Reduction
{

    namespace utils
    {
        // general dtor

        template <typename T> void deleteHeapObj( void *ptr);


        // object wrappers

        /// TO DO: Strictly speaking, there's no need to make ObjectWrapper a
        /// template, but it does "simplify" subclassing.
        template <typename T>
        struct ObjectWrapper
        {
            int m_magicNumber;
            int m_type;
            ObjectWrapper( int magicNumber, int type);
            virtual ~ObjectWrapper(){}
        };


        /// ObjectWrapper that wraps a pointer to an instance of an arbitrary 
        /// class T. TWrapper deletes the underlying pointer when its dtor 
        /// is called. This is intended for use with Python, where the 
        /// interpreter will reference count the TWrapper object.
        template <typename T>
        struct TWrapper : public ObjectWrapper<T>
        {
            T *m_pT;
            TWrapper( T *pT, int type, int magicNumber);
            ~TWrapper();
        };

        /// Wrap a  pointer along with a magic number encoding type info
        template <typename T>
        PyObject *wrapObject( T *ptemp, int type, int magicNumber);

        /// Unwrap an object, checking magic number to make sure it's the
        /// expected type. If not expected type, sets Python exception
        /// and returns 0, so CHECK THE RETURNED POINTER please.
        template <typename T>
        T *unwrapObject( PyObject *pycobj, int type); // , int magicNumber);

    } // utils::

} // reduction::

// include template function definitions (no instantiations!)
#define REDUCTION_UTILS_ICC
#include "reduction_utils.icc"
#undef REDUCTION_UTILS_ICC


#endif  // include guard


// version
// $Id: reduction_utils.h 99 2005-07-29 20:23:50Z tim $

// End of file
