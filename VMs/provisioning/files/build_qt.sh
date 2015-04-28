#!/bin/bash
ROOT=$1
PREFIX=$2
cd $ROOT
export PATH=/opt/rh/devtoolset-1.1/root/usr/bin:$PATH
export CMAKE_CC_COMPILER="/opt/rh/devtoolset-1.1/root/usr/bin/gcc"
export CMAKE_CXX_COMPILER="/opt/rh/devtoolset-1.1/root/usr/bin/g++"
./configure --prefix=$PREFIX -opensource -confirm-license -no-phonon -no-phonon-backend -dbus-linked -no-qt3support -no-rpath -no-webkit -fast 
gmake
gmake install

# Make sure we use this qt in following sessions
echo "export PATH=$PREFIX/bin:\$PATH" >> ~/.bashrc
echo "export LD_LIBRARY=$PREFIX/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc