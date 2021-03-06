filename = "romeo.txt"
fhandle = open(filename)

counts = {}
for line in fhandle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  
"""lst = []
for k, v in counts.items():
  new_tup = (v, k)
  lst.append(new_tup)
  
lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
  print (k, v)
"""
# Using List Comprehension
print (sorted([(v,k) for k,v in counts.items()], reverse=True))
