# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

person = []
mail_freq = {}
for lines in handle:
    line = lines.strip()
    words = line.split()
    for word in words:
        if word == 'From':
            person.append(words[1])
            
for per in person:
    if per in mail_freq:
        mail_freq[per] = mail_freq[per] + 1
    else:
        mail_freq[per] = 1
        
count = None
word = None
for i in mail_freq:
    if count is None or count < mail_freq[i]:
        count = mail_freq[i]
        word = i

print (word, count)
