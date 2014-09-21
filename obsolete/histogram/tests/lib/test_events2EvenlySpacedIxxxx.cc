#include <cstring>
#include <iostream>
#include <vector>
#include <cassert>

#include "histogram/Event2Quantity.h"
#include "histogram/EvenlySpacedGridData_4D.h"
#include "histogram/events2EvenlySpacedIxxxx.h"


// specialized event data object
struct Event{
  unsigned int tof;
  unsigned int pixelID;
};


USING_HISTOGRAM_NAMESPACE


// event->(pack, tube, pixel, tof) functor
struct Event2pdpt
  : public Event2Quantity4<Event, 
			   unsigned int, 
			   unsigned int,
			   unsigned int,
			   unsigned int, 
			   double>
{
  unsigned int operator() 
  ( const Event & e, 
    unsigned int & pack, unsigned int & tube, 
    unsigned int &pixel, double &tof ) const 
  {
    pack = e.pixelID/1024 + 1;
    tube = e.pixelID/128 % 8;
    pixel = e.pixelID % 128;
    tof = e.tof/10.;
    return 1;
  }
};


int main()
{  
  // create events to reduce
  typedef std::vector<Event> events_t;
  events_t evts(1);
  Event e = { 12500, (21-1)*1024+3*128+77 };
  evts[0] = e;

  // event->pack,tube,pixel,tof functor
  Event2pdpt e2pdpt;

  // intensity array
  size_t size = 115*8*128*100;
  unsigned int * intensities = new unsigned int[ size ];
  for (int i=0; i<size; i++) { intensities[i] = 0; }

  // reduce
  events2EvenlySpacedIxxxx
    <Event, Event2pdpt, 
    unsigned int, unsigned int, unsigned int, double, 
    unsigned int>
    (evts.begin(), evts.end(),
     e2pdpt, 
     1, 116, 1, 
     0, 8, 1,
     0, 128, 1,
     1000, 2000, 10.,
     intensities);

  // verify
  assert (intensities[ ((21-1)*1024+3*128+77)*100 + 25] == 1);
  
  // finalize
  delete [] intensities;
  return 0;
}

