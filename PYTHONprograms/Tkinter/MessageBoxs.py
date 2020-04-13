from tkinter import *
from tkinter import messagebox
'''
Types of Messages
    messagebox.showinfo()
    messagebox.showerror()
    messagebox.showwarning()
    messagebox.askokcancel()
    messagebox.askquestion()
    messagebox.askyesno()
    messagebox.askyesnocancel()
    
In paraenthesis (Tiltle,message)



'''
def poppup():
    response=messagebox.askyesno("Ragini Dilogue","Naa Oru Thadave Sonna Noor thadave Sonna Maari\nHAHAHA")
    #you can check the response bry printing he response on the window then use the returned value
    if response==1:
        Label(root, text="You like it").pack()
    else:
        Label(root,text="You dont like it \nNoo problem ").pack()

root=Tk()

mybtn=Button(root,text="Popup",command=poppup)
mybtn.pack()

root.mainloop()