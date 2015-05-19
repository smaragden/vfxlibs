#!/bin/bash

cd $ROOT
./configure --prefix=${PREFIX} --with-pic --enable-production --disable-debug --enable-threadsafe --with-pthread=/usr/include,/usr/lib
make
make install