import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)  # Reads and de-serializse the 'data' string. fromstring() parses XML from a string                            
                            # and gives back an object (we called it 'tree'), that we can use different methods on.
                            # 'fromstring' is an element inside ET library: we get back the root of the tree.
                            # This line will blow up if there is a formatting mistake in 'data'.

# 'Find' finds a single tag 
print ('Name:', tree.find('name'). text)   # gets 'text' from the 'name' tag (Chuck), from 'tree' (ie parsed 'data')
print ('Attr:',tree.find('email').get('hide'))  # use 'get' method to extract 'yes' from attribute 'hide'
