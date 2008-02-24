#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import stdVector

def run():
    passed1 = test_roundtripConversion_raw()
    passed2 = test_roundtripConversion()
    return passed1 and passed2


aspects = [
    """Test loading a list into a vector and then loading the vector into
    a list.
    """,
    """Test loading a list into a vector and then loading the vector into
    a list.
    """,
    ]    
    


def test_0():
    """Test loading a list into a vector and then loading the vector into
    a list.
    """
    inlist = [1,2,3,4]
    types = [5,6,24,25]
    allPassed = True
    for atype in types:
        vec = stdVector.pylist2vector( inlist, atype)
        outlist = stdVector.vector2pylist( vec, atype)
        passed = outlist == inlist
        if not passed:
            print "Test failed for type",atype
            print "input list:",inlist
            print "output list:",outlist
        allPassed = allPassed and passed
    return allPassed


def test_1():
    """Test loading a list into a vector and then loading the vector into
    a list.
    """
    from stdVector import vector
    
    inlist = [1,2,3,4]
    types = [5,6,24,25]
    allPassed = True
    for atype in types:
        vec = vector( atype, inlist)
        outlist = vec.asList()
        passed = outlist == inlist
        if not passed:
            print "Test failed for type",atype
            print "input list:",inlist
            print "output list:",outlist
        allPassed = allPassed and passed
    return allPassed


if __name__ == '__main__':
    import journal
    journal.info("stdVector").activate()
    journal.debug("stdVector").activate()
    allPassed = test_roundtripConversion_raw()
    if allPassed:
        print "Raw roundtrip conversion tests PASSED for all types"
    else:
        print "Raw roundtrip conversion tests FAILED for some/all types"

    allPassed = test_roundtripConversion()
    if allPassed:
        print "Roundtrip conversion test using StdVector PASSED for all types"
    else:
        print "Roundtrip conversion test using StdVector FAILED for some/all types"


# version
__id__ = "$Id: stdVectorTest_roundtripConversion.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
