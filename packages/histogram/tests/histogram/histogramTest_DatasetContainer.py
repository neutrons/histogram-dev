#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/initialize",
    "addDataset()",
    "datasetFromName()",
    "datasetFromId()",
    "listDatasets()",
    ]


def test_0( **kwds):

    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()

    return True

    
def test_1( **kwds):

    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = 'dataset'
    name = 'ds1'
    id = 1
    dc.addDataset( name, id, ds)

    passed = True
    if dc._byNames[ name] != ds:
        passed = False
        log("didn't correctly add dataset to _byNames")
    if dc._byIds[ id] != [name, ds]:
        passed = False
        log("didn't correctly add dataset to _byIds")    
    return passed

    
def test_2( **kwds):

    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = 'dataset'
    name = 'ds1'
    id = 1
    dc.addDataset( name, id, ds)

    passed = True
    dsbn = dc.datasetFromName( name)

    if dsbn != ds:
        passed = False
        log("datasetFromName returned %s instead of %s" % (dsbn, ds))
    return passed

    
def test_3( **kwds):

    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = 'dataset'
    name = 'ds1'
    id = 1
    dc.addDataset( name, id, ds)

    passed = True
    dsbi = dc.datasetFromId( id)

    if dsbi != ds:
        passed = False
        log("datasetFromId returned %s instead of %s" % (dsbi, ds))
    return passed

    
def test_4( **kwds):

    from histogram.DatasetContainer import DatasetContainer

    dc = DatasetContainer()
    ds = 'dataset'
    name = 'ds1'
    id = 1
    dc.addDataset( name, id, ds)

    passed = True
    dslist = dc.listDatasets()

    if dslist != [(id, name)]:
        passed = False
        log("listDatasets returned %s instead of %s" % (dslist, [(id,name)]))
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


import utilities

target = "DatasetContainer"

log = utilities.picklog( target)

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id$"

# End of file

