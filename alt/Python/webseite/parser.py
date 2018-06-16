__author__ = 'Mark Weinreuter'

import os
import sys

if len(sys.argv) < 2:
    path = input("Pass the .md file or dir")
else:
    path = sys.argv[1]

if not os.path.exists(path):
    print("No such file")

print(os.path.dirname(os.path.realpath(__file__)))


def convert_dir(path):
    files = os.listdir(path)
    for f in files:
        tmp_path = "{}/{}".format(path, f)
        if os.path.isdir(tmp_path):
            convert_dir(tmp_path)
        elif f.endswith(".md"):
            convert_file(tmp_path)


def convert_file(path):
    parts = path.split("/")
    pre_path = os.path.abspath("/".join(parts[:-1]))

    os.makedirs(pre_path,exist_ok=True)
    inFile = os.path.abspath(path)
    outFile = pre_path + ("/%s.html" % parts[-1][:-3])

    command = "pandoc {0} --filter prism_highlight.py --template=template.html --smart -o {1}".format(inFile, outFile)
    print(command)

    os.system(command)


if os.path.isdir(path):
    convert_dir(path)
else:
    convert_file(path)
