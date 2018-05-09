#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


"""def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()
"""

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "Get a slice of values in column 3, from rows 1-3:"
    coast = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)

    maxv = max(coast)
    minv = min(coast)
    maxt = coast.index(maxv) + 1
    mint = coast.index(minv) + 1
    print (maxv, maxt, minv, mint)

    # print "\nDATES:"
    maxet = sheet.cell_value(maxt, 0)
    minet = sheet.cell_value(mint, 0)
    # print "Time in Excel format:",
    print (maxet)
    print (minet)
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    maxtime = xlrd.xldate_as_tuple(maxet, 0)
    mintime = xlrd.xldate_as_tuple(minet, 0)
    print (maxtime)
    print (mintime)
    
    data = {
            'maxtime': maxtime,
            'maxvalue': maxv,
            'mintime': mintime, 
            'minvalue': minv, 10,
            'avgcoast': sum(coast)/float(len(coast))
    }
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
