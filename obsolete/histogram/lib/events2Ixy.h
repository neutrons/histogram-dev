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


#ifndef H_HISTOGRAM_EVENTS2IXY
#define H_HISTOGRAM_EVENTS2IXY

#include "Histogrammer.h"
#include "events2histogram.h"

HISTOGRAM_NAMESPACE_START

/// Function to histogramming neutron events to I(x,y) histogram.
/// events2Ix is a function that histograms neutron events (objects
/// of class Event) in to a 2D histogram.
///
/// template arguments:
///   Event: event class
///   Event2XY: a Event2Quantity2 class
///   Ixy: a DataGrid2D class or a Ixy class
/// 
/// arguments:
///   events_begin: begin iterator of neutron events 
///   events_end: end iterator of neutron events 
///   e2xy: event -> x,y functor
///   ixy: I(x,y) histogram
template 
<typename Event, typename Event2XY, typename Ixy, typename EventIterator>
void events2Ixy
( const EventIterator & events_begin,
  const EventIterator & events_end,
  const Event2XY & e2xy, 
  Ixy & ixy )
{
  Histogrammer2
    <Event, Ixy, Event2XY, 
    typename Ixy::xdatatype,
    typename Ixy::ydatatype,
    typename Ixy::zdatatype
    >
    her( ixy, e2xy );
  events2histogram( events_begin, events_end, her );
  return;
}

HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2IX


// version
// $Id$

// End of file 
  
