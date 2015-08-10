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

def main(): #TODO: Put everythin in a class so we don't need to pass everything around.
    parser = OptionParser()
    parser.add_option("-a", "--vfxlibs-archive", dest="vfxlibs_archive", help="Vfxlibs Archive", metavar="FILE")
    parser.add_option("-l", "--libs-root", dest="libs_root", help="Location of extracted libs", type="string")
    parser.add_option("-f", "--force", action="store_true", dest="force")
    (args, optargs) = parser.parse_args()

    # Validate Arguments
    if validate_archive(args.vfxlibs_archive):
        return 1
    if validate_path(args, args.libs_root):
        return 1

    # Extract the archive and return the libs
    libs = extract_archive(args.vfxlibs_archive, args.libs_root)

    for lib in libs:
        lib_name = lib[0]
        lib_version = lib[1]
        print "Configuring: {0}-{1}".format(lib_name,lib_version)
        try:
            methodToCall = getattr(package_callbacks, "relocate_{0}".format(lib_name))
            if methodToCall:
                methodToCall(os.path.join(args.libs_root, lib_name, lib_version))
        except AttributeError, e:
            pass

if __name__ == '__main__':
    sys.exit(main())