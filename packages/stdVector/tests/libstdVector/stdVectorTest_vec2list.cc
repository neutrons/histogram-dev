// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_vec2list.h"
#include "testFrame.h"
//#include "compareVectors.h"
#include "journal/info.h"
#include "journal/debug.h"

namespace
{
    journal::info_t info("ARCSStdVectorTest");
    journal::debug_t debug("ARCSStdVectorTest");
}

namespace ARCSStdVectorTest
{
    using namespace ARCSTest;
    namespace vec2list
    {
        char target[] = "";
        char aspect1[] = "";
    }

    bool test_vec2list()
    {
        using namespace vec2list;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, vec2list::test_1);

        info << journal::endl;
        return passed1;
    }

    namespace vec2list
    {
        bool test_1()
        {
            return false;
        }
    } // vec2list::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_vec2list.cc 2 2004-10-01 18:15:11Z tim $

// End of file
