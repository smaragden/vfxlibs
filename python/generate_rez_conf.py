__author__ = 'fredrik.brannbacka'

import sys
import os
from optparse import OptionParser
import shutil
from vfxlibs import *
import package_callbacks
import json

with open(os.path.join(os.path.dirname(__file__),"packages.json")) as data_file:
    LIB_CONFIGS = json.loads(data_file.read())


def validate_path(args, path):
    if os.path.exists(path):
        if not os.listdir(path) == [] and not args.force:
            raise (Exception(path + " is not empty. --force ?"))
            return 1
    return 0

def setup_rez_confs(libs, libs_root, rez_root, base_variant):
    for lib in libs:
        print "Configuring: {0}-{1}".format(lib[0],lib[1])
        create_rez_package(lib, libs_root, rez_root, base_variant)


def create_rez_package(lib, libs_root, rez_root, base_variant):
    lib_name = lib[0]
    lib_version = lib[1]

    directory = os.path.join(rez_root, lib_name, lib_version)
    package_file = os.path.join(directory, "package.yaml")

    # Create rez folder structure
    try:
        os.makedirs(os.path.join(directory, base_variant))
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
        p_file.write("- [ {0} ]\n\n".format(base_variant))
        if lib_name in LIB_CONFIGS:
            reqs = LIB_CONFIGS[lib_name].get("commands", [])
            if reqs:
                p_file.write("commands:\n")
                for req in reqs:
                    p_file.write("- {0}\n".format(req))
                p_file.write("\n")

    # Create link to library
    try:
        os.symlink(os.path.join(libs_root, lib_name, lib_version), os.path.join(directory, base_variant, "ext"))
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(os.path.join(directory, base_variant, "ext"))
            os.symlink(os.path.join(libs_root, lib_name, lib_version), os.path.join(directory, base_variant, "ext"))
    
    try:
        methodToCall = getattr(package_callbacks, "relocate_{0}".format(lib_name))
        if methodToCall:
            methodToCall(os.path.join(libs_root, lib_name, lib_version))
    except AttributeError, e:
        pass
        


def main(): #TODO: Put everythin in a class so we don't need to pass everything around.
    parser = OptionParser()
    parser.add_option("-a", "--vfxlibs-archive", dest="vfxlibs_archive", help="vfxlibarchive", metavar="FILE")
    parser.add_option("-l", "--libs-root", dest="libs_root", help="write report to FILE", type="string")
    parser.add_option("-r", "--rez-root", dest="rez_root", help="write report to FILE", type="string")
    parser.add_option("-f", "--force", action="store_true", dest="force")
    parser.add_option("-b", "--base-variant", dest="base_variant", help="variant to have the packages depend on", type="string", default="linux")
    (args, optargs) = parser.parse_args()

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
    base_variant = args.base_variant

    # All Good, let's go

    # Extract the archive and return the libs
    libs = extract_archive(vfxlibs_archive, libs_root)

    setup_rez_confs(libs, libs_root, rez_root, base_variant)

    return 0


if __name__ == '__main__':
    sys.exit(main())