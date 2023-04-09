#!/home/abraham/bin/python
from datetime import datetime
import sys
file = sys.argv[1]
# open file, get last line
with open(file,'r') as f:
    for line in f:
        pass
    last_line = line
f.close()
# split last line, to get first word
all_words = last_line.split() 
number = int(all_words[0])
print(number)
# write +1 and date to file
f = open(file,'a')
now = datetime.now()
string = "\n" + str(number+1) + " " + now.strftime("%d/%m/%Y %H:%M:%S")
f.write(string)
f.close()
