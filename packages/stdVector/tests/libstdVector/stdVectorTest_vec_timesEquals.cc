// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "stdVectorTest_vec_timesEquals.h"
#include "vec_vec_arith.h"

#include "testFrame.h"
#include "compareVectors.h"
#include "journal/info.h"
#include "journal/debug.h"

namespace
{
}

namespace ARCSStdVectorTest
{
    using namespace ARCSTest;
    namespace vec_timesEquals
    {
        char target[] = "ARCSStdVector::vec_timesEquals";
        char aspect1 [] = "with template type double";
        char aspect2 [] = "with template type unsigned int";
        char aspect3 [] = "exception paths";
    }

    bool test_vec_timesEquals()
    {
        journal::info_t info("ARCSStdVectorTest");
        
        using namespace vec_timesEquals;

        info << journal::at(__HERE__) << journal::endl;

        bool passed1 = 
            testFrame( target, aspect1, info, vec_timesEquals::test_1);

        bool passed2 = 
            testFrame( target, aspect2, info, vec_timesEquals::test_2);

        bool passed3 = 
            testFrame( target, aspect3, info, vec_timesEquals::test_3);

        info << journal::endl;
        return passed1 && passed2 && passed3;
    }

    namespace vec_timesEquals
    {
        // test with template type double
        bool test_1()
        {
            journal::info_t info("ARCSStdVectorTest");
    
            std::vector<double> lhs( 4, 3.0);
            std::vector<double> rhs( 5, 2.0);
            ARCSStdVector::vec_timesEquals( rhs, 1,5, lhs, 0);
            std::vector<double> expected( 4, 6.0);
            return compareFPVectors( lhs, expected, 0.000001, info);
        }
        // test with template type unsigned int
        bool test_2()
        {
            journal::info_t info("ARCSStdVectorTest");

            std::vector<unsigned int> lhs( 4, 3);
            std::vector<unsigned int> rhs( 5, 2);
            ARCSStdVector::vec_timesEquals( rhs, 1,5, lhs, 0);
            std::vector<unsigned int> expected( 4, 6);
            return compareIntVectors( lhs, expected, info);
        }
        // test exceptions
        bool test_3()
        {
            journal::info_t info("ARCSStdVectorTest");
    
            std::vector<unsigned int> input( 5, 1);
            std::vector<unsigned int> output( 4, 2);
            bool passed1 = false, passed2 = false, passed3 = false;
            info<<"Testing exceptions:\n";
            try
            {
                ARCSStdVector::vec_timesEquals( input, 6, 5, output, 0);
                info<<"Failed to catch exception on inputBegin > "
                       <<"inputEnd\n";
                info<<"Exception test 1/3 FAILED\n";
            }
            catch ( std::string & errstr)
            {
                info<<errstr<<"\n";
                info<<"Caught exception on inputBegin > inputEnd: "
                       <<"Exception test 1/3 PASSED\n";
                passed1 = true;
            }
            try
            {
                ARCSStdVector::vec_timesEquals( input, 1, 6, output, 0);
                info<<"Failed to catch exception on inputEnd beyond "
                       <<"input size\n";
                info<<"Exception test 2/3 FAILED\n";
            }
            catch ( std::string & errstr)
            {
                info<<errstr<<"\n";
                info<<"Caught exception on inputEnd > input size: "
                       <<"Exception test 2/3 PASSED\n";
                passed2 = true;
            }
            try
            {
                ARCSStdVector::vec_timesEquals( input, 0, 5, output, 0);
                info<<"Failed to catch exception on input range "
                       <<"greater than output size";
                info<<"Exception test 3/3 FAILED\n";
            }
            catch ( std::string & errstr)
            {
                info<<errstr<<"\n";
                info<<"Caught exception from input range greater than "
                       <<"output range: Exception test 3/3 PASSED\n";
                passed3 = true;
            }
            return passed1 && passed2 && passed3;
        } // bool test_3()

    } // vec_timesEquals::

} // ARCSStdVectorTest::



// version
// $Id: stdVectorTest_vec_timesEquals.cc 73 2005-05-17 23:36:46Z tim $

// End of file
