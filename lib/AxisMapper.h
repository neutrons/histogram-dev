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

#ifndef H_DANSE_AXISMAPPER
#define H_DANSE_AXISMAPPER


namespace DANSE {

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

#endif


// version
// $Id$

// End of file 
