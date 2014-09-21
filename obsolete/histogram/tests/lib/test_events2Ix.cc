#include <cstring>
#include <iostream>
#include <vector>
#include <cassert>

#include "histogram/EvenlySpacedGridData_1D.h"
#include "histogram/Event2Quantity.h"
#include "histogram/events2Ix.h"

USING_HISTOGRAM_NAMESPACE;

// specialized event data object
struct Event{
  unsigned int tof;
};

// the I(tof) histogram data type
typedef EvenlySpacedGridData_1D<unsigned int, unsigned int> Itofchannel;

// event -> tof  functor
// this functor is trivial, 
struct Event2TofChannel
  : public Event2Quantity1<Event, unsigned int, unsigned int>
{
  unsigned int operator() ( const Event & e, unsigned int & d ) const 
  {
    d = e.tof;
    return 1;
  }
};


int main()
{  
  // create events to reduce
  typedef std::vector<Event> events_t;
  events_t evts(10);
  for (int i=0; i<10; i++)
    evts[i].tof = 2000+i*300;

  // event->tof functor
  Event2TofChannel e2t;

  // I(tof) histogram
  // ... array of intensities
  unsigned int intensities[7];
  // ... histogram
  Itofchannel itof( 1000, 8000, 1000, intensities );
  itof.clear();
  
  // reduce events to histogram
  events2Ix<Event, Event2TofChannel, Itofchannel, events_t::const_iterator>
    (evts.begin(), evts.end(), e2t, itof);

  // for (int i=0; i<7; i++)
  //   std::cout << intensities[i] << ", ";
  // std::cout << std::endl;
  
  assert(intensities[1] == 4);
  assert(intensities[2] == 3);
  assert(intensities[3] == 3);
  
  return 0;
}

