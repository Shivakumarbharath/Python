from tkinter import *


root=Tk()
root.title("Register")
root.geometry("500x600")

MainLabel=Label(root,text="Registration Form",relief="solid",font=("ariel",20,"bold"))
MainLabel.place(x=120,y=20)

FLabel=Label(root,text="First Name: ",padx=10,pady=10,font=('ariel',14))
FLabel.place(x=40,y=105)
fn=StringVar()
Fe=Entry(root,width=30,textvar=fn,borderwidth=5)
Fe.place(x=160,y=115)

LLabel=Label(root,text="Last Name: ",padx=10,pady=10,font=('ariel',14))
LLabel.place(x=40,y=165)
ln=StringVar()
Le=Entry(root,width=30,textvar=ln,borderwidth=5)
Le.place(x=160,y=175)

PLabel=Label(root,text="DOB: ",padx=10,pady=10,font=('ariel',14))
PLabel.place(x=40,y=225)
pwd=StringVar()
Pe=Entry(root,width=30,textvar=pwd,borderwidth=5)
Pe.insert(0,"dd\mm\yyyy")
Pe.place(x=160,y=235)


#combo box is needed for the country
#First Create a list of countries

contries=["India","Afghanistan","USA","Japan","Germany","France"]
#Create a widget of comboBoxes

var=StringVar()
droplist=OptionMenu(root,var,*contries)


var.set("Select Country")
droplist.config(width=30)
droplist.place(x=160,y=295)


CLabel=Label(root,text="Country: ",padx=10,pady=10,font=('ariel',14))
CLabel.place(x=40,y=285)



logbtn=Button(root,text="Sign Up",padx=5,pady=5,relief=RAISED,bg="red")
logbtn.place(x=100,y=350)


qbtn=Button(root,text=" Cancel",padx=5,pady=5,relief=RAISED,bg="red",command=root.quit)
qbtn.place(x=200,y=350)

root.mainloop()