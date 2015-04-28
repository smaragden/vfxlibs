#!/bin/bash
ROOT=$1
PREFIX=$2
cd $ROOT
export CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc"
export CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++"
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"
./bootstrap.sh --prefix=$PREFIX --with-python=/tmp/VFXREFPLAT/BUILDS/CY2015/python/2.7.9/bin/python 
./b2 install --layout=versioned link=static link=shared threading=multi cxxflags=-fPIC
