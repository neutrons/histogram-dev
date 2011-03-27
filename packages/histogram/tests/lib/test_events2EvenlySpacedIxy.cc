#include <cstring>
#include <iostream>
#include <vector>
#include <cassert>

#include "histogram/Event2Quantity.h"
#include "histogram/EvenlySpacedGridData_2D.h"
#include "histogram/events2EvenlySpacedIxy.h"


// specialized event data object
struct Event{
  unsigned int tof;
  unsigned int pixelID;
};


USING_HISTOGRAM_NAMESPACE


// event->(pix,tof) functor
struct Event2PixTof
  : public Event2Quantity2<Event, unsigned int, unsigned int, double>
{
  unsigned int operator() 
  (const Event & e, unsigned int & pix, double & tof) 
    const 
  {
    tof = e.tof * 0.1; // micro second
    pix = e.pixelID;
    return 2;
  }
};


int main()
{  
  // create events to reduce
  typedef std::vector<Event> events_t;
  events_t evts(1);
  evts[0].tof = 3500;
  evts[0].pixelID = 2048;

  // event->pix,tof functor
  Event2PixTof e2pt;
  
  // intensity array
  const unsigned int NX = 3, NY = 4, N = NX*NY;
  unsigned int intensities[N];
  for (int i=0; i<N; i++) { intensities[i] = 0; }
  
  // reduce
  events2EvenlySpacedIxy
    <Event, Event2PixTof, unsigned int, double, unsigned int>
    (evts.begin(), evts.end(), 
     e2pt, 
     0, 3000, 1000, 
     200, 600, 100, 
     intensities);

  // verify
  for (int i=0; i<N; i++) {
    if (i==9)
      assert (intensities[i] == 2);
    else
      assert (intensities[i] == 0);
  }
  return 0;
}

