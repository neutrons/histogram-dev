#!/usr/bin/env bash
echo "HERERERERERERERRRE \n\n\n\n\n"
#lib folder
mkdir -p $PREFIX/include/histogram
cp -r histogram-dev/lib/* $PREFIX/include/histogram/

#Python files
mkdir -p $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram
cp -r histogram-dev/src/histogram/* $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram/

#Executable plothist
mkdir -p $PREFIX/bin
cp -r histogram-dev/bin/plothist $PREFIX/bin/
