import sqlite3
conn=sqlite3.connect("Our_data.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Employee_records(
ID PRIMARY KEY NOT NULL,
name text NOT NULL,
Dept text NOT NULL,
STARS INTEGER NOT NULL
)
""")
print("Table created")

conn.commit()
conn.close()