#!/bin/bash
cd $ROOT
./configure --prefix=$PREFIX -opensource -confirm-license -no-phonon -no-phonon-backend -no-dbus -no-qt3support -no-rpath -no-webkit -fast 
gmake -j2
gmake install

grep -q -F "export PATH=${PREFIX}/bin:\$PATH" ~/.bashrc || echo "export PATH=${PREFIX}/bin:\$PATH" >> ~/.bashrc
grep -q -F "export LD_LIBRARY_PATH=${PREFIX}/lib:\$LD_LIBRARY_PATH" ~/.bashrc || echo "export LD_LIBRARY_PATH=${PREFIX}/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc