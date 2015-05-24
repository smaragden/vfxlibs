__author__ = 'fredrik.brannbacka'

import sys
import os
import argparse
import tarfile
import shutil

BASE_VARIANT = "Linux" #TODO: Probably change this to a parameter with "Linux" as default value
LIB_CONFIGS = {
    "pyside": {
        "requires": ["python"],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export PYTHONPATH=:!ROOT!/ext/lib/python2.7/site-packages:$PYTHONPATH"
        ]
    },
    "openvdb": {
        "requires": ["python", "boost", "ilmbase"],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH",
            "export PYTHONPATH=:!ROOT!/ext/python/lib/python2.7:$PYTHONPATH"
        ]
    },
    "hdf5": {
        "requires": [],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    },
    "oiio": {
        "requires": ["python", "boost", "openexr"],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH",
            "export PYTHONPATH=:!ROOT!/ext/lib/python/site-packages:$PYTHONPATH"
        ]
    },
    "ilmbase": {
        "requires": ["python", "boost"],
        "commands": [
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH",
            "export PYTHONPATH=:!ROOT!/ext/lib/python2.7/site-packages:$PYTHONPATH"
        ]
    },
    "openexr": {
        "requires": ["ilmbase"],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    },
    "tbb": {
        "requires": [],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    },
    "ocio": {
        "requires": [],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH",
            "export PYTHONPATH=:!ROOT!/ext/lib/python2.7/site-packages:$PYTHONPATH"
        ]
    },
    "fbx": {
        "requires": [],
        "commands": ["export LD_LIBRARY_PATH=!ROOT!/ext/lib/gcc4/x64/release:$LD_LIBRARY_PATH"]
    },
    "alembic": {
        "requires": ["python", "boost", "ilmbase", "hdf5"],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export PYTHONPATH=:!ROOT!/ext//mcp/usr/packages/vfxlibs/alembic/1.5.8/lib:$PYTHONPATH"
        ]
    },
    "qt": {
        "requires": [],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    },
    "python": {
        "requires": [],
        "commands": [
            "export PATH=!ROOT!/ext/bin:$PATH",
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    },
    "boost": {
        "requires": [],
        "commands": [
            "export LD_LIBRARY_PATH=!ROOT!/ext/lib:$LD_LIBRARY_PATH"
        ]
    }
}


def validate_archive(archive):
    if not archive:
        raise (Exception("You need to specify vfxlib archive."))
        return 1
    if not tarfile.is_tarfile(archive):
        raise (Exception(archive + " is not an archive."))
        return 1
    return 0


def validate_path(args, path):
    if os.path.exists(path):
        if not os.listdir(path) == [] and not args.force:
            raise (Exception(path + " is not an empty. --force ?"))
            return 1
    return 0


def extract_archive(archive, libs_root):
    dirs = set();
    print "Extracting libs. This will take a moment."
    with tarfile.open(archive) as tar:
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
    return dirs


def setup_rez_confs(libs, libs_root, rez_root):
    for lib in libs:
        print lib
        create_rez_package(lib, libs_root, rez_root)


def create_rez_package(lib, libs_root, rez_root):
    lib_name = lib[0]
    lib_version = lib[1]

    directory = os.path.join(rez_root, lib_name, lib_version)
    package_file = os.path.join(directory, "package.yaml")

    # Create rez folder structure
    try:
        os.makedirs(os.path.join(directory, "Linux"))
    except:
        pass

    # Create rez package file
    with file(package_file, 'w') as p_file:
        p_file.write("config_version : 0\n\n")
        p_file.write("name: {0}\n\n".format(lib_name))
        p_file.write("version:  {0}\n\n".format(lib[1]))
        if lib_name in LIB_CONFIGS:
            reqs = LIB_CONFIGS[lib_name].get("requires", [])
            if reqs:
                p_file.write("requires:\n")
                for req in reqs:
                    p_file.write("- {0}\n".format(req))
                p_file.write("\n")

        p_file.write("variants:\n")
        p_file.write("- [ Linux ]\n\n")
        if lib_name in LIB_CONFIGS:
            reqs = LIB_CONFIGS[lib_name].get("commands", [])
            if reqs:
                p_file.write("commands:\n")
                for req in reqs:
                    p_file.write("- {0}\n".format(req))
                p_file.write("\n")

    # Create link to library

    os.symlink(os.path.join(libs_root, lib_name, lib_version), os.path.join(directory, "Linux", "ext"))


def main(): #TODO: Put everythin in a class so we don't need to pass everythin around.
    # Setup argument parsing
    parser = argparse.ArgumentParser(description='Generate rez config for vfxlibs.')
    parser.add_argument('--vfxlibs-archive', type=str, default="")
    parser.add_argument('--libs-root', type=str, default="")
    parser.add_argument('--rez-root', type=str, default="")
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    # Validate Arguments
    if validate_archive(args.vfxlibs_archive):
        return 1
    if validate_path(args, args.libs_root):
        return 1
    if validate_path(args, args.rez_root):
        return 1
    vfxlibs_archive = args.vfxlibs_archive
    libs_root = args.libs_root
    rez_root = args.rez_root

    # All Good, let's go

    # Extract the archive and return the libs
    libs = extract_archive(vfxlibs_archive, libs_root)

    setup_rez_confs(libs, libs_root, rez_root)

    return 0


if __name__ == '__main__':
    sys.exit(main())