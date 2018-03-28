# Extracting data from XML
# The program will prompt for a URL, read the XML data from that URL using
# urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
xmldata = urllib.request.urlopen(url).read()
print ('Retrieving', url)
tree = ET.fromstring(xmldata)
counts = tree.findall('.//count')
numbers = []
count = 0
for c in counts:
  numbers.append(int(c.text))
  count = count + 1
  
s = 0
for i in numbers:
  s = s + i
  
print ('Count:', count)
print ('Sum:', s)
