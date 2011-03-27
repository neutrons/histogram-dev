// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2011  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef HISTOGRAM_EVENLYSPACEDAXISMAPPER_H
#define HISTOGRAM_EVENLYSPACEDAXISMAPPER_H


#include <sstream>

#include "AxisMapper.h"

HISTOGRAM_NAMESPACE_START

  // map data value to index
  template <typename NumberType, typename IndexType>
  class EvenlySpacedAxisMapper: AxisMapper<NumberType, IndexType> {

  public:
    EvenlySpacedAxisMapper( NumberType begin, NumberType end, NumberType step )
      : m_begin( begin ), m_end( end ), m_step( step )
    {}

    virtual IndexType operator() ( const NumberType & data ) const 
    {
      if (data>=m_end || data<m_begin) {
	std::ostringstream oss;
	oss << "data " << data 
	    << " is out of bound (" << m_begin << ", " << m_end
	    << " )";
	throw OutOfBound(oss.str());
      }
      //std::cout << data << std::endl;
      //std::cout << IndexType( (data-m_begin)/m_step ) << std::endl;
      return IndexType( (data-m_begin)/m_step );
    }
    
  private:
    NumberType m_begin, m_end, m_step;
  };


HISTOGRAM_NAMESPACE_END

#endif // HISTOGRAM_EVENLYSPACEDAXISMAPPER_H


// version
// $Id$

// End of file 
