// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2011  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef HISTOGRAM__MACROS_H
#define HISTOGRAM__MACROS_H


#ifdef USE_DANSE_NAMESPACE
#define HISTOGRAM_NAMESPACE_START namespace DANSE {namespace Histogram{
#define HISTOGRAM_NAMESPACE_END }}
#define USING_HISTOGRAM_NAMESPACE using namespace DANSE::Histogram;
#else
#define HISTOGRAM_NAMESPACE_START namespace histogram{
#define HISTOGRAM_NAMESPACE_END }
#define USING_HISTOGRAM_NAMESPACE using namespace histogram;
#endif


#endif


// version
// $Id$

// End of file 
  
