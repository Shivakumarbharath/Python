from tkinter import *

root = Tk()

E = Entry(root, width=50, font=('ariel', 6))
E.pack(padx=5, pady=5)

'''
def delete():
    l.pack_forget()
    btn['state'] = 'active'
    print(l.winfo_exists())
   '''


def Click():
    global l

    if l.winfo_exists() == 1:
        l.destroy()
    hello = 'Hello  ' + E.get()
    E.delete(0, END)
    l = Label(root, text=hello)
    l.pack()
    # btn['state']=DISABLED


btn = Button(root, text="Name", command=Click)
btn.pack()
l = Label(root, text='')
l.pack()

# delbtn=Button(root,text="Delete",command=delete)
# delbtn.pack()

root.mainloop()
