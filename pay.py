# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 

hrs = input("Enter Hours:")
h = float(hrs)
r = input("Enter rate:")
rate = float(r)

if h <= 40:
    total = h * rate
elif h > 40:
    basic = 40 * rate
    extrahrs = h - 40
    total = basic + (extrahrs * (1.5 * rate))
print (total)
