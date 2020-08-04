import sqlite3

conn = sqlite3.connect("Our_data.db")
c = conn.cursor()
c.execute("""DELETE FROM Employee_records WHERE ID= 2""")
rec = c.execute("""SELECT * FROM Employee_records""")
print(rec.fetchall())
conn.commit()
conn.close()
