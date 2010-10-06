// Jiao Lin Copyright (c) 2005 All rights reserved

#include <vector>
#include <string>
#include "proxy_bdgs.h"
#include "stdVector/VectorProxy.h"


namespace stdVector
{
  char stdVector_proxy__name__[] = "stdVector_proxy";
  char stdVector_proxy__doc__[] = 
    "stdVector_proxy( dtype, raw_vector) -> new wrapped std::vector<dtype>\n"
    ""
    ;

  PyObject * stdVector_proxy(PyObject *, PyObject *args)
  {
    using ARCSStdVector::createVectorProxy;

    int dtype = 0;
    PyObject *obj = 0;
    int ok = PyArg_ParseTuple( args, "iO", &dtype, &obj);
    if (!ok) return 0;

    std::string errstr("stdVector_proxy()");

    if (!PyCObject_Check( obj )) {
      errstr += "Second argument should be a PyCObject with a void pointer pointing to";
      errstr += " a std::vector object\n";
      PyErr_SetString( PyExc_ValueError, errstr.c_str());
      return 0;      
    }

    PyObject *retval = 0;

    switch( dtype)
      {
      case 4:   // char
	retval = createVectorProxy<char>( obj, dtype );
	break;
      case 5:   // float
	retval = createVectorProxy<float>( obj, dtype );
	break;
      case 6:   // double
	retval = createVectorProxy<double>( obj, dtype );
	break;
      case 20:  // short short
	retval = createVectorProxy<char>( obj, dtype );
	break;
      case 21:  // unsigned short short
	retval = createVectorProxy<unsigned char>( obj, dtype );
	break;
      case 22:  // short
	retval = createVectorProxy<short>( obj, dtype );
	break;
      case 23:  // unsigned short
	retval = createVectorProxy<unsigned short>( obj, dtype );
	break;
      case 24:  // int
	retval = createVectorProxy<int>( obj, dtype );
	break;
      case 25:  // unsigned int
	retval = createVectorProxy<unsigned int>( obj, dtype );
	break;
      default:
	errstr += "unsupported target datatype. Recognized datatypes:\n"
	  "          char.....4\n"
	  "          float....5\n"
	  "          double...6\n"
	  "          short short ........... 20\n"
	  "          unsigned short short .. 21\n"
	  "          short ................. 22\n"
	  "          unsigned short ........ 23\n"
	  "          int.....24\n"
	  "          unsigned int...25\n";
	PyErr_SetString( PyExc_ValueError, errstr.c_str());
	return 0;
      } // switch( dtype)
    return retval;
  } // stdVector_proxy
  
} // stdVector::




// version
// $Id: proxy_bdgs.cc 141 2005-07-08 22:32:11Z linjiao $

// End of file
