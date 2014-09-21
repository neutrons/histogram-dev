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


#ifndef H_HISTOGRAM_EVENTS2IXXXX
#define H_HISTOGRAM_EVENTS2IXXXX

#include "Histogrammer.h"
#include "events2histogram.h"


HISTOGRAM_NAMESPACE_START

/// Function to histogramming neutron events to I(x,y) histogram.
/// events2Ix is a function that histograms neutron events (objects
/// of class Event) in to a 2D histogram.
///
/// template arguments:
///   Event: event class
///   Event2XXXX: a Event2Quantity2 class
///   Ixxxx: a DataGrid2D class or a Ixxxx class
/// 
/// arguments:
///   events_begin: begin iterator of neutron events 
///   events_end: end iterator of neutron events 
///   e2xxxx: event -> x,y functor
///   ixxxx: I(x,y) histogram
template 
<typename Event, typename Event2XXXX, 
 typename Ixxxx, typename EventIterator>
void events2Ixxxx
( const EventIterator & events_begin, const EventIterator & events_end,
  const Event2XXXX & e2xxxx, Ixxxx & ixxxx )
{
  Histogrammer4
    <Event, Ixxxx, Event2XXXX, 
    typename Ixxxx::x1datatype, typename Ixxxx::x2datatype, 
    typename Ixxxx::x3datatype, typename Ixxxx::x4datatype> 
    her( ixxxx, e2xxxx );
  events2histogram( events_begin, events_end, her );
  return ;
}


HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2IX


// version
// $Id$

// End of file 
  
