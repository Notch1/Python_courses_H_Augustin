""" In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= values from the 
anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that 
link and repeat the process a number of times and report the last name you find. 

Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Prithvi.html

Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is 
the last name that you retrieve. Hint: The first character of the name of the last page that you will load is: R.
"""

import urllib.request
from bs4 import BeautifulSoup

#print(html)

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# The code will loop the amount of times as specified in the input, each time it will take the href at 
# the given position and replace it with the url, in that way each loop will look further in the tree structure.

#perform the loop "count" (7) times.
for i in range(count):
    html = urllib.request.urlopen(url) #.read()
    soup = BeautifulSoup(html, 'lxml')
    tags=soup.findAll('a')
    for tag in tags:
        url= tag.get('href')
        tags=soup.findAll('a')
        url = tags[position-1].get('href')
print(url)


# Alternative way -  starts after line 20 (position)
#names = []
#
#while count > 0:
#    print ("retrieving: {0}".format(url))
#    page = urllib.request.urlopen(url)
#    soup = BeautifulSoup(page)
#    anchors = soup('a')
#    name = anchors[position-1].string
#    names.append(name)
#    url = anchors[position-1]['href']
#    count -= 1
#
#print (names[-1])

