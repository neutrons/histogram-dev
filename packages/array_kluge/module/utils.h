// Copyright (C) 2004 Tim Kelley, Jiao Lin California Institute of Technology

#ifndef H_ARRAY_KLUGE_UTILS
#define H_ARRAY_KLUGE_UTILS


namespace 
{
  template <typename T>
    void deleteObjectWDesc( void *ptr, void *desc);

  template <typename T>
    void deleteObject( void *ptr);

  char *journal_channel = "array_kluge";
} 

#include "utils.icc"

#endif // H_ARRAY_KLUGE_UTILS


// version 
// $Id: array_kluge.h 375 2005-08-16 18:44:57Z linjiao $

// End of file 

