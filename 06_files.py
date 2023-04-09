#!/home/abraham/bin/python
import os

f = open('./06_files.py.txt','r')
number = int(f.read())
print(number)
f.close()

f = open('./06_files.py.txt','w')
f.write(str(number+1))
f.close()
