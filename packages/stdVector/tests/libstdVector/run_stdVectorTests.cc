// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "run_stdVectorTests.h"
#include "stdVectorTest_add_scalar_vec.h"
#include "stdVectorTest_add_scalar_vecIt.h"
// #include "stdVectorTest_extractSlice.h"
// #include "stdVectorTest_minusEquals.h"

#include "stdVectorTest_mult_scalar_vec.h"
#include "stdVectorTest_mult_scalar_vecIt.h"
#include "stdVectorTest_vecPlus.h"
#include "stdVectorTest_vec_plusEquals.h"
#include "stdVectorTest_vec_minus.h"
#include "stdVectorTest_vec_minusEquals.h"
#include "stdVectorTest_vec_times.h"
#include "stdVectorTest_vec_timesEquals.h"
#include "stdVectorTest_vec_divideEquals.h"
#include "stdVectorTest_it_plusEquals.h"
// #include "stdVectorTest_reduceSum2d.h"

// #include "stdVectorTest_reduceSum3d.h"
// #include "stdVectorTest_squareVector.h"


#include <iostream>
#include "journal/info.h"
#include "journal/debug.h"
#include "testFrame.h"
#include "reporting.h"

namespace ARCSStdVectorTest
{
    bool run_stdVectorTests()
    {
        using journal::at;
        using journal::endl;
        using ARCSTest::testFrame;
        journal::info_t log("ARCSStdVectorTest");
    
        
        bool addScalarOK = 
            testFrame( "ARCSStdVector::add_scalar_vec", "", log, 
                       ARCSStdVectorTest::test_add_scalar_vec);
        bool addScalarItOK = 
            testFrame( "ARCSStdVector::add_scalar_vecIt", "", log, 
                       ARCSStdVectorTest::test_add_scalar_vecIt);

        bool multScalarOK = 
            testFrame( "ARCSStdVector::mult_scalar_vec", "", log, 
                       ARCSStdVectorTest::test_mult_scalar_vec);

        bool multScalarItOK = 
            testFrame( "ARCSStdVector::mult_scalar_vecIt", "", log, 
                       ARCSStdVectorTest::test_mult_scalar_vecIt);

        bool vec_plusOK = 
            testFrame( "ARCSStdVector::vec_plus", "", log,
                       StdVectorTest::test_vecPlus);

        bool vec_plusEqualsOK = 
            testFrame( "ARCSStdVector::vec_plusEquals", "", log,
                       ARCSStdVectorTest::test_vec_plusEquals);

        bool vec_minusOK = 
            testFrame( "ARCSStdVector::vec_minus", "", log,
                       StdVectorTest::test_vec_minus);

        bool vec_minusEqualsOK = 
            testFrame( "ARCSStdVector::vec_minusEquals", "", log,
                       ARCSStdVectorTest::test_vec_minusEquals);

        bool vec_timesOK = 
            testFrame( "ARCSStdVector::vec_times", "", log,
                       StdVectorTest::test_vec_times);

        bool vec_timesEqualsOK = 
            testFrame( "ARCSStdVector::vec_timesEquals", "", log,
                       ARCSStdVectorTest::test_vec_timesEquals);

        bool vec_divideEqualsOK = 
            testFrame( "ARCSStdVector::vec_divideEquals", "", log,
                       ARCSStdVectorTest::test_vec_divideEquals);

        bool it_plusEqualsOK = 
            testFrame( "ARCSStdVector::it_plusEquals", "", log,
                       ARCSStdVectorTest::test_it_plusEquals);

//         log << at(__HERE__)
//             << "Testing Pharos::vec_divEquals" << endl;
//         bool divEqualsOK = ARCSStdVectorTest::test_divEquals();
//         report( "Pharos::vec_divEquals", divEqualsOK, log); 

//         // extract slice
//         log << at( __HERE__) 
//             << "Testing Pharos::extract_slice" << endl;
//         bool extractSliceOK = ARCSStdVectorTest::test_extractSlice();
//         report( "Pharos::extractSlice", extractSliceOK, log);
        
//         log << at(__HERE__)
//             << "Testing Pharos::vec_minusEquals" << endl;
//         bool minusEqualsOK = ARCSStdVectorTest::test_minusEquals();
//         report( "Pharos::vec_minusEquals", minusEqualsOK, log); 



//         log << at(__HERE__)
//             << "Testing Pharos::reduceSum2d():" << endl;
//         bool reduceSum2dOK = ARCSStdVectorTest::test_reduceSum2d();
//         report( "Pharos::reduceSum2d", reduceSum2dOK, log);

//         log << at(__HERE__)
//             << "Testing Pharos::reduceSum3d()" << endl;
//         bool reduceSum3dOK = ARCSStdVectorTest::test_reduceSum3d();
//         report( "Pharos::reduceSum3d", reduceSum3dOK, log);


//         log << at(__HERE__)
//             << "Testing Pharos::square_vec():" << endl;
//         bool square_vecOK = ARCSStdVectorTest::test_squareVector();
//         report( "Pharos::square_vec", square_vecOK, log);

//         log << at( __HERE__) 
//             << "Testing Pharos::vec_timesEquals" << endl;
//         bool timesEqualsOK = ARCSStdVectorTest::test_timesEquals();
//         report( "Pharos::vec_timesEquals", timesEqualsOK, log);

//         bool allPassed = minusEqualsOK && extractSliceOK && reduceSum2dOK 
//             && reduceSum3dOK && multScalarOK && addScalarOK && plusEqualsOK 
//             && timesEqualsOK && square_vecOK && divEqualsOK;

        bool allPassed = multScalarOK && addScalarOK && addScalarItOK 
            && multScalarItOK && vec_plusEqualsOK && it_plusEqualsOK
            && vec_minusEqualsOK && vec_timesEqualsOK && vec_divideEqualsOK
            && vec_plusOK && vec_minusOK && vec_timesOK;
        return allPassed;
    }
} // ARCSStdVectorTest::


// version
// $Id: run_stdVectorTests.cc 73 2005-05-17 23:36:46Z tim $

// End of file
