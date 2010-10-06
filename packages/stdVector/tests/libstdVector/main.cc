// T. M. Kelley tkelley@caltech.edu (c) 2004

#include "journal/info.h"
#include "run_stdVectorTests.h"

int main( int argc, char **argv)
{
    journal::info_t info("ARCSStdVectorTest");
    info.activate();
    bool allPassed = ARCSStdVectorTest::run_stdVectorTests();

    info << journal::at(__HERE__); info.newline();
    if (allPassed) 
        info << "All tests of stdVector PASSED" << journal::endl;
    else 
        info << "Some test(s) stdVector FAILED" << journal::endl;
    return 0;
}


// version
// $Id: main.cc 2 2004-10-01 18:15:11Z tim $

// End of file
