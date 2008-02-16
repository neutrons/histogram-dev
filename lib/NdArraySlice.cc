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


#include "NdArray.h"
#include "NdArraySlice.h"


namespace DANSE { 
  namespace Histogram {

    typedef NdArray<unsigned int*, unsigned int, unsigned int, long, 2> UIntArray_2D;
    typedef NdArraySlice< UIntArray_2D, unsigned int > UIntArray_2D_Slice;
  }
}


// version
// $Id$

// End of file 
