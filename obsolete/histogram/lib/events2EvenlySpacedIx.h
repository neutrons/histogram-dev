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


#ifndef H_HISTOGRAM_EVENTS2EVENLYSPACEDIX
#define H_HISTOGRAM_EVENTS2EVENLYSPACEDIX


#include "Histogrammer.h"
#include "events2histogram.h"
#include "EvenlySpacedGridData_1D.h"


HISTOGRAM_NAMESPACE_START

/// add events to histogram I(x); x is an evenly spaced axis.
///
/// template arguments:
///   Event: Event class
///   Event2X: a Event2Quantity class
///   XData: data type of x 
///   YIterator: iterator of y values.
///   EventIterator: event iterator type.
/// 
/// arguments:
///   events_begin: events beginning iterator
///   events_end: events ending iterator
///   N: number of neutron events to be processed
///   e2x: event -> x functor
///   x_begin, x_end, x_step: define the x axis
///   y_begin: iterator of y array to store y values at x points on x axis
template <typename Event, 
	  typename Event2X, 
	  typename XData,
	  typename YData, typename YIterator,
	  typename EventIterator>
void events2EvenlySpacedIx
( const EventIterator & events_begin, const EventIterator &events_end,
  const Event2X & e2x,
  XData x_begin, XData x_end, XData x_step, 
  YIterator y_begin)
{
  // histogram type
  typedef EvenlySpacedGridData_1D< XData, YData, YIterator> Ix;
  // the histogram
  Ix ix(x_begin, x_end, x_step, y_begin);
  
  // histogrammer
  Histogrammer1< Event, Ix, Event2X, 
    typename Ix::xdatatype, typename Ix::ydatatype> her( ix, e2x );

  // reduce
  events2histogram( events_begin, events_end, her );
  
  return;
}

HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2EVENLYSPACEDIX


// version
// $Id$

// End of file 
  
