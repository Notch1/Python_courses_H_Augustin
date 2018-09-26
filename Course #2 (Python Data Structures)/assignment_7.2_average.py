# Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute 
# the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter as the file name.

# Use the file name mbox-short.txt as the file name

spam = []
count = 0
total = 0

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        sdb = line[20:26].strip()
        bab = float(sdb)
        total = total + bab
        count = count + 1

pop = total/count
print ('Average spam confidence:', pop)

#total = sum(float(item) for item in spam)
#print(total)
#print(total/count)
        