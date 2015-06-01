VFX LIBS
========

Description
-----------

After having to build alot of different libraries that is used in the vfx industry I decided to automate the process.
I use the vfx reference platform as guidlines to what libraries to build. As we use Centos 7 that's what initially is implemented.
But it should be fairly easy to change that. What needs to be done then is to make sure all system dependencies are met.

Supported Platform
------------------
- Only Centos for now

Requirements
------------
- [VirtualBox](https://www.virtualbox.org)
- [Vagrant](http://www.vagrantup.com) 
- [Ansible](http://www.ansible.com)

Libraries
---------
- [alembic 1.5.8](https://github.com/alembic/alembic)
- [boost 1.55.0](http://www.boost.org)
- [fbx 2016](http://www.autodesk.com/products/fbx/overview)
- [hdf5 1.8.14](https://www.hdfgroup.org/HDF5/)
- [ocio 1.0.9](http://opencolorio.org)
- [oiio 1.5.15](https://sites.google.com/site/openimageio/home)
- [ilmbase 2.2.0](https://github.com/openexr/openexr)
- [openexr 2.2.0](https://github.com/openexr/openexr)
- [openvdb 3.0.0](http://www.openvdb.org)
- [pyside 1.3.0](http://www.pyside.org)
- [python 2.7.9](https://www.python.org)
- [qt 4.8.5](http://www.qt.io/developers/)
- [tbb 4.3.5](https://www.threadingbuildingblocks.org)

To Do's
-------
- Make all libraries relocatable
- Change rpath to relative paths on all libs and executables
- Make it simpler to choose build os

Notes
-----
- Alembic is built in c++11 mode but that should probably be optional.
- This is not a strict translation of the vfx reference platforms specification, but a collection of libs that fits my needs. In the future i might have this repo match vfx reference platform rather than my own preferences.

How To
------
Initial run:
```
shell$ git clone https://github.com/smaragden/vfxlibs.git
shell$ cd vfxlibs/VMs
shell$ vagrant up centos7
```

Rerun build process:
```
shell$ vagrant provision centos7
```
