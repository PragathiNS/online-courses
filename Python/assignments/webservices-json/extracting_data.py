# Extracting data from XML
# The program will prompt for a URL, read the XML data from that URL using
# urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url)
dd = data.read()
info = json.loads(dd)

numbers = []
count = 0
for item in info['comments']:
  numbers.append(int(item['count']))
  count = count + 1
  
s = 0
for i in numbers:
  s = s + i
  
print ('Count:', count)
print ('Sum:', s)
