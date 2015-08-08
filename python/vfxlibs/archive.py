#!/bin/env python
import os, errno
import tarfile
import shutil

def validate_archive(archive):
    if not archive:
        raise (Exception("You need to specify vfxlib archive."))
        return 1
    if not tarfile.is_tarfile(archive):
        raise (Exception(archive + " is not an archive."))
        return 1
    return 0

def extract_archive(archive, libs_root):
    dirs = set();
    print "Extracting libs. This will take a moment."
    tar = tarfile.open(archive)
    for path in tar.getnames():
        elems = path.split(os.sep)
        if len(elems) > 1:
            dirs.add(tuple(elems[:2]))
    for directory in map(lambda x:os.path.join(libs_root, x[0]), dirs):
        if os.path.isdir(directory):
            print "Removing dir:", directory
            shutil.rmtree(directory)
    print "Extracting:", archive, "to", libs_root
    tar.extractall(libs_root)
    tar.close()
    return dirs