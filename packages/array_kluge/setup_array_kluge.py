#!/usr/bin/env python

def preparePackage( package, sourceRoot = "." ):
    package.changeRoot ( sourceRoot )

    #------------------------------------------------------------
    #dependencies
    #
    from distutils_adpt.paths.Numpy import paths as NumpyPaths
    from distutils_adpt.paths.Paths import Paths
    #------------------------------------------------------------

    #--------------------------------------------------------
    # now add subdirs
    #
    #array_kluge
    package.addPurePython(
        sourceDir = 'array_kluge',
        destModuleName = 'array_kluge' )

    #lib
    package.addCLib(
        libName = 'array_kluge',
        libDir = 'lib',
        linkArgs = [] )

    #module
    package.addModule(
        moduleDir = 'module',
        include_dirs = NumpyPaths.includes,
        libs = ['array_kluge'],
        dest = 'array_kluge.array_kluge' )

    return package



if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('array_kluge', '0.1.0a')

    preparePackage(package)

    package.setup()

