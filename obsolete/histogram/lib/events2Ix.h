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


#ifndef H_HISTOGRAM_EVENTS2IX
#define H_HISTOGRAM_EVENTS2IX

#include "Histogrammer.h"
#include "events2histogram.h"

HISTOGRAM_NAMESPACE_START

  /// add events to histogram I(x).
  ///
  /// template arguments:
  ///   Event2X: a Event2Quantity class
  ///   Ix: a GridData_1D class
  ///   EventIterator: event iterator type
  /// 
  /// arguments:
  ///   events_begin: beginning iterator for events
  ///   events_end: ending iterator for events
  ///   e2x: event -> x functor
  ///   ix: I(x) histogram
  template
  <typename Event, typename Event2X, typename Ix, typename EventIterator>
  void events2Ix
  ( const EventIterator & events_begin, const EventIterator & events_end,
    const Event2X & e2x, Ix & ix )
  {
    Histogrammer1				\
      <Event, Ix, Event2X, 
      typename Ix::xdatatype, 
      typename Ix::ydatatype> 
      her(ix, e2x);
    events2histogram( events_begin, events_end, her );
    return;
  }

HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2IX


// version
// $Id$

// End of file 
  
