"""The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
comment counts from the XML data, compute the sum of the numbers in the file.

Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_344840.xml (Sum ends with 57)

The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code
that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the 
data we are parsing in that sample code you will have to make real changes to the code.

To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for 
any tag named 'count' with the following line of code:  counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could 
also work from the top of the XML down to the comments node and then loop through the child nodes of the comments 
node."""

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
sum = 0

uh = urllib.request.urlopen(url).read()
print (uh)
tree = ET.fromstring(uh)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text) # gets 'text' from the 'count' tag ('string number'), from 'tree' (i.e. ET-parsed 'data')
print(sum)
        

