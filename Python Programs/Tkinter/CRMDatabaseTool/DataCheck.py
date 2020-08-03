import sqlite3

bankdet = sqlite3.connect("Crm.db")
c = bankdet.cursor()
det = c.execute("""SELECT *,oid FROM customers """)
print(det.fetchall())
