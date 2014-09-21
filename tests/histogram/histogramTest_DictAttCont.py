#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/initialize",
    "setAttribute()",
    "getAttribute()", # uses setAttribute()
    "listAttributes()", # uses setAttribute()
    ]


def test_0( **kwds):

    from histogram.DictAttributeCont import AttributeCont
    attCont = AttributeCont()
    return True

    
def test_1( **kwds):

    from histogram.DictAttributeCont import AttributeCont
    attCont = AttributeCont()

    attCont.setAttribute( 'name', 'timmah!')

    passed = True
    attDict = attCont._attributes
    try:
        name = attDict['name']
        if name != 'timmah!':
            passed = False
            log("value of 'name' attribute (%s) was incorrect" % name)
    except KeyError:
        passed = False
        log("did not store 'name' as a key")
        
    return passed

    
def test_2( **kwds):

    from histogram.DictAttributeCont import AttributeCont
    attCont = AttributeCont()

    attCont.setAttribute( 'name', 'timmah!')

    passed = True
    name = attCont.getAttribute('name')
    if name != 'timmah!':
        passed = False
        log("value of 'name' attribute (%s) was incorrect" % name)  
        
    return passed


def test_3( **kwds):
    from histogram.DictAttributeCont import AttributeCont
    attCont = AttributeCont()

    attCont.setAttribute( 'name', 'timmah!')
    attCont.setAttribute( 'unit', 'tons')

    passed = True
    attList = ['name', 'unit']
    acList = attCont.listAttributes()
    if acList != attList:
        passed = False
        log("listAtts() returned %s, should have been %s" %(acList, attList))
        
    return passed
    
# ------------- do not modify below this line ---------------


def run( **kwds):
    
    allPassed = True
    
    for i, aspect in enumerate( aspects):
        run = eval( 'test_' + str(i))
        utilities.preReport( log, target, aspect)
        passed = run( **kwds)
        utilities.postReport( log, target, aspect, passed)
        allPassed = allPassed and passed

    return allPassed


import  utilities

target = "DictAttCont"

log = utilities.picklog( target)

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id$"

# End of file

