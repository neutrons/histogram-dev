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


#ifndef DANSE_HISTOGRAM_EXCEPTION_H
#define DANSE_HISTOGRAM_EXCEPTION_H


#include <string>


namespace DANSE {

  namespace Histogram {

    struct Exception{ 
    public:
      
      Exception(const char *m) {_msg = std::string(m);}
      const char *what() const throw()  { return _msg.c_str(); }
      ~Exception() throw() {}
      
    private:
      std::string _msg;
      
    };
  } //Histogram:
} // DANSE:


#endif // DANSE_HISTOGRAM_EXCEPTION_H

// version
// $Id$

// End of file 
