# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the sum, count, average, largest and smallest of the number.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

num = 0
total = 0.0
largest = None
smallest = None
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
  # Largest
  if largest is None:
    largest = fval
  elif largest < fval:
    largest = fval
  # Smallest
  if smallest is None:
    smallest = fval
  if smallest > fval:
    smallest = fval

print (total, num, total/num, largest, smallest)
