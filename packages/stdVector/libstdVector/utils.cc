// T. M. Kelley tkelley@caltech.edu (c) 2004


#include "utils.h"

namespace ARCSStdVector
{

    ObjectWrapper::ObjectWrapper( int magicNum, int type)
    : m_magicNumber(magicNum), m_type( type + magicNum)
    {
    }

}
// version
// $Id: utils.cc 118 2006-04-17 06:41:49Z jiao $

// End of file
