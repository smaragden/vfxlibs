VFX LIBS
========

Description
-----------

After having to build alot of different libraries that is used in the vfx industry I decided to automate the process.
I use the cfx reference platform as guidlines to what libraries to build. As we use Centos 7 that's what initially is implemented.
But it should be fairly easy to change that. What needs to be done then is to make sure all system dependencies are met.

Libraries
---------
- alembic 1.5.8
- boost 1.55.0
- fbx 2016
- hdf5 1.8.14
- ocio 1.0.9
- oiio 1.5.15
- ilmbase 2.2.0
- openexr 2.2.0
- openvdb 3.0.0
- pyside 1.3.0
- python 2.7.9
- qt 4.8.5
- tbb 4.3.5

To Do's
-------
- Make all libraries relocatable
- Change rpath to relative paths on all libs and exrcutables
- MAke it simpler to choose build os

How To
------
Initial run:
```
shell$ cd VMs
shell$ vagrant up centos7
```

Rerun build process:
```
shell$ vagrant provision centos7
```