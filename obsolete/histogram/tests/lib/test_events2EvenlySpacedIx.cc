#include <cstring>
#include <iostream>
#include <vector>
#include <cassert>


#include "histogram/EvenlySpacedGridData_1D.h"
#include "histogram/Event2Quantity.h"
#include "histogram/events2EvenlySpacedIx.h"


// specialized event data object
struct Event{
  unsigned int tof;
};


USING_HISTOGRAM_NAMESPACE

// event->tof functor
struct Event2TofChannel: public Event2Quantity1<Event, unsigned int>
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

  // result histogram intensity array
  unsigned int intensities[7];
  for (int i=0; i<7; i++) { intensities[i] = 0; }
  
  // run reduction
  events2EvenlySpacedIx
    <Event, Event2TofChannel, 
    unsigned int, unsigned int
    >
    (evts.begin(), evts.end(), 
     e2t, 
     1000, 8000, 1000,
     intensities);

  //
  // for (int i=0; i<7; i++)
  //   std::cout << intensities[i] << ", ";
  // std::cout << std::endl;
  
  // verify
  assert(intensities[1] == 4);
  assert(intensities[2] == 3);
  assert(intensities[3] == 3);
  
  return 0;
}

