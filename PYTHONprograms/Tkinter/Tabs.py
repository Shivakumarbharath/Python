from tkinter import *
from tkinter import ttk


'''
To have tabs we need notebook 
so we import ttk

'''

def Hide():
    #here the notebook tabs are indexed same as the list
    my_notebook.hide(1)

def Get():
    my_notebook.add(frame2,text="red tab")


def Select():
    my_notebook.select(1)

root=Tk()
root.geometry('300x300')

#create notebook
my_notebook=ttk.Notebook(root)
my_notebook.pack()

#create frames to insert into the notebook
frame1=Frame(my_notebook,width=300,height=300,bg='blue')
frame2=Frame(my_notebook,width=300,height=300,bg='red')


frame1.pack(fill=BOTH,expand=1)
frame2.pack(fill=BOTH,expand=1)

#we need to designate the actual tabs themselves

my_notebook.add(frame1,text="blue tab")
my_notebook.add(frame2,text="red tab")



#create buttons in the tab
#Hide a tab
btn=Button(frame1,text="Hide Tab 2",command=Hide)
btn.pack()

#show a tab
btn=Button(frame1,text="Get Tab 2",command=Get)
btn.pack()

#access the tabs
#navigate the tab
btn=Button(frame1,text="navigtae to  Tab 2",command=Select)
btn.pack()


root.mainloop()