import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
# The executescript() method allows us to execute the whole SQL code in one step
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id) 
)
''')
# PRIMARY KEY above is a composite primary key

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ], = [name, title, role]
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data) # a python list

for entry in json_data:    # 'entry' will iterate through the list [0, 1, 2]

    name = entry[0];
    title = entry[1];
    role = entry[2]

    print (name, title, role)
    # cur.execute lines below: inserts the 'name' and gives it a primary key if it sees it for the first time
    # if it sees it 2nd, 3rd... time it doesn't insert it, i.e. does nothing
    # second cur.exectute line selects the primary key created in the first cur.execute line 
    # 'OR IGNORE' means ignore if 'INSERT' causes an error
    cur.execute('''INSERT OR IGNORE INTO User (name)    
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]  # give me one row (there should only be one row) and the [0] element within the row (id)
    
    # repeat for the 'title'
    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', 
        ( user_id, course_id, role ) )

    conn.commit()
    
