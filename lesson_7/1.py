import os
import sys
import shutil

os.makedirs("first")
os.makedirs("second")
os.makedirs("third")

file = sys.argv[0]
path = os.path.dirname(os.path.abspath(file))

shutil.copyfile(file, os.path.join(path, "first", os.path.basename(file)))
