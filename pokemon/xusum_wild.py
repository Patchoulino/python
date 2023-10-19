#!/home/abagl/bin/python
# run as ./usum_ultrawormhole.py pkmn 192.168.1.
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

def button(btn, timing_on, timing_off):
    match btn:
        case 'up':
            server.press(HIDButtons.DPADUP)
        case 'right':
            server.press(HIDButtons.DPADRIGHT)
        case 'down':
            server.press(HIDButtons.DPADDOWN)
        case 'left':
            server.press(HIDButtons.DPADLEFT)
        case 's_up':
            server.circle_pad_set(CPAD_Commands.CPADUP, 1)
        case 's_down':
            server.circle_pad_set(CPAD_Commands.CPADUP, -1)
        case 's_right':
            server.circle_pad_set(CPAD_Commands.CPADRIGHT, 1)
        case 's_left':
            server.circle_pad_set(CPAD_Commands.CPADRIGHT, -1)
        case 'a':
            server.press(HIDButtons.A)
        case 'b':
            server.press(HIDButtons.B)
        case 'x':
            server.press(HIDButtons.X)
        case 'y':
            server.press(HIDButtons.Y)
        case 'l':
            server.press(HIDButtons.L)
        case 'r':
            server.press(HIDButtons.R)
        case 'zl':
            server.press(HIDButtons.ZL)
        case 'start':
            server.press(HIDButtons.START)
        case 'select':
            server.press(HIDButtons.SELECT)

    server.send(print_sent=False)
    time.sleep(timing_on)

    match btn:
        case 'up':
            server.unpress(HIDButtons.DPADUP)
        case 'right':
            server.unpress(HIDButtons.DPADRIGHT)
        case 'down':
            server.unpress(HIDButtons.DPADDOWN)
        case 'left':
            server.unpress(HIDButtons.DPADLEFT)
        case 's_up':
            server.circle_pad_neutral()
        case 's_down':
            server.circle_pad_neutral()
        case 's_right':
            server.circle_pad_neutral()
        case 's_left':
            server.circle_pad_neutral()
        case 'a':
            server.unpress(HIDButtons.A)
        case 'b':
            server.unpress(HIDButtons.B)
        case 'x':
            server.unpress(HIDButtons.X)
        case 'y':
            server.unpress(HIDButtons.Y)
        case 'l':
            server.unpress(HIDButtons.L)
        case 'r':
            server.unpress(HIDButtons.R)
        case 'zl':
            server.unpress(HIDButtons.ZL)
        case 'start':
            server.unpress(HIDButtons.START)
        case 'select':
            server.unpress(HIDButtons.SELECT)

    server.send(print_sent=False)
    time.sleep(timing_off)

def soft_reset():
    server.press(HIDButtons.L)
    server.press(HIDButtons.R)
    server.press(HIDButtons.START)
    server.send(print_sent=False)
    time.sleep(0.2)
    #server.clear_everything()
    server.unpress(HIDButtons.L)
    server.unpress(HIDButtons.R)
    server.unpress(HIDButtons.START)
    server.send(print_sent=False)
    time.sleep(T)

    file = sys.argv[1]
    with open(file,'r') as f:
        for line in f:
            pass
        last_line = line
    f.close()
    # split last line, to get first word
    all_words = last_line.split()
    number = int(all_words[0])
    # print(number)
    # write +1 and date to file
    f = open(file,'a')
    now = datetime.now()
    string = "\n" + str(number+1) + " " + now.strftime("%d/%m/%Y %H:%M:%S")
    f.write(string)
    print(string, end ="")
    f.close()

#Create a client by creating a new LumaInputServer with the 3DS's IP address.
print("Connecting to 3ds..")
serverIP = sys.argv[2]
server = LumaInputServer(serverIP)
time.sleep(5)
print("Connected!")

while True:
    for i in range(75):     # 15 sec
        button('a', T, T)
    server.press(HIDButtons.B)
    for i in range(37):     # 15~ sec
        button('s_up', T, 0)
        button('s_left', T, 0)
        button('s_down', T, 0)
        button('s_right', T, 0)
    server.unpress(HIDButtons.B)
    server.send(print_sent=False)
    for i in range(15):     # 3 sec
        button('b', T, T)
    soft_reset()
