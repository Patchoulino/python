#!/usr/bin/python

import os
stream = os.popen('ls -la')
output = stream.readlines()
print(output)
