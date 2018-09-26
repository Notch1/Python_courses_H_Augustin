"""The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that 
data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a 
place as within Google Maps.

API End Points
To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
http://python-data.dr-chuck.net/geojson

This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can 
test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which 
can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the 
address= parameter that is properly URL encoded using the urllib.urlencode() fuction.

Turn In
Please run your program to find the place_id for this location:
Faculty of Technical Sciences Novi Sad Serbia

Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The 
first seven characters of the place_id are "ChIJVTT ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work 
with the Google API - but the place_id may not match for this assignment. """

import urllib.request
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print ('Retrieved',len(data),'characters')
    #print(data)

    try:
        js = json.loads(data) # parses a string containing JSON data so that you can work with the data in Python
    except:
        js = None
    placeID = js["results"][0]["place_id"]
    print(placeID)
