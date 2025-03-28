#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved
import logging

logger = logging.getLogger("Histogram")

aspects = [
    "instantiate/initialize",
    "setAttribute()",
    "getAttribute()",  # uses setAttribute()
    "listAttributes()",  # uses setAttribute()
]


def test_0(**kwds):
    from histogram.DictAttributeCont import AttributeCont

    attCont = AttributeCont()
    assert True


def test_1(**kwds):
    from histogram.DictAttributeCont import AttributeCont

    attCont = AttributeCont()

    attCont.setAttribute("name", "timmah!")

    passed = True
    attDict = attCont._attributes
    try:
        name = attDict["name"]
        if name != "timmah!":
            passed = False
            logger.info("value of 'name' attribute ({0!s}) was incorrect".format(name))
    except KeyError:
        passed = False
        logger.info("did not store 'name' as a key")

    assert passed


def test_2(**kwds):
    from histogram.DictAttributeCont import AttributeCont

    attCont = AttributeCont()

    attCont.setAttribute("name", "timmah!")

    passed = True
    name = attCont.getAttribute("name")
    if name != "timmah!":
        passed = False
        logger.info("value of 'name' attribute ({0!s}) was incorrect".format(name))

    assert passed


def test_3(**kwds):
    from histogram.DictAttributeCont import AttributeCont

    attCont = AttributeCont()

    attCont.setAttribute("name", "timmah!")
    attCont.setAttribute("unit", "tons")

    passed = True
    attList = ["name", "unit"]
    acList = attCont.listAttributes()
    if acList != attList:
        passed = False
        logger.info("listAtts() returned {0!s}, should have been {1!s}".format(acList, attList))

    assert passed


# ------------- do not modify below this line ---------------


def run(**kwds):
    allPassed = True

    for i, aspect in enumerate(aspects):
        run = eval('test_' + str(i))
        # utilities.preReport(log, target, aspect)
        passed = run(**kwds)
        # utilities.postReport(log, target, aspect, passed)
        allPassed = allPassed and passed

    return allPassed



if __name__ == "__main__":

    run()

# version
__id__ = "$Id$"

# End of file
