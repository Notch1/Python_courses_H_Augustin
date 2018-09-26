"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each 
of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string 
a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour."""

fname = open("mbox-short.txt")

bobo = dict()
for line in fname:
    if line.startswith("From "):
        words = line.split()
        # 6th word in 'From' lines is the time
        time = words[5]
        # split time into h, m, sec
        hms = time.split(":")
        # hour is the first 'word' 
        hour = hms[0]     
        bobo[hour] = bobo.get(hour,0) + 1   # creates an (unsorted) histogram; key(hours) first, and 
                                            # value (how many of them) second

# Creates a list of (still unsorted) tuples [( ), ( ), ( )...] with val (how many) first and key (hours) second:
lst = list()   # creates a new, temporary list []
for key, val in bobo.items():
    newtup = (val, key) 
    lst.append(newtup)   # append tuples in reverse (val, key) order

# or this line of code instead of the for loop above (an idiom):
# ( sorted( [ (val,key) for key,val in bobo.items() ] ) )


lst.sort(key=lambda x: x[1]) # lambda is a built-in, 'inline' anonymous function; in this case, it takes the 
                             # single argument x and returns x[1] (i.e. it takes 'value' and returns 'key').
                             # The list is then sorted based on the value of 'key', e.g. (3, '11'), (2, '15')...
print(lst)
#for val, key in lst:
    #print(key, val)  # goes through and prints the whole list, but we go back to the key, val order now that have 
                     # sorted it based on 'key' in the previous step


