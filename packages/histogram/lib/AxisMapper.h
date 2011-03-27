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

#ifndef HISTOGRAM_AXISMAPPER_H
#define HISTOGRAM_AXISMAPPER_H


#include "OutOfBound.h"

HISTOGRAM_NAMESPACE_START

  // map data value to index
  template <typename DataType, typename IndexType>
  class AxisMapper {

  public:
    
    typedef DataType datatype;
    typedef IndexType indextype;
  
    virtual IndexType operator() ( const DataType & data ) const = 0;
    virtual ~AxisMapper() {};
  };

HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_AXISMAPPER_H


// version
// $Id$

// End of file 
