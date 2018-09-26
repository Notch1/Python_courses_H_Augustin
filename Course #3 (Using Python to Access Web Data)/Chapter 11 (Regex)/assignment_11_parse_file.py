"""Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers 
in the file and compute the sum of the numbers. 
There are 75 values and the sum ends with 886.
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a 
regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers."""


import re
hand = open('actual.txt')

total = 0
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for i in stuff:
        i = int(i)
        total = total + i
        
print(total)

# A longer way, via 'append' (after line #18):
#        numlist.append(i)
#    
#sump = 0
#for z in numlist:
#    sump = sump + z
#print(sump)

    
#

