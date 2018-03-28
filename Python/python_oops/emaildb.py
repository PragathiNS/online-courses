import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter the filename: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = peices[1]
    # It's not a good idea to directly write the string in quotes rather use ? as a
    # placeholder and read the value from the variable. Prevents SQL injection
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO COunts (email, count)
        VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                (email,))
    conn.commit()

sqlstr = 'SELECT email, count FORM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print (str(row[0]), row[1])

cur.close()
