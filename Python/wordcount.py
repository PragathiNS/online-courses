filename = "words.txt"
fhandle = open(filename)

word_count = {}
for line in fhandle:
  words = line.split()
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  
bigCount = 0
bigWord = 0
for word, count in word_count.items():
  if bigCount is None or count > bigCount:
    bigCount = count
    bigWord = word

print (bigWord, bigCount)
