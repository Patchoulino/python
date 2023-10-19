#!/home/abagl/bin/python
import sys, time, math

if sys.version[0] == '2':
	raw_input("This client only works with python 3, and you're using python 2. You can download python 3 from python.org.\nPress enter to exit.")
	quit()

from tppflush import *

if len(sys.argv) < 2:
	input("To run this client, please supply an IP address from the command line: python3 command_examples.py <3ds ip>\nPress enter to exit.")
	quit()


#Create a client by creating a new LumaInputServer with the 3DS's IP address.

serverIP = sys.argv[1]
server = LumaInputServer(serverIP)
time.sleep(5)

server.send(print_sent=False)
time.sleep(0.5)
server.clear_everything()
