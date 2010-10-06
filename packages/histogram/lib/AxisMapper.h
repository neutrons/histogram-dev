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

#ifndef DANSE_HISTOGRAM_AXISMAPPER_H
#define DANSE_HISTOGRAM_AXISMAPPER_H


#include "OutOfBound.h"

namespace DANSE {

  namespace Histogram {

  // map data value to index
  template <typename DataType, typename IndexType>
  class AxisMapper {

  public:
    
    typedef DataType datatype;
    typedef IndexType indextype;
  
    virtual IndexType operator() ( const DataType & data ) const = 0;
    virtual ~AxisMapper() {};
  };

  }
}

#endif // DANSE_HISTOGRAM_AXISMAPPER_H


// version
// $Id$

// End of file 
