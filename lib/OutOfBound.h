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

#ifndef DANSE_HISTOGRAM_OUTOFBOUND_H
#define DANSE_HISTOGRAM_OUTOFBOUND_H


#include "Exception.h"

namespace DANSE {

  namespace Histogram {

    struct OutOfBound : public Exception
    {
      OutOfBound() : Exception( "out of bound" ) {}
      OutOfBound(const char *msg) : Exception( msg ) {}
    };

  } // Histogram:
  
} // DANSE:

#endif // DANSE_HISTOGRAM_OUTOFBOUND_H


// version
// $Id$

// End of file 
