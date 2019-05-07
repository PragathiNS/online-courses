# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input ('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})

print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
  js = json.loads(data)
except:
  js = None

if not js or 'status' not in js or js['status'] != 'OK':
  print('==== Failure To Retrieve ====')
  print(data)

placeid = js["results"][0]["place_id"]
print ('Place id',placeid)
