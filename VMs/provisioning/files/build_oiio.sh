#!/bin/bash
ROOT=$1
PREFIX=$2
cd $ROOT
make all BOOST_HOME=/tmp/VFXREFPLAT/BUILDS/CY2015/boost/1.55.0 ILMBASE_HOME=/tmp/VFXREFPLAT/BUILDS/CY2015/ilmbase/2.2.0 OPENEXR_HOME=/tmp/VFXREFPLAT/BUILDS/CY2015/openexr/2.2.0  LINKSTATIC=1 MYCC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc" MYCXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++" EXTRA_CPP_ARGS="-fPIC"
mkdir -p $PREFIX
cp -rf dist/linux64/* $PREFIX/