// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2003 All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

//#include <portinfo>
#include <Python.h>

#include "misc.h"
#include "ak_types.h"
#include <iostream>
#include "array_kluge/array_kluge.h"


// copyright

char pyarray_kluge_copyright__doc__[] = "";
char pyarray_kluge_copyright__name__[] = "copyright";

static char pyarray_kluge_copyright_note[] = 
    "array_kluge python module: Copyright (c) 1998-2003 California Institute of Technology";


PyObject * pyarray_kluge_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pyarray_kluge_copyright_note);
}
    
// void ptr to Python list:
char pyNeXus_vptr2pylist__name__[] = "vptr2pylist";
char pyNeXus_vptr2pylist__doc__[] = "Convert void ptr to Python list"
                    "3 Arguments: vptr, length, type\n"
                    "Input:\n"
                    "      data (PyCObject w/ void ptr)\n"
                    "      length (integer)\n"
                    "      type (integer) \n"
                    "Output: \n"
                    "      (return) PyList\n"
                    "Exceptions: TypeError, ValueError, RuntimeError";


static int loadpylist(PyObject * pylist, void *ptr, int const length, const int type)
{
// NeXus type map
// #define NX_CHAR      4
// #define NX_FLOAT32   5
// #define NX_FLOAT64   6
// #define NX_UINT8    21
// #define NX_INT32    24
// #define NX_UINT32   25

    PyObject *listee = 0;

    char *cp = static_cast<char *>(ptr);
    float32 *fp = static_cast<float32*>(ptr);
    double *dp = static_cast<double*>(ptr);
    int *ip = static_cast<int*>(ptr);
    unsigned int* uip = static_cast<unsigned int*>(ptr);
    //char *ucp = static_cast< char*>(ptr);

    int bad = 0;

    int8 *i8p = static_cast<int8 *>(ptr);
    uint8 *ui8p = static_cast<uint8 *>(ptr);
    int16 *i16p = static_cast<int16 *>(ptr);
    uint16 *ui16p = static_cast<uint16 *>(ptr);

    if(type == NX_CHAR)
    {
        char *buff = new char[length+1];
        for(int i=0; i<length; i++) buff[i] = *(cp+i);

        buff[length] = '\0';
        listee = PyString_FromString(buff);
        int ok = PyList_SetItem( pylist, 0, listee);
        if (ok != 0)
        {
            std::cerr<<" i="<<0<<" val = "<<buff<<" listee = "<<listee<<"\n";
            bad = -1;
        }
        delete [] buff;
    }//if(type == NX_CHAR)

    else
    {
        for(int i=0; i<length; i++)
        {
    //		int ok = 0;
            switch(type)
            {
                case 5:
                    listee = PyFloat_FromDouble( static_cast<double>(*( fp + i)));
                    break;
                case 6:
                    listee = PyFloat_FromDouble( *( dp + i));
                    break;
                case 24:
                    listee = PyInt_FromLong( *( ip + i));
                    break;
                case 25:
                    listee = PyInt_FromLong( *( uip + i));
                    break;
                case 20:
                    listee = PyInt_FromLong( static_cast<int>(*( i8p + i)));
                    break;
                case 21:
                    listee = PyInt_FromLong( static_cast<int>(*(ui8p + i)));
                    break;
                case 22:
                    listee = PyInt_FromLong( static_cast<int>(*(i16p + i)));
                    break;
                case 23:
                    listee = PyInt_FromLong( static_cast<int>(*(ui16p + i)));
                    break;
                default:
                    return -2;
            }
            int ok = PyList_SetItem( pylist, i, listee);
            if (ok != 0)
            {
                std::cerr<<" i="<<i<<" val = "<<*(dp+i)<<" "<<listee<<"\n";

                bad = -1;
            }
        } //for(int i=0; i<length; i++)
    }//else
    return bad;
}

