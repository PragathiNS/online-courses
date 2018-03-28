name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

freq = {}
days = []
for lines in handle:
    words = lines.strip().split()
    if lines.startswith('From '):
        day = words[5][0:2]
        days.append(day)

for d in days:
    freq[d] = freq.get(d, 0) + 1

for k in sorted(freq.iterkeys()):
    print ("%s %s" % (k, freq[k]))
