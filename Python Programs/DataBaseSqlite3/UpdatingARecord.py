import sqlite3

conn = sqlite3.connect("Our_data.db")
c = conn.cursor()
c.execute(""" UPDATE Employee_records set name='S.Bharath' WHERE ID= {}""".format(1))
rec = c.execute("""SELECT * FROM Employee_records""")
print(rec.fetchall())
conn.commit()
conn.close()
