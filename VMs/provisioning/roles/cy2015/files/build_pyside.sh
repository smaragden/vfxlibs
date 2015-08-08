#!/bin/bash
cd $ROOT
export QT_SDK_HOME=$QT_PREFIX
export PATH=$PYTHON_PREFIX/bin:$PATH
export PYTHONHOME=$PYTHON_PREFIX
export PYTHON_INCLUDE_DIR=$PYTHON_PREFIX/include/python2.7
export PYTHON_INCLUDE_DIRS=$PYTHON_PREFIX/include/python2.7 
export PYTHON_LIBRARY=$PYTHON_PREFIX/lib/python2.7/config/libpython2.7.so
export PYTHON_LIBRARIES=$PYTHON_PREFIX/lib/python2.7/config/libpython2.7.so
export PYTHON_INCLUDE_DIR=/path/to/brewed/python/Headers
export PYTHON_LIBRARY=/path/to/brewed/libpython.dylib

git submodule init
git submodule update
git submodule foreach git checkout master
git submodule foreach git pull

export BUILD_TYPE=Release
export PYTHONXY=python2.7
export PYSIDE_BUILDSCRIPTS_USE_PYTHON3=no
export PATH=$PREFIX/bin:$PATH
export PYTHONPATH=$PREFIX/lib/$PYTHONXY/site-packages:$PREFIX/lib64/$PYTHONXY/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$PREFIX/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH

export PATH=$QT_SDK_HOME/bin:$QT_SDK_HOME/qt/bin:$PATH
export LD_LIBRARY_PATH=$QT_SDK_HOME/lib:$LD_LIBRARY_PATH
export QTDIR=$QT_SDK_HOME:$QT_SDK_HOME/qt:$QTDIR

find . -name CMakeCache.txt -exec rm {} \;

cat <<EOF
    === PySide BuildScripts Configuration ===
    Installation prefix:    $PREFIX
    Build type:             $BUILD_TYPE
    Target Python version:  $PYTHONXY
    Build for Python 3:     $PYSIDE_BUILDSCRIPTS_USE_PYTHON3
EOF


alldirs=("shiboken" "pyside" "pyside-tools")

if [ $# == 0 ] ; then
    dirs=("${alldirs[@]}")
else
    dirs=("$@")
fi

for d in "${alldirs[@]}" ; do
    rm -rf "$d/build"
    mkdir -p "$d/build"
    (
        if [ "`uname -s`" == "Darwin" ]; then
            # When running on Mac OS X, we need to specify the
            # Qt include dir for the header files to be found.
            echo "$0: Mac OS X detected (uname -s gave 'Darwin')."
            PYSIDE_BS_CMAKE_FLAGS="-DALTERNATIVE_QT_INCLUDE_DIR=/Library/Frameworks/"
        else
            # On Non-OS X builds, we enable this to fix a gcc bug
            PYSIDE_BS_CMAKE_FLAGS="-DENABLE_GCC_OPTIMIZATION=On"
        fi

        if [ "$Q_WS_SIMULATOR" == "yes" ]; then
            PYSIDE_BS_CMAKE_FLAGS=$PYSIDE_BS_CMAKE_FLAGS" -DQ_WS_SIMULATOR=yes"
        fi

        if [ "$PYSIDE_BUILDSCRIPTS_USE_PYTHON3" == "yes" ]; then
            PYSIDE_BS_CMAKE_FLAGS=$PYSIDE_BS_CMAKE_FLAGS" -DUSE_PYTHON3=1"
        fi

        cd "$d/build"
        cmake .. -DCMAKE_INSTALL_PREFIX=$PREFIX \
                 -DCMAKE_BUILD_TYPE=$BUILD_TYPE \
                 -DENABLE_ICECC=0 \
                 -DPYTHON_INCLUDE_DIR=$PYTHON_PREFIX/include/${PYTHONXY} \
				 -DPYTHON_LIBRARY=$PYTHON_PREFIX/lib/lib${PYTHONXY}.so \
                 $PYSIDE_BS_CMAKE_FLAGS \
            && make -j4 && make install || exit 1
    ) || exit 1
done
#mkdir -p $PREFIX/lib/python2.7/site-packages
#export PYTHONPATH=$PYTHONPATH:$PREFIX/lib/python2.7/site-packages
#cd $ROOT
#python2.7 setup.py bdist_egg --qmake=$QT_PREFIX/bin/qmake
#easy_install --prefix=$PREFIX dist/PySide-1.3.0.dev0-py2.7-linux-x86_64.egg

#grep -rnhl ${PREFIX} -e "!${PYTHON_PREFIX}/bin/python" | xargs sed -i "s@!${PYTHON_PREFIX}/bin/python@!/usr/bin/env python@g"
