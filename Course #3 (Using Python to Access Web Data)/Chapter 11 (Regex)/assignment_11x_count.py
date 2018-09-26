# Sample text. There are 87 values with a sum=445822

import re
hand = open('sample.txt')


total = 0

for line in hand:
    line = line.rstrip()
    stuff = re.findall("[0-9]+", line)
    for i in stuff:
        i = int(i)
        total = total + i
        
print(total)
