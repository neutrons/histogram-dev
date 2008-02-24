// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_it_plusEquals.h"
#include "vec_vec_arith.h"
#include "testFrame.h"
#include "compareVectors.h"
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
    namespace it_plusEquals
    {
        char target[] = "ARCSStdVector::it_plusEquals()";
        char aspect1[] = "simple test, template type double";
        char aspect2[] = "simple test, template type unsigned";
    }

    bool test_it_plusEquals()
    {
        using namespace it_plusEquals;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, it_plusEquals::test_1);
        bool passed2 = 
            testFrame( target, aspect2, info, it_plusEquals::test_2);

        info << journal::endl;
        return passed1 && passed2;
    }

    namespace it_plusEquals
    {
        bool test_1()
        {
            std::vector<double> lhs( 4, 3.0);
            std::vector<double> rhs( 5, 1.0);
            ARCSStdVector::it_plusEquals
                <std::vector<double>::iterator, double>
                ( rhs.begin(), rhs.begin()+4, lhs.begin());
            std::vector<double> expected( 4, 4.0);
            return compareFPVectors( lhs, expected, 0.000001, info);
        }
        // test with template type unsigned int
        bool test_2()
        {
            std::vector<unsigned int> lhs( 4, 3);
            std::vector<unsigned int> rhs( 5, 1);
            ARCSStdVector::it_plusEquals
                <std::vector<unsigned>::iterator, unsigned>
                ( rhs.begin()+1, rhs.end(), lhs.begin());
            std::vector<unsigned int> expected( 4, 4);
            return compareIntVectors( lhs, expected, info);
        }
    } // it_plusEquals::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_it_plusEquals.cc 2 2004-10-01 18:15:11Z tim $

// End of file
