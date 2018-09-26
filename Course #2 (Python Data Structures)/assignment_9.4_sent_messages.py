""" 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of 
mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of 
times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer."""


fname = open("mbox-short.txt")

bobo = dict()
for line in fname:
    if line.startswith("From: "):
        words = line.split()
        # select 2nd word in the line:
        gogo = words[1]
        
        bobo[gogo] = bobo.get(gogo,0) + 1

# The last line of the code above is checking if a key is already in a dictionary and assuming a default value (0) 
# if the key is not there. The long version of the code is below:
#        if gogo not in bobo:
#            bobo[gogo] = 1
#        else :
#            bobo[gogo] = bobo[gogo] + 1

# print(bobo)

# Maximum loop (which email address is most frequent?): 
bigcount = None
bigword = None
for pipi,cipi in bobo.items():
    if bigcount is None or cipi > bigcount:
        bigword = pipi
        bigcount = cipi
print(bigword, bigcount)