PyObject * pyNeXus_vptr2pylist(PyObject *, PyObject *args)
{
    PyObject *pydata;
    int length, type;

    int ok = PyArg_ParseTuple( args, "Oii", &pydata, &length, &type);
    if (!ok) return 0;

    void *data = PyCObject_AsVoidPtr(pydata);

    if( length < 1)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() length must be > 0");
        PyErr_SetString(PyExc_ValueError, errstr.c_str() );
        return 0;
    }
    PyObject *pylist = PyList_New(length);
    if(pylist == 0)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() couldn't make list");
        PyErr_SetString(PyExc_RuntimeError, errstr.c_str() );
        return 0;
    }

    int chk = loadpylist(pylist, data, length, type);
    if(chk == -2)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() unknown data type");
        PyErr_SetString(PyExc_ValueError, errstr.c_str() );
        return 0;
    }
    if(chk == -1)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() problem with "
                           "loademup()");
        PyErr_SetString(PyExc_ValueError, errstr.c_str() );
        return 0;
    }
    return Py_BuildValue("O", pylist);
}

// Python list to void ptr:
char pyNeXus_pylist2vptr__name__[] = "pylist2vptr";
char pyNeXus_pylist2vptr__doc__[] = "Load Python list into memory at voir ptr"
                    "3 Arguments: pylist, length, type\n"
                    "Input:\n"
                    "      pylist (PyList)\n"
                    "      length (integer)\n"
                    "      type (integer) \n"
                    "Output: \n"
                    "      (return) (PyCObject w/ void ptr)\n"
                    "Exceptions: TypeError, ValueError, RuntimeError";


