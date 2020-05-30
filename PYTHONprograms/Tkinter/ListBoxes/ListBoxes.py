from tkinter import *

root=Tk()
root.geometry('300x300')
#list box
my_list_box=Listbox(root,bg='green',bd=3)
my_list_box.pack(pady=15)

#add item to list box
my_list_box.insert(0,"HI this is an item no  1")
my_list_box.insert(2,"s an item no 2")
my_list_box.insert(END,"s an item no End")

#add list of items
lst=["one","two",'three','four']

for e in lst:
    my_list_box.insert(END,e)


def delete():
    my_list_box.delete(ANCHOR)#here anchor means the selectetd one

mybtn=Button(root,text="delete",command=delete)
mybtn.pack()

def select():
    l.configure(text=my_list_box.get(ANCHOR))
    l.update()
    #to access the element
    #listbox.get(anchor)

mybtn2=Button(root,text="select",command=select)
mybtn2.pack()

l=Label(root,text='')
l.pack()

root.mainloop()