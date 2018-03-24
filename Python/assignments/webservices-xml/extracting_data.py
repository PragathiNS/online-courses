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
# what will the datatype of counts be here? List
counts = tree.findall('.//count')
print (counts)
