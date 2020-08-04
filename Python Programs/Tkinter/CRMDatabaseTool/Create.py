from tkinter import *
import sqlite3

root = Tk()

root.title("CRM Tool")
# connect to database
mydb = sqlite3.connect("Crm.db")
# createe a cursor
c = mydb.cursor()

# create a table if not created
c.execute("""CREATE TABLE IF NOT EXISTS customers(
first_name VARCHAR(255),
last_name VARCHAR(255),
zip_code integers(6),
price_paid DECIMAL(4,2),
user_id INT AUTO_INCREAMENT PRIMARY KEY
)""")
'''
first_name
last_name
zip_code integers
price_paid DECIMAL
user_id
email
add1
add2
city
state
country
phone  INTEGER

'''

data = c.execute("SELECT * FROM customers")
print(data.description)

for thing in data.description:
    print(thing[0])
# close the database
mydb.close()

root.mainloop()
