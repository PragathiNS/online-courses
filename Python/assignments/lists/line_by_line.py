# Open the file romeo.txt and read it line by line. For each line split the line
# into a list of words using the spilt() method. The program should build a list
# of words. For each word on each line check to see if the world is already in
# the list and if not append it to the list. Sort and print the resulting words
# in alphabetical order

fname = input('Enter the filename: ')
fh = open (fname)

lst = list()
for line in fh:
    words = line.strip().split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)

lst.sort()
print (lst)
