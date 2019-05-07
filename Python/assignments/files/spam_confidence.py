# Write a program that prompts for a file name, then opens that file and reads through the
# file, looking for lines of the form: [X_DSPAM_Confidence:     0.8475].
# Count these lines and extract the floating point values form each of the lines and compute
# the average of those values.

filename = input('Enter file name: ')

try:
    fh = open(filename)
except:
    print ("Error while opening a file")

count = 0
num = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    ret = float(line[line.find(':') + 1:])
    num = num + ret

print ('Average spam confidence:', num/count)
