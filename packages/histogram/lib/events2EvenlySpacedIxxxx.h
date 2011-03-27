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


#ifndef H_HISTOGRAM_EVENTS2EVENLYSPACEDIXXXX
#define H_HISTOGRAM_EVENTS2EVENLYSPACEDIXXXX

//#include "events2Ixxxx.h"
#include "Histogrammer.h"
#include "events2histogram.h"
#include "EvenlySpacedGridData_4D.h"


HISTOGRAM_NAMESPACE_START

/// add events to histogram I(x1,x2,x3,x4); {xi}, i=1..4 are evenly spaced axes.
///
/// template arguments:
///   Event: event class
///   Event2XXXX: a Event2Quantity4 class
///   X1Data: data type of x1 
///   X2Data: data type of x2 
///   X3Data: data type of x3 
///   X4Data: data type of x4 
///   ZIterator: iterator of z values.
//    EventIterator: event iterator type.
/// 
/// arguments:
///   events_begin: begin iterator of neutron events 
///   events_end: end iterator of neutron events 
///   e2xxxx: event -> x functor
///   i in [1..4]: xi_begin, xi_end, xi_step: define the xi axis
///   z_begin: iterator of z array to store z values on the grid defined
///            by {xi} axes
template <typename Event, 
	  typename Event2XXXX, 
	  typename X1Data, typename X2Data, typename X3Data, typename X4Data,
	  typename ZData, typename ZIterator,
	  typename EventIterator>
void events2EvenlySpacedIxxxx
( const EventIterator & events_begin, const EventIterator & events_end, 
  const Event2XXXX & e2xxxx, 
  X1Data x1_begin, X1Data x1_end, X1Data x1_step, 
  X2Data x2_begin, X2Data x2_end, X2Data x2_step, 
  X3Data x3_begin, X3Data x3_end, X3Data x3_step, 
  X4Data x4_begin, X4Data x4_end, X4Data x4_step, 
  ZIterator z_begin)
{
  // histogram type
  typedef EvenlySpacedGridData_4D
    < X1Data, X2Data, X3Data, X4Data, ZData, ZIterator> Ixxxx;
  // the histogram
  Ixxxx ixxxx
    (x1_begin, x1_end, x1_step, 
     x2_begin, x2_end, x2_step, 
     x3_begin, x3_end, x3_step, 
     x4_begin, x4_end, x4_step, 
     z_begin);
    
  // histogrammer
  Histogrammer4
    <Event, Ixxxx, Event2XXXX, 
    X1Data, X2Data, X3Data, X4Data, ZData>
    her( ixxxx, e2xxxx );

  // reduce
  events2histogram( events_begin, events_end, her );
  
  return ;
}

HISTOGRAM_NAMESPACE_END


#endif // H_HISTOGRAM_EVENTS2EVENLYSPACEDIXXXX


// version
// $Id$

// End of file 
  
