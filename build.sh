#!/usr/bin/env bash
echo "-------------  BUILD SCRIPT  -------------"
python -m pip install . --no-deps --ignore-installed

#lib folder
mkdir -p $PREFIX/include/histogram
cp -r lib/* $PREFIX/include/histogram/

#Python files
mkdir -p $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram
ls src/histogram/
cp -r src/histogram/* $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram/

#Executable plothist
mkdir -p $PREFIX/bin
cp -r bin/plothist $PREFIX/bin/
