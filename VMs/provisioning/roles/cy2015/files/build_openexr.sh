#!/bin/bash

export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

# IlmBase
cd $ROOT/IlmBase
./bootstrap
./configure --prefix=${ILMBASE_PREFIX}  --enable-namespaceversioning=no --with-pic CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make -j2
make install

export LD_LIBRARY_PATH=${ILMBASE_PREFIX}/lib:${OPENEXR_PREFIX}/lib:${BOOST_PREFIX}/lib:${PYTHON_PREFIX}/lib:$LD_LIBRARY_PATH
cd $ROOT/OpenEXR
./bootstrap
./configure --prefix=${OPENEXR_PREFIX} --with-ilmbase-prefix=${ILMBASE_PREFIX} --enable-namespaceversioning=no --with-pic CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make -j2
make install

cd $ROOT/PyIlmBase
./bootstrap
./configure --prefix=$ILMBASE_PREFIX --with-ilmbase-prefix=${ILMBASE_PREFIX} --enable-namespaceversioning=no --with-boost-include-dir=${BOOST_INCLUDE_PATH} --with-boost-lib-dir=${BOOST_PREFIX}/lib --with-boost-python-libname=${BOOST_PYTHON_LIBRARY} --with-pic PYTHON="${PYTHON_PREFIX}/bin/python"
make -j2
make install


