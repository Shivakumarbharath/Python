from tkinter import *
import sqlite3

root=Tk()
root.geometry("500x600")


#First thing to do is to create a database or connect to one
conn=sqlite3.connect("address_book.db")
#create a cursor
#we use  a cursor to make things
#for example to execute something
c=conn.cursor()


#create a table But only one time
#so execute only once
'''
c.execute(""" CREATE TABLE addresses (

First_name text,
Last_name text,
address text,
city text ,
state text,
zipcode integer


)





""")



'''
#create submit function
def submit():
    #whenever the function opens we have to connect the database commit and close every time
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:Fe,:Le,:addE,:cityE,:stateE,:zipE)",
              {
                  'Fe':Fe.get(),
                  'Le':Le.get(),
                  'addE':addE.get(),
                  'cityE':cityE.get(),
                  'stateE':stateE.get(),
                  'zipE':zipE.get()
              }


              )







    conn.commit()
    conn.close()

    '''clear the text boxes'''
    Fe.delete(0,END)
    Le.delete(0,END)
    addE.delete(0, END)
    cityE.delete(0, END)
    stateE.delete(0, END)
    zipE.delete(0, END)
    return

#create query function
def query():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    record=c.fetchall()
    print(record)
    text=''
    for rec in record:
        text+=str(rec[0])+' ' +str(rec[1])+' \n'

    qlabel=Label(root,text=text)
    qlabel.place(x=100,y=550)
    conn.commit()
    conn.close()


#create Entries and labels

MainLabel=Label(root,text="Address Book",relief="solid",font=("ariel",20,"bold"))
MainLabel.place(x=150,y=20)

FLabel=Label(root,text="First Name: ",padx=10,pady=10,font=('ariel',14))
FLabel.place(x=40,y=105)

Fe=Entry(root,width=30,borderwidth=5)
Fe.place(x=160,y=115)


LLabel=Label(root,text="Last Name: ",padx=10,pady=10,font=('ariel',14))
LLabel.place(x=40,y=165)
Le=Entry(root,width=30,borderwidth=5)
Le.place(x=160,y=175)

addLabel=Label(root,text="Address: ",padx=10,pady=10,font=('ariel',14))
addLabel.place(x=40,y=225)
addE=Entry(root,width=30,borderwidth=5)
addE.place(x=160,y=235)

cityLabel=Label(root,text="City: ",padx=10,pady=10,font=('ariel',14))
cityLabel.place(x=40,y=290)
cityE=Entry(root,width=30,borderwidth=5)
cityE.place(x=160,y=300)


stateLabel=Label(root,text="State: ",padx=10,pady=10,font=('ariel',14))
stateLabel.place(x=40,y=355)
stateE=Entry(root,width=30,borderwidth=5)
stateE.place(x=160,y=365)


zipLabel=Label(root,text="Zipcode: ",padx=10,pady=10,font=('ariel',14))
zipLabel.place(x=40,y=430)
zipE=Entry(root,width=30,borderwidth=5)
zipE.place(x=160,y=440)

#create submit button

logbtn=Button(root,text="Submit",padx=5,pady=5,relief=RAISED,bg="red",command=submit)
logbtn.place(x=100,y=500)

#quit button
qbtn=Button(root,text=" Show Records",padx=5,pady=5,relief=RAISED,bg="red",command=query)
qbtn.place(x=200,y=500)






#anytime we make change to the database we need to commit those changes to the database
#to do that
#commit changes
conn.commit()
#finally we close our connection
#close connection
conn.close()


root.mainloop()