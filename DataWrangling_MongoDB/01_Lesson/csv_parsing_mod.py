import os
import csv
import pprint

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        dd = csv.DictReader(f)
        for line in dd:
            print (line)
            data.append(line)
    return data

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    pprint.pprint(d)
