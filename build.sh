#!/usr/bin/env bash
echo "-------------  BUILD SCRIPT  -------------"

#lib folder
mkdir -p $PREFIX/include/histogram
cp -r lib/* $PREFIX/include/histogram/

#Python files
mkdir -p $PREFIX/lib/python/site-packages/histogram
cp -r src/histogram/* $PREFIX/lib/python/site-packages/histogram/

#Executable plothist
mkdir -p $PREFIX/bin
cp -r bin/plothist $PREFIX/bin/
