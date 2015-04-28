#!/bin/bash
ROOT=$1
PREFIX=$2
export CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc"
export CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++"
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

# IlmBase
cd $ROOT/IlmBase
./bootstrap
./configure --prefix=$PREFIX/ilmbase/2.2.0  --enable-namespaceversioning=no --with-pic CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc" CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++" CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make
make install

export LD_LIBRARY_PATH=$PREFIX/lib:$LD_LIBRARY_PATH
cd $ROOT/OpenEXR
./configure --prefix=$PREFIX/openexr/2.2.0 --with-ilmbase-prefix=/tmp/VFXREFPLAT/BUILDS/CY2015/ilmbase/2.2.0 --enable-namespaceversioning=no --with-pic CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc" CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++" CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make
make install

cd $ROOT/PyIlmBase
./configure --prefix=/tmp/VFXREFPLAT/BUILDS/CY2015/ilmbase/2.2.0 --with-ilmbase-prefix=/tmp/VFXREFPLAT/BUILDS/CY2015/ilmbase/2.2.0 --enable-namespaceversioning=no --with-boost-include-dir=/tmp/VFXREFPLAT/BUILDS/CY2015/boost/1.55.0/include/boost-1_55 --with-boost-lib-dir=/tmp/VFXREFPLAT/BUILDS/CY2015/boost/1.55.0/lib --with-boost-python-libname=boost_python-gcc47-mt-1_55 --with-pic PYTHON="/tmp/VFXREFPLAT/BUILDS/CY2015/python/2.7.9/bin/python"
make
make install


