from tkinter import *
import sqlite3

root=Tk()

root.title("CRM Tool")
#connect to database
mydb=sqlite3.connect("Crm.db")
#createe a cursor
c=mydb.cursor()

#alter the table
c.execute(""" ALTER TABLE customers ADD 
'phone' 'INTEGER';
""")#can add one at a time
#mydb.commit()

data=c.execute("SELECT * FROM customers")
for thing in data.description:
    print(thing)

#close the database
mydb.close()

#root.mainloop()