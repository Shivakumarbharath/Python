import sqlite3
conn=sqlite3.connect("Our_data.db")
c=conn.cursor()

rec=c.execute(""" SELECT ID,name,Dept,STARS FROM Employee_records ORDER BY Dept""")#or use *

for record in rec:
    print('Id : '+str(record[0]))
    print('NAME : ' + str(record[1]))
    print('DEPARTMENT : ' + str(record[2]))
    print('STARS: ' + str(record[3]))

conn.close()