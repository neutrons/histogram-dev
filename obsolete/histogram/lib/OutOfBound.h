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

#ifndef HISTOGRAM_OUTOFBOUND_H
#define HISTOGRAM_OUTOFBOUND_H


#include "Exception.h"

HISTOGRAM_NAMESPACE_START

    struct OutOfBound : public Exception
    {
      OutOfBound() : Exception( "out of bound" ) {}
      OutOfBound(const char *msg) : Exception( msg ) {}
      OutOfBound(const std::string &msg) : Exception( msg ) {}
    };

HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_OUTOFBOUND_H


// version
// $Id$

// End of file 
