import sqlite3

conn = sqlite3.connect("Our_data.db")
c = conn.execute("""INSERT INTO Employee_records(ID,name,dept,STARS)
VALUES(2,'SUJITH','CSE',10)


""")
'''
method 2
c=conn.execute("""INSERT INTO Employee_records(ID,name,dept,STARS)
VALUES(?,?,?,?)


""",(id,name,dept,stars))


'''
conn.commit()
conn.close()