static void delete_chararr(void *ptr)
{
    char *oldp = static_cast<char *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old char array\n";
    return;
}
static void delete_intarr(void *ptr)
{
    int *oldp = static_cast<int *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old int array\n";
    return;
}
static void delete_dblarr(void *ptr)
{
    double *oldp = static_cast<double *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_flt32arr(void *ptr)
{
    float32 *oldp = static_cast<float32 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_int8arr(void *ptr)
{
    int8 *oldp = static_cast<int8 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_uint8arr(void *ptr)
{
    uint8 *oldp = static_cast<uint8 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_int16arr(void *ptr)
{
    int16 *oldp = static_cast<int16 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_uint16arr(void *ptr)
{
    uint16 *oldp = static_cast<uint16 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}
static void delete_uintarr(void *ptr)
{
    uint32 *oldp = static_cast<uint32 *>(ptr);
    delete [] oldp;
//	std::cout<<"misc.cc Deleted old double array\n";
    return;
}

//Load data into appropriate array, return base address
PyObject * pyNeXus_pylist2vptr(PyObject *, PyObject *args)
{
    PyObject *pylist;
    int length, type;

    int ok = PyArg_ParseTuple( args, "Oii", &pylist, &length, &type);
    if (!ok) return 0;


    // TK changed 6/1/05: if length of list is zero, nothing is copied from
    // the list to the array; copying nothing should be fine.
    if( length < 0)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() length must be > 0");
        PyErr_SetString(PyExc_ValueError, errstr.c_str() );
        return 0;
    }

// #define NX_CHAR      4 x
// #define NX_FLOAT32   5 x
// #define NX_FLOAT64   6 x
// #define NX_INT8     20 x
// #define NX_UINT8    21 x
// #define NX_INT16    22 x
// #define NX_UINT16   23 x
// #define NX_INT32    24 x
// #define NX_UINT32   25

    PyObject *ret = 0;
    char *vc = 0;
    int *ip = 0;
    double *dp = 0;
    float32 *fp =0;

    int8 *i8p = 0;
    uint8 *ui8p = 0;
    int16 *i16p = 0;
    uint16 *ui16p = 0;
    uint32 *uip = 0;
    switch(type)
    {
        case NX_CHAR:
            vc = new char[length];
            ret = PyCObject_FromVoidPtr(vc, delete_chararr);
            for(int i=0; i<length; i++)
            {
                char *temp = PyString_AsString( PyList_GetItem(pylist,i));
                vc[i] = *temp;
//				std::cout<<"vc[i] = "<<vc[i]<<"\n";
            }
            break;
        case 5:
            fp = new float32[length];
            ret = PyCObject_FromVoidPtr(fp, delete_flt32arr);
            for(int i=0; i<length; i++)
            {
                double temp = PyFloat_AsDouble( PyList_GetItem(pylist,i));
                fp[i] = static_cast<float32>(temp);
//				std::cout<<"pylist2vptr "<<temp<<" "<<fp[i]<<"\n";
            }
            break;
        case 6:
            dp = new double[length];
            ret = PyCObject_FromVoidPtr(dp, delete_dblarr);
            for(int i=0; i<length; i++)
            {
                double temp = PyFloat_AsDouble( PyList_GetItem(pylist,i));
                dp[i] = temp;
            }
            break;
        case 20:
            i8p = new int8[length];
            ret = PyCObject_FromVoidPtr(i8p, delete_int8arr);
            for(int i=0; i<length; i++)
            {
                int8 temp = static_cast<int8>(PyFloat_AsDouble(
                                                    PyList_GetItem(pylist,i)));
                i8p[i] = temp;
            }
            break;
        case 21:
            ui8p = new uint8[length];
            ret = PyCObject_FromVoidPtr(ui8p, delete_uint8arr);
            for(int i=0; i<length; i++)
            {
                uint8 temp = static_cast<int8>(PyFloat_AsDouble(
                                                    PyList_GetItem(pylist,i)));
                ui8p[i] = temp;
            }
            break;
        case 22:
            i16p = new int16[length];
            ret = PyCObject_FromVoidPtr(i16p, delete_int16arr);
            for(int i=0; i<length; i++)
            {
                int16 temp = static_cast<int16>(PyFloat_AsDouble(
                                                    PyList_GetItem(pylist,i)));
                i16p[i] = temp;
            }
            break;
        case 23:
            ui16p = new uint16[length];
            ret = PyCObject_FromVoidPtr(ui16p, delete_uint16arr);
            for(int i=0; i<length; i++)
            {
                uint16 temp = static_cast<uint16>(PyFloat_AsDouble(
                                                    PyList_GetItem(pylist,i)));
                ui16p[i] = temp;
            }
            break;
        case 24:
            ip = new int[length];
            ret = PyCObject_FromVoidPtr(ip, delete_intarr);
            for(int i=0; i<length; i++)
            {
                int temp = PyInt_AsLong( PyList_GetItem(pylist,i));
                ip[i] = temp;
            }
            break;
        case 25:
            uip = new uint32[length];
            ret = PyCObject_FromVoidPtr(uip, delete_uintarr);
            for(int i=0; i<length; i++)
            {
                uint32 temp = static_cast<uint32>(PyInt_AsLong(
                                                    PyList_GetItem(pylist,i)));
                uip[i] = temp;
            }
            break;
        default:
            std::string errstr("misc.cc pyNeXus_pylist2vptr() unknown type");
            PyErr_SetString(PyExc_ValueError, errstr.c_str() );
            return 0;
        }

    return ret;
}

char pyNeXus_pylistin2vptr__name__[] = "pylistin2vptr";
char pyNeXus_pylistin2vptr__doc__[] = 
"pylistin2vptr(pylist, length, datatype, vptr)\n"
"load a Python list into an existing array at void pointer\n";

PyObject * pyNeXus_pylistin2vptr(PyObject *, PyObject *args)
{
    PyObject *pylist, *pyvptr;
    int length, type;

    int ok = PyArg_ParseTuple( args, "OiiO", &pylist, &length, &type,
                               &pyvptr);
    if (!ok) return 0;



    if( length < 1)
    {
        std::string errstr("misc.cc pyNeXus_vptr2pylist() length must be > 0");
        PyErr_SetString(PyExc_ValueError, errstr.c_str() );
        return 0;
    }

    void *temp = PyCObject_AsVoidPtr(pyvptr);

// #define NX_CHAR      4 x
// #define NX_FLOAT32   5 x
// #define NX_FLOAT64   6 x
// #define NX_INT8     20 x
// #define NX_UINT8    21 x
// #define NX_INT16    22 x
// #define NX_UINT16   23 x
// #define NX_INT32    24 x
// #define NX_UINT32   25

    PyObject *ret = 0;
    char *vc = 0;
    int *ip = 0;
    double *dp = 0;
    float32 *fp =0;

    int8 *i8p = 0;
    uint8 *ui8p = 0;
    int16 *i16p = 0;
    uint16 *ui16p = 0;
    uint32 *uip = 0;
    switch(type)
    {
        case NX_CHAR:
            vc = static_cast<char *>(temp);
            for(int i=0; i<length; i++)
            {
                char *tempc = PyString_AsString( PyList_GetItem(pylist,i));
                vc[i] = *tempc;
//				std::cout<<"vc[i] = "<<vc[i]<<"\n";
            }
            break;
        case 5:
            fp = static_cast<float *>(temp);
            for(int i=0; i<length; i++)
            {
                double tempd = PyFloat_AsDouble( PyList_GetItem(pylist,i));
                fp[i] = static_cast<float32>(tempd);
            }
            break;
        case 6:
            dp = static_cast<double *>(temp);
            for(int i=0; i<length; i++)
            {
                double tempd = PyFloat_AsDouble( PyList_GetItem(pylist,i));
                dp[i] = tempd;
            }
            break;
// 		case 20:
// 			i8p = new int8[length];
// 			ret = PyCObject_FromVoidPtr(i8p, delete_int8arr);
// 			for(int i=0; i<length; i++)
// 			{
// 				int8 temp = static_cast<int8>(PyFloat_AsDouble(
// 													PyList_GetItem(pylist,i)));
// 				i8p[i] = temp;
// 			}
// 			break;
// 		case 21:
// 			ui8p = new uint8[length];
// 			ret = PyCObject_FromVoidPtr(ui8p, delete_uint8arr);
// 			for(int i=0; i<length; i++)
// 			{
// 				uint8 temp = static_cast<int8>(PyFloat_AsDouble(
// 													PyList_GetItem(pylist,i)));
// 				ui8p[i] = temp;
// 			}
// 			break;
// 		case 22:
// 			i16p = new int16[length];
// 			ret = PyCObject_FromVoidPtr(i16p, delete_int16arr);
// 			for(int i=0; i<length; i++)
// 			{
// 				int16 temp = static_cast<int16>(PyFloat_AsDouble(
// 													PyList_GetItem(pylist,i)));
// 				i16p[i] = temp;
// 			}
// 			break;
// 		case 23:
// 			ui16p = new uint16[length];
// 			ret = PyCObject_FromVoidPtr(ui16p, delete_uint16arr);
// 			for(int i=0; i<length; i++)
// 			{
// 				uint16 temp = static_cast<uint16>(PyFloat_AsDouble(
// 													PyList_GetItem(pylist,i)));
// 				ui16p[i] = temp;
// 			}
// 			break;
        case 24:
            ip = static_cast<int *>(temp);
            for(int i=0; i<length; i++)
            {
                int tempint = PyInt_AsLong( PyList_GetItem(pylist,i));
                ip[i] = tempint;
            }
            break;
        case 25:
            uip = static_cast<unsigned int *>(temp);
            for(int i=0; i<length; i++)
            {
                uint32 tempui = static_cast<uint32>(PyInt_AsLong(
                                                    PyList_GetItem(pylist,i)));
                uip[i] = tempui;
            }
            break;
        default:
            std::string errstr("misc.cc pyNeXus_pylistin2vptr() unknown type");
            PyErr_SetString(PyExc_ValueError, errstr.c_str() );
            return 0;
        }

    return Py_BuildValue("i",0);
}

    
// version
// $Id: misc.cc 46 2007-05-02 16:39:50Z linjiao $

// End of file
