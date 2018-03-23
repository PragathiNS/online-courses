num = 0
total = 0.0
while True:
  sval = input('Enter a number: ')
  if sval == 'done':
    break
  try:
    fval = float(sval)
  except:
    print ('Invalid Input')
    continue
  num = num + 1
  total = total + fval

print (total, num, total/num)
