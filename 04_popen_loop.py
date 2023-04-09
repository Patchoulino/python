#!/usr/bin/python

import os
stream = os.popen('ls -la')
output = stream.readlines()
#print(output)
for item in output:
	print(item)
