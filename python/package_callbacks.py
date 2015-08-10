import os
from glob import glob
def relocate(func_to_decorate):
    def new_func(*original_args, **original_kwargs):
        root = original_args[0]
        p_root, lib, version = root.rsplit(os.sep, 2)
        original_kwargs["root"] = root
        original_kwargs["p_root"] = p_root
        original_kwargs["lib"] = lib
        original_kwargs["version"] = version
        return func_to_decorate(*original_args, **original_kwargs)
    return new_func

def replace_in_file(filename, search, replace):
    # Read in the file
    filedata = None
    with open(filename, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(search, replace)

    # Write the file out again
    with open(filename, 'w') as file:
      file.write(filedata)

@relocate
def relocate_python(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "python-2.7.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","python2.7", "_sysconfigdata.py"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])

@relocate
def relocate_pyside(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    replace_in_file(os.path.join(kwargs["root"],"include","PySide", "pyside_global.h"), "/tmp/VFXREFPLAT/BUILDS/CY2015/", kwargs["p_root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "pyside.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "shiboken.pc"), "/tmp/VFXREFPLAT/BUILDS/CY2015/", kwargs["p_root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","cmake", "PySide-1.2.2","PySideConfig.cmake"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","cmake", "PySide-1.2.2","PySideConfig-python2.7.cmake"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","cmake", "Shiboken-1.2.2","ShibokenConfig.cmake"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","cmake", "Shiboken-1.2.2","ShibokenConfig-python2.7.cmake"), "/tmp/VFXREFPLAT/BUILDS/CY2015/", kwargs["p_root"])

@relocate
def relocate_ilmbase(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "IlmBase.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "PyIlmBase.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])

@relocate
def relocate_openexr(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "OpenEXR.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])

@relocate
def relocate_ocio(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    replace_in_file(os.path.join(kwargs["root"],"lib","pkgconfig", "OpenColorIO.pc"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
    replace_in_file(os.path.join(kwargs["root"],"share","ocio", "setup_ocio.sh"), os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])

@relocate
def relocate_qt(*args, **kwargs):
    print "Running relocation callback for:", "{0}-{1}".format(kwargs["lib"],kwargs["version"])
    with open(os.path.join(kwargs["root"],"bin","qt.conf"), 'w') as file:
        file.write("[Paths]\n")
        file.write("Prefix = {0}".format(kwargs["root"]))
    pc_files = glob("{0}/*.pc".format(os.path.join(kwargs["root"], "lib", "pkgconfig")))
    for pc_file in pc_files:
        replace_in_file(pc_file, os.path.join("/tmp/VFXREFPLAT/BUILDS/CY2015/",kwargs["lib"],kwargs["version"]), kwargs["root"])
