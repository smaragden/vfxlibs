#!/bin/bash

cd $ROOT
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"
./bootstrap.sh --prefix=$PREFIX --with-python=${PYTHON_PREFIX}/bin/python 
./b2 install --layout=versioned link=static link=shared threading=multi cxxflags=-fPIC
