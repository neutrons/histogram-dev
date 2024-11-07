#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved
import logging

logger = logging.getLogger("Histogram")

aspects = [
    "instantiate/initialize",
    "addDataset()",
    "datasetFromName()",
    "datasetFromId()",
    "listDatasets()",
]


def test_0(**kwds):
    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()

    assert True


def test_1(**kwds):
    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = "dataset"
    name = "ds1"
    id = 1
    dc.addDataset(name, id, ds)

    passed = True
    if dc._byNames[name] != ds:
        passed = False
        logger.debug("didn't correctly add dataset to _byNames")
    if dc._byIds[id] != [name, ds]:
        passed = False
        logger.debug("didn't correctly add dataset to _byIds")
    try:
        logger.info('Attempting to log something')
    except Exception as e:
        print(f"Logging failed with error: {e}")
    print(" \n\n\n\n print't correctly add dataset to _byIds")

    assert passed


def test_2(**kwds):
    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = "dataset"
    name = "ds1"
    id = 1
    dc.addDataset(name, id, ds)

    passed = True
    dsbn = dc.datasetFromName(name)

    if dsbn != ds:
        passed = False
        logger.debug("datasetFromName returned {0!s} instead of {1!s}".format(dsbn, ds))
    assert passed


def test_3(**kwds):
    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = "dataset"
    name = "ds1"
    id = 1
    dc.addDataset(name, id, ds)

    passed = True
    dsbi = dc.datasetFromId(id)

    if dsbi != ds:
        passed = False
        logger.debug("datasetFromId returned {0!s} instead of {1!s}".format(dsbi, ds))
    assert passed


def test_4(**kwds):
    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = "dataset"
    name = "ds1"
    id = 1
    dc.addDataset(name, id, ds)

    passed = True
    dslist = dc.listDatasets()

    if dslist != [(id, name)]:
        passed = False
        logger.debug("listDatasets returned {0!s} instead of {1!s}".format(dslist, [(id, name)]))
    assert passed


# ------------- do not modify below this line ---------------


def run(**kwds):
    allPassed = True

    for i, aspect in enumerate(aspects):
        run = eval('test_' + str(i))
        passed = run(**kwds)
        allPassed = allPassed and passed
    return allPassed


if __name__ == "__main__":

    run()

# version
__id__ = "$Id$"

# End of file
