#!/usr/bin/env bash

# Create the include directory in the package
echo $PREFIX/include/histogram
ls lib/
mkdir -p $PREFIX/include/histogram
cp -r lib/* $PREFIX/include/histogram/

# Create the lib directory for shared libraries (.so or .dylib files)
# PROJ_SRCS = \
# 	Array_1D.cc \
# 	events2Ix.cc \
# 	events2Ixy.cc \
# 	Event2Quantity.cc \
# 	NdArray.cc \
# 	NdArraySlice.cc \
#mkdir -p $PREFIX/lib
#$(CXX) $(CXXFLAGS) -fPIC $(ls lib/*.cc) -o $PREFIX/lib/libhistogram.so
#cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX .. && make -j 2 && make install

#mkdir -p $PREFIX/lib
#c++ -O3 -Wall -shared -std=c++11 -fPIC $(ls lib) -o $PREFIX/lib/libhistogram.so

#Install the Python files
#mkdir -p $PREFIX/lib/python${PYSHORT_VERSION}/site-packages/histogram
#cp -r src/* $PREFIX/lib/python${PYSHORT_VERSION}/site-packages/histogram/

mkdir -p $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram
cp -r src/histogram/* $PREFIX/lib/python$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')/site-packages/histogram/

mkdir -p $PREFIX/bin
cp -r bin/plothist $PREFIX/bin/
