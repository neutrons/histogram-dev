#!/usr/bin/env bash
echo "-------------  BUILD SCRIPT  -------------"

# write out the _version.py file
python -m pip install . --no-deps --ignore-installed

#lib folder
mkdir -p $PREFIX/include/histogram
cp -r lib/* $PREFIX/include/histogram/

#Python files
mkdir -p $PREFIX/lib/python/site-packages/histogram
cp -r src/histogram/* $PREFIX/lib/python/site-packages/histogram/

#Executable plothist
mkdir -p $PREFIX/bin
cp -r bin/plothist $PREFIX/bin/
