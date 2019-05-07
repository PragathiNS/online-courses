small = None
for i in [2, 10, 9, 0, 34, 22]:
  if small == None:
    small = i
  elif small > i:
    small = i
  print (small, i)
print (small)
