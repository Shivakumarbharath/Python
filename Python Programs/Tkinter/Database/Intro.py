from tkinter import *
import sqlite3

root=Tk()
root.title("My Address Book")
root.geometry("600x600")


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
    frame = LabelFrame(root, text='', padx=5, pady=5, font=('times ', 10, 'bold'))
    frame.place(x=400, y=100, anchor=W)
    frame.place_forget()
    frame=LabelFrame(root,text='Success',padx=5,pady=5,font=('times ',10,'bold'))
    frame.place(x=400,y=100,anchor=W)
    l=Label(frame,text="Address Added")
    l.pack()
    Fe.delete(0,END)
    Le.delete(0,END)
    addE.delete(0, END)
    cityE.delete(0, END)
    stateE.delete(0, END)
    zipE.delete(0, END)
    return


#create query function
def query():
    global frame
    frame=LabelFrame(root,text='Records Present',padx=5,pady=5,font=('times ',10,'bold'))
    frame.place(x=370,y=100,anchor=W)
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    record=c.fetchall()
    print(record)
    text=''
    for rec in record:
        text+=str(rec[0])+' ' +str(rec[1])+' \t UID-'+ str(rec[6])+' \n'
    l = Label(frame, text=text)
    l.pack()

    conn.commit()
    conn.close()


#delete record
def delete_a_record():
    global delbtn, ue,ULabel,btn
    def delb(uid):

        conn=sqlite3.connect("address_book.db")
        c=conn.cursor()
        c.execute("DELETE FROM addresses WHERE oid={}".format(uid))
        conn.commit()
        conn.close()
        ue.place_forget()
        ULabel.place_forget()
        btn.place_forget()
        delbtn = Button(root, text=" Delete Record", padx=5, pady=5, relief=RAISED, bg="red",command=delete_a_record)
        delbtn.place(x=350, y=500)

    delbtn.place_forget()
    delbtn = Button(root, text=" Delete Record",padx=5,pady=5, relief=RAISED, bg="red", state=DISABLED,font=('ariel',8))
    delbtn.place(x=240, y=500)
    ULabel = Label(root, text="UID ", padx=10, pady=10, font=('ariel', 14))
    ULabel.place(x=40, y=550)
    ue = Entry(root, width=30, borderwidth=5)
    ue.place(x=130, y=560)
    btn=Button(root,text="Delete",bg='red',height=1,width=5,font=('ariel',7),command=lambda:delb(ue.get()))
    btn.place(x=330,y=560)

