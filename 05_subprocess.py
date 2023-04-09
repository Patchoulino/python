#!/home/abraham/bin/python

import subprocess
#subprocess.run('ls')
#subprocess.run(['ls -la'], shell=True)
#x = subprocess.run(['ls', '-la'])
x = subprocess.run(['ls', '-la'], capture_output=True)
#print(x)
print(x.args)
print(x.returncode)
print(x.stdout)
print(x.stderr)
