"""This application will read the mailbox data (mbox.txt) count up the number email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)"""

import sqlite3
# The next 2 steps establish the connection
conn = sqlite3.connect('counting_org.sqlite')  # take a connection object
cur = conn.cursor()  # ask for cursor object (through which you can send commands)

# Call the execute method
cur.execute('''
DROP TABLE IF EXISTS Counts''') 

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)  # filehandler
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    orm = pieces[1]   # extracts email address
    org = orm[orm.find("@")+1:].split()[0] # extracts the part of email after the '@' sign, i.e. between '@' and first whitespace
    #print (org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, )) # the sign '?' is a placeholder
    row = cur.fetchone() # returns a list
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',  # updates id there is an emai
            (org, ))
    # This statement commits outstanding changes to disk each  time through the loop - the program can be 
    # made faster by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'  # SELECT (to read) and ORDER 

print
print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()