import os

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

def relocate_python(root):
    print "Running relocation callback for:", root
    replace_in_file(os.path.join(root,"lib","pkgconfig", "python-2.7.pc"), "/tmp/VFXREFPLAT/BUILDS/CY2015/python/2.7.9", root)
    replace_in_file(os.path.join(root,"lib","python2.7", "_sysconfigdata.py"), "/tmp/VFXREFPLAT/BUILDS/CY2015/python/2.7.9", root)

def relocate_qt(root):
    print "Running relocation callback for:", root
    with open(os.path.join(root,"bin","qt.conf"), 'w') as file:
        file.write("[Paths]\n")
        file.write("Prefix = {0}".format(root))