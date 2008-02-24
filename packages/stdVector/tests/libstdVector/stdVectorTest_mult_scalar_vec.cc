// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_mult_scalar_vec.h"
#include "vec_scalar_arith.h"
#include "journal/info.h"
#include "compareVectors.h"
#include "reporting.h"
#include "testFrame.h"

namespace 
{
    const char target[] = "Pharos::mult_scalar_vec";
    journal::info_t testlog("ARCSDatasetTest");
} // anonymous namespace

namespace ARCSStdVectorTest
{
    using namespace ARCSTest;
    
    namespace mult_scalar_vec
    {
        char aspect1 [] = "simple test";
    }

    bool test_mult_scalar_vec()
    {
        using namespace mult_scalar_vec;

        testlog << journal::at(__HERE__); testlog.newline();

        bool passed1 = 
            testFrame( target, aspect1, testlog, mult_scalar_vec::test_1);

        testlog << journal::endl;
        return passed1;
    }

    namespace mult_scalar_vec
    {
        bool test_1()
        {
            std::vector<double> actual(10,1.0);
            ARCSStdVector::mult_scalar_vec( actual, actual, 3.14159);
            std::vector<double> expected(10, 3.14159);
            return compareFPVectors( actual, expected, 0.000001, testlog);
        }
    }
}



// version
// $Id: stdVectorTest_mult_scalar_vec.cc 2 2004-10-01 18:15:11Z tim $

// End of file
