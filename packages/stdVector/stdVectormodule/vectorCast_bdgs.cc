// Timothy M. Kelley Copyright (c) 2004 All rights reserved

#include "vectorCast_bdgs.h"
#include <string>
#include <vector>
#include "stdVector/utils.h"
#include "journal/debug.h"

#include <iostream>

namespace
{
    template <typename InNumT, typename OutNumT>
    void castVector( std::vector<InNumT> const & source,
                     std::vector<OutNumT> & target)
    {
        journal::debug_t debug("castVector");

        if(source.size() != target.size()) 
        {
            debug << journal::at(__HERE__) << "resizing target from "
                  << target.size() << " to " << source.size() << journal::endl;
            target.resize( source.size());
        }

//        debug << journal::at(__HERE__);
        for(size_t i=0; i<source.size(); ++i)
        {
            target[i] = static_cast<OutNumT>( source[i]);
//            debug << source[i] << " " << target[i] << " ";
        }
//        debug << journal::endl;
        return;
    }


    template <typename InNumT, typename OutNumT>
    bool _callVecCast( std::vector<InNumT> const &source,
                       PyObject *pytarg,
                       int targtype)
    {
        std::vector<OutNumT> *ptarg = 
            ARCSStdVector::unwrapVector<OutNumT>( pytarg, targtype);
        // Unwrap vector sets Python's error indicator
        if (ptarg == 0) return false;

        castVector<InNumT, OutNumT>( source, *ptarg);

//         journal::debug_t debug("castVector");

//         debug << journal::at(__HERE__);
//         for( size_t i=0; i < ptarg -> size(); ++i)
//         {
//             debug << " " << (*ptarg)[i];
//         }
//         debug << journal::endl;

        return true;
    }
    

    template <typename InNumT>
    bool _vecCastResolveInType( PyObject *pysrc,
                                       int srctype,
                                       PyObject *pytarg,
                                       int targtype,
                                       std::string & errstr)
    {
        std::vector<InNumT> *psrc = 
            ARCSStdVector::unwrapVector<InNumT>( pysrc, srctype);
        // Unwrap vector sets Python's error indicator if necessary
        if (psrc == 0) return false;

        bool ok = false;

        switch( targtype)
        {
        case 5:   // float
            ok = _callVecCast<InNumT, float>        ( *psrc, pytarg, targtype);
            break;
        case 6:   // double
            ok = _callVecCast<InNumT, double>       ( *psrc, pytarg, targtype);
            break;
        case 20:  // short short
            ok = _callVecCast<InNumT, char>         ( *psrc, pytarg, targtype);
            break;
        case 21:  // unsigned short short
            ok = _callVecCast<InNumT, unsigned char>( *psrc, pytarg, targtype);
            break;
        case 22:  // short
            ok = _callVecCast<InNumT, short>        ( *psrc, pytarg, targtype);
            break;
        case 23:  // int
            ok = _callVecCast<InNumT,unsigned short>( *psrc, pytarg, targtype);
            break;
        case 24:  // int
            ok = _callVecCast<InNumT, int>          ( *psrc, pytarg, targtype);
            break;
        case 25:  // unsigned int
            ok = _callVecCast<InNumT, unsigned int> ( *psrc, pytarg, targtype);
            break;
        default:
            errstr += "unsupported target datatype. Recognized datatypes:\n"
                "          float....5\n"
                "          double...6\n"
                "          short short ........... 20\n"
                "          unsigned short short .. 21\n"
                "          short ................. 22\n"
                "          unsigned short ........ 23\n"
                "          int.....24\n"
                "          unsigned int...25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return false;
        }
        return ok;
    }
} // anonymous::


namespace stdVector
{
    char vectorCast__name__[] = "vectorCast";
    char vectorCast__doc__[] = 
    "vectorCast( source, sourceType, target, targetType) --> None\n"
    "Copy source to target, casting from sourceType to targetType.\n"
    "inputs:\n"
    "    source (std::vector<sourceType>, PyCObject)\n"
    "    sourceType (int, see below for supported types)\n"
    "    target (std::vector<sourceType>, PyCObject)\n"
    "    targetType (int, see below for supported types)\n"
    "output: None\n"
    "Exceptions: ValueError\n";

    PyObject * vectorCast(PyObject *, PyObject *args)
    {
        PyObject *pysrc = 0, *pytarg = 0;
        int srctype = 0, targtype = 0;
        int ok = PyArg_ParseTuple( args, "OiOi", &pysrc, &srctype, &pytarg, 
                                   &targtype);
        if (!ok) return 0;

        std::string errstr("pystdVector_vectorCast()");
        switch( srctype)
        {
        case 5:   // float
            if (!_vecCastResolveInType<float>         ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 6:   // double
            if (!_vecCastResolveInType<double>        ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 20: // int 8 short short
            if (!_vecCastResolveInType<char>          ( pysrc, srctype, pytarg,
                                                        targtype, errstr))
                return 0;
            break;
        case 21: // unsigned int 8 
            if (!_vecCastResolveInType<unsigned char> ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 22: // int 16 short
            if (!_vecCastResolveInType<short>         ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 23: // unsigned int 16 
            if (!_vecCastResolveInType<unsigned short>( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 24:  // int
            if (!_vecCastResolveInType<int>           ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        case 25:  // unsigned int
            if (!_vecCastResolveInType<unsigned int>  ( pysrc, srctype, pytarg, 
                                                        targtype, errstr))
                return 0;
            break;
        default:
            errstr += "unsupported source datatype. Recognized datatypes:\n"
                "          float....5\n"
                "          double...6\n"
                "          short short ........... 20\n"
                "          unsigned short short .. 21\n"
                "          short ................. 22\n"
                "          unsigned short ........ 23\n"
                "          int........... 24\n"
                "          unsigned int.. 25\n";
            PyErr_SetString( PyExc_ValueError, errstr.c_str());
            return 0;
        }
        Py_INCREF(Py_None);
        return Py_None;
    }
} // stdVector::



// version
// $Id: vectorCast_bdgs.cc 85 2005-06-17 16:54:43Z tim $

// End of file
