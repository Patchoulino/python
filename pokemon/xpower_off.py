#!/home/abraham/bin/python
# sleep 0.1~ between multiple ones
# port = 4950
import sys, time, math
from datetime import datetime
T = 0.1

if sys.version[0] == '2':
	raw_input("This client only works with python 3, and you're using python 2. You can download python 3 from python.org.\nPress enter to exit.")
	quit()

from tppflush import *

if len(sys.argv) < 2:
	input("To run this client, please supply an IP address from the command line: python3 command_examples.py <3ds ip>\nPress enter to exit.")
	quit()

def poweroff():
    server.press(Special_Buttons.POWER_LONG)
    server.send(print_sent=False)

#Create a client by creating a new LumaInputServer with the 3DS's IP address.
print("Connecting to 3ds..")
serverIP = sys.argv[1]
server = LumaInputServer(serverIP)
time.sleep(5)
print("Powering off!")
poweroff()
