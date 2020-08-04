import sqlite3

bankdet = sqlite3.connect("BankDetails.db")
c = bankdet.cursor()
det = c.execute("""SELECT * FROM details """)
print(det.fetchall())
