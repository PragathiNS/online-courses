# Write a program that prompts for a file name, then opens that file and reads through
# the file, and print the contents of the file in upper case.

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print ('Error on opening file')

for lines in fh:
    line = lines.strip().upper()
    print (line)
