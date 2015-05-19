#!/bin/bash
cd $ROOT
./configure --prefix=$PREFIX --enable-unicode=ucs4 --enable-shared CFLAGS="-fPIC" CXXFLAGS="-fPIC" LDFLAGS="-fPIC"
make
make install

export PATH=${PREFIX}/bin:$PATH
export LD_LIBRARY_PATH=${PREFIX}/lib:$LD_LIBRARY_PATH
# Install easy install, pip, wheel and numpy
curl https://bootstrap.pypa.io/get-pip.py | python
pip install wheel
pip install numpy
pip install epydoc
grep -rnhl ${PREFIX} -e "!${PREFIX}/bin/python" | xargs sed -i "s@!${PREFIX}/bin/python@!/usr/bin/env python@g"

grep -q -F "export PATH=${PREFIX}/bin:\$PATH" ~/.bashrc || echo "export PATH=${PREFIX}/bin:\$PATH" >> ~/.bashrc
grep -q -F "export LD_LIBRARY_PATH=${PREFIX}/lib:\$LD_LIBRARY_PATH" ~/.bashrc || echo "export LD_LIBRARY_PATH=${PREFIX}/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc

