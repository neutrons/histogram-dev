// -*- C++ -*-
// Copyright (C) 2004 Tim Kelley, Jiao Lin California Institute of Technology

#ifndef H_VPTR2STDVECTORPTR
#define H_VPTR2STDVECTORPTR

#include <vector>
#include "utils.h"

namespace 
{
  template <typename T>
    std::vector<T> *newVector( void *vptr, size_t size);
} 

namespace 
{
  template <typename T>
  std::vector<T> *newVector( void *vptr, size_t size)
  {
    T *ptr = static_cast<T *>(vptr);
    std::vector<T> *result = new std::vector<T>( ptr, ptr+size);

#ifdef DEBUG
    journal::debug_t debug(journal_channel);
    debug << journal::at(__HERE__) << "created pointer" << result << journal::endl;
#endif
    return result;
  }
} // anonymous namespace a slight improvement over static


#endif // H_VPTR2STDVECTORPTR


// version 
// $Id: array_conversion.h 375 2005-08-16 18:44:57Z linjiao $

// End of file 

