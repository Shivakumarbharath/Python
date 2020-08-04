import sqlite3

bankdet = sqlite3.connect("BankDetails.db")

c = bankdet.cursor()

c.execute(""" CREATE TABLE  details 
          
(

name text,
age integer,
acn integer PRIMARY KEY NOT NULL,
min integer ,
pin int,
bal integer
)

""")

bankdet.commit()
bankdet.close()
