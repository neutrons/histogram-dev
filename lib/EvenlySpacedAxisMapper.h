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

#ifndef H_DANSE_EVENLYSPACEDAXISMAPPER
#define H_DANSE_EVENLYSPACEDAXISMAPPER

#include "AxisMapper.h"

namespace DANSE {

  // map data value to index
  template <typename NumberType, typename IndexType>
  class EvenlySpacedAxisMapper: AxisMapper<NumberType, IndexType> {

  public:
    EvenlySpacedAxisMapper( NumberType begin, NumberType end, NumberType step )
      : m_begin( begin ), m_end( end ), m_step( step )
    {}

    virtual IndexType operator() ( const NumberType & data ) const 
    {
      if (data>=m_end || data<m_begin) { throw OutOfBound(); }
      //std::cout << data << std::endl;
      //std::cout << IndexType( (data-m_begin)/m_step ) << std::endl;
      return IndexType( (data-m_begin)/m_step );
    }
    
  private:
    NumberType m_begin, m_end, m_step;
  };

}

#endif


// version
// $Id$

// End of file 
