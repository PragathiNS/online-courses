# Finding numbers in a haystack

import re

fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for lines in fh:
    line = lines.strip()
    numbers = re.findall('[0-9]+', line)
    for i in numbers:
        lst.append(i)

s = 0
for i in lst:
    s = s + int(i)

print (s)
