# Following links in Python
# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags, scan for a tag that is in a
# particular position relative to the first name in the list, follow that link
# and repeat the process a number of times and report the last name you find

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter positon: ')) - 1

while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print ('Retrieving:', url)
    tags = soup('a')
    url = tags[position].get('href', None)
    count = count - 1
