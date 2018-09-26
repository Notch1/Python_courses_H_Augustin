""" The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the 
comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the 
other is the actual data you need to process for the assignment.

    Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://python-data.dr-chuck.net/comments_344844.json (Sum ends with 66)  
    
    "comments":[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
      
                                                                        """
    
import urllib.request, urllib.parse
import json

address = input('Enter location: ')
uh = urllib.request.urlopen(address)
data = uh.read().decode()

# print('Retrieved', len(data), 'characters')
#print(data)
        
try:
    js = json.loads(data) # parses a string containing JSON data so that you can work with the data in Python
except:
    js = None

sum = 0
for coco in js['comments']:    # 'comments' is above 'counts'
    sum = sum + coco['count']    

print(sum)
    


