from tkinter import *
#to create scrollbars we need a frame

def select():
    l.configure(text=my_list_box.get(ANCHOR))
    l.update()
    #to access the element
    #listbox.get(anchor)


def deletesel():
    #the list number gets changes
    for i in reversed(my_list_box.curselection()):
        my_list_box.delete(i)
        l.config(text='')

def deleteall():
    my_list_box.delete(0,END)


def delete():
    my_list_box.delete(ANCHOR)#here anchor means the selectetd one

def selectall():
    print(my_list_box.curselection())#this functions returns the index number of the list box selected

    result=''
    for item in my_list_box.curselection():
        result=result+str(my_list_box.get(item))+'\n'

    print(result)
    l.configure(text=result)
    l.update()


root=Tk()
root.geometry('300x300')
list_frame=Frame(root)

my_scrollbar=Scrollbar(list_frame,orient=VERTICAL)


#list box
#SINGLE,MULTIPLE,BROWSE,EXTENDED
my_list_box=Listbox(list_frame,fg='green',bd=3,yscrollcommand=my_scrollbar.set,selectmode=MULTIPLE)


'''
selectmode extended
In this to select continuesly use shift and select
To select uniqly use control 

'''


#confiure scroll bar
my_scrollbar.config(command=my_list_box.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

list_frame.pack()#fill=BOTH,expand=1)
my_list_box.pack(pady=15)

#add item to list box
my_list_box.insert(0,"HI this is an item no  1")
my_list_box.insert(END,"s an item no 2")
my_list_box.insert(END,"s an item no End")

#add list of items
lst=["one","two",'three','four','dfjg','dfgjofg','pfgifdjg','pfdjgkm','dfhgofkj0','fihgpifgkij','difjgfijpg','igidmfjgi']

for e in lst:
    my_list_box.insert(END,e)

mybtn=Button(root,text="delete",command=delete)
mybtn.pack()

mybtn2=Button(root,text="select",command=select)
mybtn2.pack()
global l
l=Label(root,text='')
l.pack()

mybtn3=Button(root,text="delete all",command=deleteall)
mybtn3.pack()


mybtn4=Button(root,text="select  all",command=selectall)
mybtn4.pack()

mybtn5=Button(root,text="delete selected",command=deletesel)
mybtn5.pack()

root.mainloop()