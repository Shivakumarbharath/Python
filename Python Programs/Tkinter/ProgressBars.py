from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
root=Tk()
msg=messagebox.showinfo('save changes')
def start():
    prog['value']+=20

def diff():
    for i in range(20):
        prog['value']+=10
        root.update_idletasks()#to view all the tasks happening
        time.sleep(0.1)

def stop():
    prog.stop()

prog=ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
#mode=determinte or indeterminate
prog.pack(pady=20,padx=20)
#prog.start(20) -continuesly

prog_button1=Button(root,text='start',command=start)
prog_button1.pack(padx=15,pady=15)
#prog.stop()-to stop

prog_button2=Button(root,text='stop',command=stop)
prog_button2.pack(padx=15,pady=15)

prog_button3=Button(root,text='task',command=diff)
prog_button3.pack(padx=15,pady=15)

root.mainloop()