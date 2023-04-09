#!/usr/bin/python

import os
import subprocess
import shutil
from pprint import pprint

# Get your current working directly
# This returns a string
my_cwd = os.getcwd()
print(my_cwd)

# List the contents of a directory
# This returns a list
dir_list = os.listdir(my_cwd)
for item in dir_list:
    print(item)
