# Scraping numbers from HTML using BeautifulSoup
# The program uses urllib to read the HTML from the data files, and parse the
# data, extracting numbers and compute the sum of the numbers in the file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all <span> tags
tags = soup('span')
numbers = []
for tag in tags:
    numbers.append(int(tag.contents[0]))

s = 0
for i in numbers:
    s = s + i

print (s)
