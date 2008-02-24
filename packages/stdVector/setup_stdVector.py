#!/usr/bin/env python


def preparePackage( package, sourceRoot = "." ):
    package.changeRoot( sourceRoot )
    #------------------------------------------------------------
    #dependencies
    #
    from distutils_adpt.paths.Paths import Paths
    #------------------------------------------------------------
    #python itself
    from distutils_adpt.paths.Python import name as pathsName
    pythonPaths = Paths(pathsName)
    #numpy
    from distutils_adpt.paths.Numpy import name as pathsName
    numpyPaths = Paths(pathsName)


    #------------------------------------------------------------
    #include directories
    package.addIncludeDirs(pythonPaths.includes)



    #--------------------------------------------------------
    # now add subdirs
    #
    #stdVector
    package.addPurePython(
        sourceDir = 'stdVector',
        destModuleName = 'stdVector' )

    #lib
    package.addCLib(
        libName = 'stdVector',
        libDir = 'libstdVector',
        libs = ['journal'],
        libdirs = pythonPaths.clibs,
        macros = [('BLD_PROCEDURE',None)],
        linkArgs = [] )

    #module
    package.addModule(
        moduleDir = 'stdVectormodule',
        include_dirs = numpyPaths.includes,
        libs = ['journal', 'stdVector'],
        libdirs = [],
        macros = [('BLD_PROCEDURE',None)],
        dest = 'stdVector.stdVector' )

    return package



if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('stdVector', '0.1.0a')

    preparePackage( package )

    package.setup()

