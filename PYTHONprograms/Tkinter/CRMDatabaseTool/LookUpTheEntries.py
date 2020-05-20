from tkinter import *
import sqlite3

root=Tk()

root.title("CRM Tool")
root.geometry("400x500")
titleLabel=Label(root,text="Vedic Math Data Managment",font=('Helvetica',16,'bold'))
titleLabel.place(relx=0.12,rely=0.001)
'''
#connect to database
mydb=sqlite3.connect("Crm.db")
#createe a cursor
c=mydb.cursor()

mydb.commit()
mydb.close()
'''
#functions
def Clear_Fields():
    fn_box.delete(0,END)
    ln_box.delete(0, END)
    zc_box.delete(0, END)
    pp_box.delete(0, END)
    e_box.delete(0, END)
    a1_box.delete(0, END)
    a2_box.delete(0, END)
    city_box.delete(0, END)
    s_box.delete(0,END)
    co_box.delete(0, END)
    ph_box.delete(0, END)

def add_customer():
    sql_command="INSERT INTO customers (first_name,last_name,zip_code,price_paid,email,add1,add2,city,state,country,phone) VALUES {}"
    values=(fn_box.get(),ln_box.get(),zc_box.get(),pp_box.get(),e_box.get(),a1_box.get(),a2_box.get(),city_box.get(),s_box.get(),co_box.get(),ph_box.get())
    mydb = sqlite3.connect("Crm.db")
    # createe a cursor  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)
    c = mydb.cursor()
    c.execute(sql_command.format(values))
    mydb.commit()
    mydb.close()
    Clear_Fields()


def list_cust():
    cust_query=Toplevel()
    cust_query.title("Your Query!!!")
    cust_query.geometry("600x600")


    mydb = sqlite3.connect("Crm.db")
    c = mydb.cursor()
    det = c.execute("""SELECT oid,* FROM customers """)
    details=det.fetchall()
    column=["ID","First Name","Last Name","Zip"]
    for col in range(0, 4):
        lookup_label = Label(cust_query, text=column[col])
        lookup_label.place(relx=col / 4, rely=0)
    for mindex,data in enumerate(details,2):
        for each in range(0,4):
            lookup_label = Label(cust_query, text=data[each])
            lookup_label.place(relx=each/4,rely=mindex/10)





#create main form to enter the fields
x=0.060
fn=Label(root,text="First Name").place(relx=x,rely=0.1)
ln=Label(root,text="Last Name").place(relx=x,rely=0.15)
zc=Label(root,text="Zip Code").place(relx=x,rely=0.2)
pp=Label(root,text="Price Paid").place(relx=x,rely=0.25)
e=Label(root,text="Email").place(relx=x,rely=0.3)
a1=Label(root,text="Address 1").place(relx=x,rely=0.35)
a2=Label(root,text="Address 2").place(relx=x,rely=0.4)
city=Label(root,text="City").place(relx=x,rely=0.45)
s=Label(root,text="State").place(relx=x,rely=0.5)
co=Label(root,text="Country").place(relx=x,rely=0.55)
ph=Label(root,text="Phone").place(relx=x,rely=0.6)


#entery labels
xe=0.3
fn_box=Entry(root)
fn_box.place(relx=xe,rely=0.1)

ln_box=Entry(root)
ln_box.place(relx=xe,rely=0.15)

zc_box=Entry(root)
zc_box.place(relx=xe,rely=0.2)

pp_box=Entry(root)
pp_box.place(relx=xe,rely=0.25)

e_box=Entry(root)
e_box.place(relx=xe,rely=0.3)

a1_box=Entry(root)
a1_box.place(relx=xe,rely=0.35)


a2_box=Entry(root)
a2_box.place(relx=xe,rely=0.4)

city_box=Entry(root)
city_box.place(relx=xe,rely=0.45)

s_box=Entry(root)
s_box.place(relx=xe,rely=0.5)

co_box=Entry(root)
co_box.place(relx=xe,rely=0.55)

ph_box=Entry(root)
ph_box.place(relx=xe,rely=0.6)
#use tab for cursor to move to next entry box


#add buttons

#to add detail into database
add_customer_database=Button(root,text="Submit",command=add_customer)
add_customer_database.place(relx=0.25,rely=0.7)

#to clear the fields
clr=Button(root,text="Clear",command=Clear_Fields)
clr.place(relx=0.4,rely=0.7)

#query Button
list_customer=Button(root,text="List Customers",command=list_cust)
list_customer.place(relx=0.55,rely=0.7)



root.mainloop()