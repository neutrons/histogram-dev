// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_list2vec.h"
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
    namespace list2vec
    {
        char target[] = "";
        char aspect1[] = "";
    }

    bool test_list2vec()
    {
        using namespace list2vec;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, list2vec::test_1);

        info << journal::endl;
        return passed1;
    }

    namespace list2vec
    {
        bool test_1()
        {
            return false;
        }
    } // list2vec::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_list2vec.cc 2 2004-10-01 18:15:11Z tim $

// End of file
