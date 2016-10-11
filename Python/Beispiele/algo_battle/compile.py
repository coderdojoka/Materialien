import sys

major, minor = sys.version_info[:2]

if major != 3 or minor != 5:
    print("Please use python 3.5!")
    exit()

if len(sys.argv) < 2:
    script = input("Please enter your script: ")
else:
    script = sys.argv[1]

# Compile script
import py_compile
res = py_compile.compile(script)

# Copy file
from shutil import copyfile
copyfile(res, script + "c")
