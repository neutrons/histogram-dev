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


#ifndef HISTOGRAM_EXCEPTION_H
#define HISTOGRAM_EXCEPTION_H


#include <string>
#include "_macros.h"


HISTOGRAM_NAMESPACE_START

    class Exception: public std::exception{
      
    public:
      
      /// ctor
      Exception(const char *m) {_msg = std::string(m);}
      Exception(const std::string &m) {_msg = m;}
      
      /// dtor
      ~Exception() throw() {}
      
      
      // methods
      
      /// report exception details.
      const char *what() const throw()  { return _msg.c_str(); }
      
      
    private:
      // data
      std::string _msg;
      
    };

HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_EXCEPTION_H

// version
// $Id$

// End of file 
