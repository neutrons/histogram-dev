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


#ifndef H_HISTOGRAM_EVENTS2HISTOGRAM
#define H_HISTOGRAM_EVENTS2HISTOGRAM


#include <algorithm>

#include "_macros.h"




HISTOGRAM_NAMESPACE_START

  template <typename histogrammer_t, typename event_it_t>
  void events2histogram
  (const event_it_t & events_begin,
   const event_it_t & events_end,
   histogrammer_t & her )
  {
#ifdef DEBUG
    printf("Warning events2histogram %s:%d \n", __FILE__, __LINE__);
#endif
    std::for_each(events_begin, events_end, her);
  }

HISTOGRAM_NAMESPACE_END

#endif // H_HISTOGRAM_EVENTS2HISTOGRAM


// version
// $Id$

// End of file
