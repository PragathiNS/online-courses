# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# `X-DSPAM-Confidence:    0.8475`
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below.
# Use the file name mbox-short.txt as the file name

def extract(line):
    num_start = line.find(':')
    data_str = line[num_start + 1:]
    #data_str = data_str.strip()
    data = float(data_str)
    return data

fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    ret = extract(line)
    num = num + ret
    
print("Average spam confidence:", num/count)
