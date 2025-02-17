#!/usr/bin/env bash
# to be used for c++ lib/
let CORES=`grep -c ^processor /proc/cpuinfo`
let CORES-=1
if ((CORES < 1)); then
    CORES = 1;
fi

SHAREDLIB=so

PYVER_MAJOR=`python -c "from __future__ import print_function; import sys; print(sys.version_info[0])"`
PYVER_MINOR=`python -c "from __future__ import print_function; import sys; print(sys.version_info[1])"`
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}
echo $PYVER
PY_INCLUDE_DIR=${PREFIX}/include/`ls ${PREFIX}/include/|grep python${PYVER}`
PY_SHAREDLIB=${PREFIX}/lib/`ls ${PREFIX}/lib/|grep libpython${PYVER}[a-z]*.so$`
echo $PY_INCLUDE_DIR
echo $PY_SHAREDLIB

# mkdir build
# cd build
# cmake \
#     -DCONDA_BUILD=TRUE
#     -DCMAKE_INSTALL_PREFIX=$PREFIX \
#     -DDEPLOYMENT_PREFIX=$PREFIX \
#     -DCMAKE_PREFIX_PATH=$PREFIX \
#     -DCMAKE_SYSTEM_LIBRARY_PATH=$PREFIX/lib \
#     -DPYTHON_INCLUDE_DIR=${PY_INCLUDE_DIR} \
#     -DPYTHON_LIBRARY=${PY_SHAREDLIB} \
#     .. \
#     && make && make install
