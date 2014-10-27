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


#ifndef H_HISTOGRAM_EVENTS2EVENLYSPACEDIXY
#define H_HISTOGRAM_EVENTS2EVENLYSPACEDIXY

//#include "events2Ixy.h"
#include "Histogrammer.h"
#include "events2histogram.h"
#include "EvenlySpacedGridData_2D.h"


HISTOGRAM_NAMESPACE_START

/// add events to histogram I(x,y); both x and y are evenly spaced axes.
///
/// template arguments:
///   Event: event class
///   Event2XY: a Event2Quantity2 class
///   XData: data type of x 
///   YData: data type of y 
///   ZIterator: iterator of z values.
///   EventIterator: event iterator type.
/// 
/// arguments:
///   events_begin: begin iterator of neutron events 
///   events_end: end iterator of neutron events 
///   e2xy: event -> x functor
///   x_begin, x_end, x_step: define the x axis 
///   y_begin, y_end, y_step: define the y axis
///   z_begin: iterator of z array to store z values on the grid defined
///            by x and y axes
///   Note: bin boundaries will be begin, begin+step, begin+2*step,
///         ..., x_begin + n *x_step
///         where n = int( (end-begin)/step ). 
///         So be careful when choosing "end" to leave room for 
///         floating point error. Usually it is wise to choose
//          end = begin + n*step + step/100.
template <typename Event, 
	  typename Event2XY, 
	  typename XData, typename YData,
	  typename ZData, typename ZIterator,
	  typename EventIterator>
void events2EvenlySpacedIxy
( const EventIterator &events_begin, const EventIterator &events_end,
  const Event2XY & e2xy, 
  XData x_begin, XData x_end, XData x_step, 
  YData y_begin, YData y_end, YData y_step, 
  ZIterator z_begin)
{
  // histogram type
  typedef EvenlySpacedGridData_2D< XData, YData, ZData, ZIterator> Ixy;
  // the histogram
  Ixy ixy
    (x_begin, x_end, x_step, 
     y_begin, y_end, y_step, 
     z_begin);
    
  // histogrammer
  Histogrammer2
    <Event, Ixy, Event2XY, XData, YData, ZData>
    her( ixy, e2xy );

  // reduce
  events2histogram( events_begin, events_end, her );
  return ;
}


HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2EVENLYSPACEDIXY


// version
// $Id$

// End of file 
  
