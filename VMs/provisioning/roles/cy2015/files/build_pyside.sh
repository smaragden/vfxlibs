#!/bin/bash

mkdir -p $PREFIX/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:$PREFIX/lib/python2.7/site-packages
cd $ROOT
python2.7 setup.py bdist_egg --qmake=$QT_PREFIX/bin/qmake
easy_install --prefix=$PREFIX dist/PySide-1.3.0.dev0-py2.7-linux-x86_64.egg

grep -rnhl ${PREFIX} -e "!${PYTHON_PREFIX}/bin/python" | xargs sed -i "s@!${PYTHON_PREFIX}/bin/python@!/usr/bin/env python@g"