#To update a record
def update_a_record():
    global upbtn, ue,ULabel,btn,editor
    def update(uid):
        editor = Toplevel()
        editor.title("Edit Record")
        editor.geometry('450x550')

        # create Entries and labels

        MainLabel = Label(editor, text="Edit", relief="solid", font=("ariel", 20, "bold"),padx=5,pady=5)
        MainLabel.place(x=190, y=20)

        FLabel_editor = Label(editor, text="First Name: ", padx=10, pady=10, font=('ariel', 14))
        FLabel_editor.place(x=40, y=105)

        Fe_editor = Entry(editor, width=30, borderwidth=5)
        Fe_editor.place(x=160, y=115)

        LLabel_editor = Label(editor, text="Last Name: ", padx=10, pady=10, font=('ariel', 14))
        LLabel_editor.place(x=40, y=165)
        Le_editor = Entry(editor, width=30, borderwidth=5)
        Le_editor.place(x=160, y=175)

        addLabel_editor = Label(editor, text="Address: ", padx=10, pady=10, font=('ariel', 14))
        addLabel_editor.place(x=40, y=225)
        addE_editor = Entry(editor, width=30, borderwidth=5)
        addE_editor.place(x=160, y=235)

        cityLabel_editor = Label(editor, text="City: ", padx=10, pady=10, font=('ariel', 14))
        cityLabel_editor.place(x=40, y=290)
        cityE_editor = Entry(editor, width=30, borderwidth=5)
        cityE_editor.place(x=160, y=300)

        stateLabel_editor = Label(editor, text="State: ", padx=10, pady=10, font=('ariel', 14))
        stateLabel_editor.place(x=40, y=355)
        stateE_editor = Entry(editor, width=30, borderwidth=5)
        stateE_editor.place(x=160, y=365)

        zipLabel_editor = Label(editor, text="Zipcode: ", padx=10, pady=10, font=('ariel', 14))
        zipLabel_editor.place(x=40, y=430)
        zipE_editor = Entry(editor, width=30, borderwidth=5)
        zipE_editor.place(x=160, y=440)


        #get the details
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        record_edit = list(c.execute("SELECT * FROM addresses WHERE oid={}".format(uid)).fetchall()[0])
        print(record_edit)

        #insert them in fields
        Fe_editor.insert(0,record_edit[0])
        Le_editor.insert(0,record_edit[1])
        addE_editor.insert(0,record_edit[2])
        cityE_editor.insert(0,record_edit[3])
        stateE_editor.insert(0,record_edit[4])
        zipE_editor.insert(0,record_edit[5])

        # create a save button
        savebtn = Button(editor, text="Save", padx=5, pady=5, relief=RAISED, bg="green", font=('ariel', 8),
                         command=lambda: edit(uid,Fe_editor.get(),Le_editor.get(),addE_editor.get(),cityE_editor.get(),stateE_editor.get(),zipE_editor.get(),editor))
        savebtn.place(x=75, y=500)



        '''
        conn=sqlite3.connect("address_book.db")
        c=conn.cursor()
        c.execute("DELETE FROM addresses WHERE oid={}".format(uid))
        conn.commit()
        conn.close()
        ue.place_forget()
        ULabel.place_forget()
        btn.place_forget()
        upbtn = Button(root, text=" Delete Record", padx=5, pady=5, relief=RAISED, bg="green",command=update_a_record)
        upbtn.place(x=350, y=500)
'''


    def edit(uid,fn,ln,add,city,state,zip,editor):
        global frame
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        record_edit=list(c.execute("SELECT * FROM addresses WHERE oid={}".format(uid)).fetchall()[0])
        print(record_edit)
        c.execute(""" UPDATE addresses SET 
        First_name = :first,
        Last_name =:last,
        address =:add,
        city =:city,
        state =:state,
        zipcode=:zip WHERE oid =:ooid
        
        
        """.format(uid),{
            'first':fn,
            'last':ln,
            'add':add,
            'city':city,
            'state':state,
            'zip':zip,
            'ooid':uid


        })
        conn.commit()
        conn.close()


        frame.place_forget()

        frame = LabelFrame(root, text='Edit Status', padx=5, pady=5, font=('times ', 10, 'bold'))
        frame.place(x=400, y=100, anchor=W)
        l = Label(frame, text='Edited Succesfully')
        l.pack()

        ue.place_forget()
        ULabel.place_forget()
        btn.place_forget()
        upbtn = Button(root, text=" Update Record", padx=5, pady=5, relief=RAISED, bg="green", command=update_a_record)
        upbtn.place(x=340, y=500)
        editor.destroy()

    upbtn.place_forget()
    upbtn = Button(root, text=" Update Record",padx=5,pady=5, relief=RAISED, bg="green", state=DISABLED,font=('ariel',8))
    upbtn.place(x=340, y=500)
    ULabel = Label(root, text="UID ", padx=10, pady=10, font=('ariel', 14))
    ULabel.place(x=40, y=550)
    ue = Entry(root, width=30, borderwidth=5)
    ue.place(x=130, y=560)
    btn=Button(root,text="update",bg='green',height=1,width=5,font=('ariel',7),command=lambda:update(ue.get()))
    btn.place(x=330,y=560)




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
logbtn=Button(root,text="Submit",padx=5,pady=5,relief=RAISED,bg="green",command=submit,font=('ariel',8))
logbtn.place(x=75,y=500)


#query button
qbtn=Button(root,text=" Show Records",padx=5,pady=5,relief=RAISED,bg="blue",command=query,font=('ariel',8))
qbtn.place(x=135,y=500)


#DElete button
delbtn=Button(root,text=" Delete Record",padx=5,pady=5,relief=RAISED,bg="red",command=delete_a_record,font=('ariel',8))
delbtn.place(x=240, y=500)

#Update button
upbtn=Button(root,text=" Update Record",padx=5,pady=5,relief=RAISED,bg="green",command=update_a_record,font=('ariel',8))
upbtn.place(x=340, y=500)


#anytime we make change to the database we need to commit those changes to the database
#to do that
#commit changes
conn.commit()
#finally we close our connection
#close connection
conn.close()


root.mainloop()