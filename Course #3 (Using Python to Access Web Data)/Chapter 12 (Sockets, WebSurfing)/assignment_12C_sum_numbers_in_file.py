"""Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to 
http://www.pythonlearn.com/code/urllink2.py. The program will use urllib to read the HTML from the data files 
below, and parse the data, extracting numbers and compute the sum of the numbers in the file. 

Actual data: http://python-data.dr-chuck.net/comments_344843.html (Sum ends with 42)

You do not need to save these files to your folder since your program will read the data directly from the URL. 

The file is a table of names and comment counts. Ignore most of the data except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers. """

import re 
import urllib.request
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_344843.html' or input('Enter -')
html = urllib.request.urlopen(url).read() # open and read 

# print(html)  # let's see what we're working with!

soup = BeautifulSoup(html, "html.parser") # you can use lxml (library) instead of html.parser 

new_list = []

# Retrieve span tags (they mark segments of text between <span> and </span> tags)
tags = soup('span')
for tag in tags:
    #print('TAG:',tag) # prints the whole segment between the span tags
    #print('TAG.text:',tag.text)  # It is the tag.text we need to scan for integers.
    for x in re.findall('[0-9]+', tag.text):
        new_list.append(int(x))

print(new_list)

print('Total:', sum(new_list))

# or 

#total = 0
#for itervar in new_list:
#    total += itervar 
#print('Total: ', total)
