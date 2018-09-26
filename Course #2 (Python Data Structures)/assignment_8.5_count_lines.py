# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' 
# like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

# opens the text doc
fname = open("mbox-short.txt")
count = 0

for line in fname:
    # strips newlines
    line = line.rstrip()
    if line.startswith("From "):  
        #breaks the line (a string) into parts (words)
        words = line.split()
        # add line to the (initially empty) list
        words.append(line)

print(words[1])
count += 1


print("There were", count, "lines in the file with From as the first word")

