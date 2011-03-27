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


#ifndef H_HISTOGRAM_EVENT2QUANTITY
#define H_HISTOGRAM_EVENT2QUANTITY


#include "_macros.h"


HISTOGRAM_NAMESPACE_START

  /// Event2Quantity1: convert event to a scalar quantity.
  /// Class to convert an neutron event (Event object) to a scalar quantity.
  /// For example, 
  ///   * event --> pixel ID
  ///   * event --> tof
  /// This is an abstract base class. 
  /// Solid subclasses will be used by histogrammers (objects of Histogrammer1). 
  template <typename event_t, 
	    typename prob_t,
	    typename data_t = prob_t>
  class Event2Quantity1 {
  public:
    /// convert event to a quantity
    /// return: 0 if failed. 1 if succeed
    virtual prob_t operator() ( const event_t & e, data_t & d ) const = 0;
    virtual ~Event2Quantity1() {} ;
  };

  /// Event2Quantity2: convert event to two scalar quantities, 
  /// and return the probability of the event
  /// Class to convert an neutron event (Event object) to two scalar quantities.
  /// Forexample, 
  ///   event --> pixel ID, tof
  ///   event --> Q, E
  /// This is an abstract base class.
  /// Solid subclasses will be used by histogrammers 
  /// (objects of Histogrammer2). 
  template <typename event_t, 
	    typename prob_t,
	    typename x_t = prob_t, 
	    typename y_t = x_t
	    >
  class Event2Quantity2 {
    public:
    /// convert event to two quantities
    /// return: 0 if failed. 1 if succeed
    virtual prob_t operator() ( const event_t & e, x_t & d1, y_t &d2 ) const = 0;
    virtual ~Event2Quantity2() {}
  };
  
  /// Event2Quantity4: convert event to four scalar quantities.
  /// Class to convert an neutron event (Event object) to four
  /// scalar quantities.
  /// Forexample, 
  ///   event --> Qx, Qy, Qz, E
  /// This is an abstract base class.
  /// Solid subclasses will be used by histogrammers 
  /// (objects of Histogrammer4). 
  template <typename event_t,
	    typename prob_t,
	    typename x_t=prob_t,
	    typename y_t=x_t,
	    typename z_t=x_t,
	    typename u_t=x_t
	    >
  class Event2Quantity4 {
  public:
    /// convert event to 4 quantities
    /// return: 0 if failed. 1 if succeed
    virtual prob_t operator() 
    ( const event_t & e, 
      x_t & d1, y_t &d2, z_t &d3, u_t &d4  ) const = 0;
    virtual ~Event2Quantity4() {}
  };

HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENT2QUANTITY


// version
// $Id$

// End of file 
