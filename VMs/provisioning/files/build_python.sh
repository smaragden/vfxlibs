#!/bin/bash
ROOT=$1
PREFIX=$2
cd $ROOT
./configure --prefix=$PREFIX --enable-unicode=ucs4 --enable-shared CC="/opt/rh/devtoolset-1.1/root/usr/bin/gcc" CXX="/opt/rh/devtoolset-1.1/root/usr/bin/g++" CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make
sudo make install

# Make sure we use this python in following sessions
echo "export PATH=$PREFIX/bin:\$PATH" >> ~/.bashrc
echo "export LD_LIBRARY=$PREFIX/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc

# Install easy install, pip, wheel and numpy
wget https://bootstrap.pypa.io/ez_setup.py -O - | $PREFIX/bin/python2.7
curl https://bootstrap.pypa.io/get-pip.py | $PREFIX/bin/python2.7
$PREFIX/bin/pip install wheel
$PREFIX/bin/pip install numpy

