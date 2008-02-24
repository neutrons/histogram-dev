#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

dashes = '-'*45

def picklog():
    try:
        import journal
        info = journal.info("stdVector")
        info.activate()
        log = info.log
    except ImportError, msg:
        print msg
        print "Seems to be no journal, using sys.stdout"
        import sys
        log = sys.stdout.write
    return log

def preReport( log, target, aspect):
    if aspect:
        outstr = "Testing "+target+' '+ aspect + '\n'
    else:
        outstr = "Testing "+target + '\n'
    log( outstr)
    return


def postReport( log, target, aspect, passed):
    if aspect:
        outstr = "Test of "+target+' '+ aspect
    else:
        outstr = "Test of "+target
    if passed:
        log( outstr+ ' PASSED\n' + dashes)
    else:
        log( outstr + ' FAILED\n' + dashes)
    return


def compareFPLists( a, b, tol, log ):

    if len(a) != len(b):
        log( "array size is different: %s != %s" % (len(a), len(b) ) )
        return False
    
    ret = True
    
    for a1,b1 in zip(a,b):
        if abs(a1-b1)>tol: log("%s!=%s" % (a1,b1)); ret = False
        continue
    
    return ret


# version
__id__ = "$Id: utilities.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
