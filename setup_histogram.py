#!/usr/bin/env python

def preparePackage( package, sourceRoot = "." ):
    package.changeRoot( sourceRoot )
    #------------------------------------------------------------
    #dependencies
    #
    #------------------------------------------------------------

    #--------------------------------------------------------
    # now add subdirs
    #
    #histogram
    package.addPurePython(
        sourceDir = 'histogram',
        destModuleName = 'histogram' )

    #histogram.applications
    package.addPurePython(
        sourceDir = 'applications',
        #sourceDir = 'applications',
        destModuleName = 'histogram.applications' )

    #apps
    package.addScripts(sourceFiles = [
        "applications/gui/HistogramGUIApp.py",
        "applications/PlotHist.py",
        #"applications/gui/histogramGui.py",
        ] )

    #data
    package.addData(
        sourceDir = "applications/gui/examples",
        destDir = "histogram/applications/gui/examples"
        )

    #etc
    package.addEtc("etc")

    #ndarray
    package.addPurePython(
        sourceDir = 'ndarray',
        destModuleName = 'ndarray' )
    return package


if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('histogram', '0.1.0a')

    preparePackage( package )

    package.setup()

