from tkinter import *
#to create scrollbars we need a frame
root=Tk()
root.geometry('300x300')
list_frame=Frame(root)

my_scrollbar=Scrollbar(list_frame,orient=VERTICAL)


#list box
my_list_box=Listbox(list_frame,fg='green',bd=3,yscrollcommand=my_scrollbar.set)
#confiure scroll bar
my_scrollbar.config(command=my_list_box.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

list_frame.pack()#fill=BOTH,expand=1)
my_list_box.pack(pady=15)

#add item to list box
my_list_box.insert(0,"HI this is an item no  1")
my_list_box.insert(2,"s an item no 2")
my_list_box.insert(END,"s an item no End")

#add list of items
lst=["one","two",'three','four','dfjg','dfgjofg','pfgifdjg','pfdjgkm','dfhgofkj0','fihgpifgkij','difjgfijpg','igidmfjgi']

for e in lst:
    my_list_box.insert(END,e)

def deleteall():
    my_list_box.delete(0,END)


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

mybtn3=Button(root,text="delete all",command=deleteall)
mybtn3.pack()


root.mainloop()