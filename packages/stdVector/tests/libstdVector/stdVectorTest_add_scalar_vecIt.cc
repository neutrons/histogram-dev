// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_add_scalar_vecIt.h"
#include "vec_scalar_arith.h"
#include "testFrame.h"
#include "compareVectors.h"
#include "journal/info.h"
#include "journal/debug.h"
#include <vector>

namespace
{
    journal::info_t info("ARCSStdVectorTest");
    journal::debug_t debug("ARCSStdVectorTest");
}

namespace ARCSStdVectorTest
{
    using namespace ARCSTest;
    namespace add_scalar_vecIt
    {
        char target[] = "ARCSStdVector::add_scalar_vecIt";
        char aspect1[] = "simple test, template type double";
        char aspect2[] = "simple test, template type unsigned";
    }

    bool test_add_scalar_vecIt()
    {
        using namespace add_scalar_vecIt;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, add_scalar_vecIt::test_1);
        bool passed2 = 
            testFrame( target, aspect2, info, add_scalar_vecIt::test_2);

        info << journal::endl;
        return passed1 && passed2;
    }

    namespace add_scalar_vecIt
    {
        bool test_1()
        {
            std::vector<double> input( 4, 3.14159);
            std::vector<double> output( 4);
            ARCSStdVector::add_scalar_vecIt( input.begin(), input.end(),
                                             output.begin(), 2.0);
            std::vector<double> exptd( 4, 5.14159);
            return compareFPVectors( output, exptd, 0.00001, info);
        }
        bool test_2()
        {
            std::vector<unsigned> input( 4, 2);
            std::vector<unsigned> output( 4);
            ARCSStdVector::add_scalar_vecIt( input.begin(), input.end(),
                                             output.begin(), (unsigned)2);
            std::vector<unsigned> exptd( 4, 4);
            return compareIntVectors( output, exptd, info);
        }
    } // add_scalar_vecIt::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_add_scalar_vecIt.cc 2 2004-10-01 18:15:11Z tim $

// End of file
