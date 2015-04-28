#!/bin/bash
ROOT=$1
PREFIX=$2
export QT_SDK_HOME=$3
PYTHON_ROOT=/tmp/VFXREFPLAT/BUILDS/CY2015/python/2.7.9
export PATH=/opt/rh/devtoolset-1.1/root/usr/bin:$PYTHON_ROOT/bin:$QT_SDK_HOME/bin:$PATH
export CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc"
export CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++"
mkdir -p $PREFIX/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:$PREFIX/lib/python2.7/site-packages
cd $ROOT
python2.7 setup.py bdist_egg --qmake=$QT_SDK_HOME/bin/qmake
easy_install --prefix=$PREFIX dist/PySide-1.3.0.dev0-py2.7-linux-x86_64.egg

