import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # 'findall' gets us all tags. Returns the LIST of TAGS, not of text.
print (('User count:'), len(lst))  # the length is 2 as there are 2 'users'

for item in lst:
    print ('Name', item.find('name').text)
    print ('Id', item.find('id').text)
    print ('Attribute', item.get("x"))
# as there are 2 users, it will print the name, id and attribute 2x
