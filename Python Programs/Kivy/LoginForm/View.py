import sqlite3

conn = sqlite3.connect("details.db")
c = conn.cursor()

rec = c.execute(""" SELECT * FROM Info""")  # or use *

for record in rec:
    print('First Name : ' + str(record[0]))
    print('Last Name: ' + str(record[1]))
    print('Email : ' + str(record[2]))
    print('Contact: ' + str(record[3]))

conn.close()
