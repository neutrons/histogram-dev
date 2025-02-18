#!/usr/bin/env bash

#lib folder
mkdir -p $PREFIX/include/histogram
cp -r lib/* $PREFIX/include/histogram/

#shared library
mkdir build_files/
cp -r lib/* build_files/
cd build_files
src_files=$(ls *.cc)

mkdir -p $PREFIX/lib
g++ -c -fPIC $src_files
g++ -shared -o $PREFIX/lib/libhistogram.so $(ls *.o)
cd ../

#Python files
mkdir -p $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram
cp -r src/histogram/* $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram/

#Executable
mkdir -p $PREFIX/bin
cp -r bin/plothist $PREFIX/bin/
