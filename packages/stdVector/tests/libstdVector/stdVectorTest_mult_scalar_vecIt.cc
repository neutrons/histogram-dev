// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_mult_scalar_vecIt.h"
#include "testFrame.h"
#include "compareVectors.h"
#include "journal/info.h"
#include "journal/debug.h"
#include "vec_scalar_arith.h"

namespace
{
    journal::info_t info("ARCSStdVectorTest");
    journal::debug_t debug("ARCSStdVectorTest");
}

namespace ARCSStdVectorTest
{
    using namespace ARCSTest;
    namespace mult_scalar_vecIt
    {
        char target[] = "ARCSStdVector::mult_scalar_vecIt";
        char aspect1[] = "simple test, template type double";
    }

    bool test_mult_scalar_vecIt()
    {
        using namespace mult_scalar_vecIt;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, mult_scalar_vecIt::test_1);

        info << journal::endl;
        return passed1;
    }

    namespace mult_scalar_vecIt
    {
        bool test_1()
        {
            std::vector<double> input( 4, 3.1416);
            std::vector<double> output( 4);
            ARCSStdVector::mult_scalar_vecIt( input.begin(), input.end(),
                                             output.begin(), 2.0);
            std::vector<double> exptd( 4, 6.2832);
            return compareFPVectors( output, exptd, 0.00001, info);
        }
    } // mult_scalar_vecIt::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_mult_scalar_vecIt.cc 2 2004-10-01 18:15:11Z tim $

// End of file
