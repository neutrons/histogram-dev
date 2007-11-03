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


#ifndef H_DANSE_EXCEPTION
#define H_DANSE_EXCEPTION


namespace DANSE {

  struct Exception{ //: public std::exception {
  public:
  
    Exception(const char *m) {_msg = std::string(m);}
    const char *what() const throw()  { return _msg.c_str(); }
    ~Exception() throw() {}

  private:
    std::string _msg;

  };

}

#endif

// version
// $Id$

// End of file 
