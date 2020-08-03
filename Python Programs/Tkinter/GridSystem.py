from tkinter import *

'''
grid system are representing interms of rows and columns
'''

root = Tk()

label1 = Label(root, text="Hello World").grid(row=0, column=0)
label2 = Label(root, text="Ketta Paiye saar Ave").grid(row=1, column=5)

# label1.grid(row=0,column=0)
#
# label2.grid(row=1,column=5 )


root.mainloop()
