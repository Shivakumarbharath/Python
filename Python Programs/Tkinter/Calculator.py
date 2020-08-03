from tkinter import *


def Buton_click(num):
    current = e.get()
    e.delete(0, END)  # from 0th column to end
    e.insert(0, str(current) + str(num))  # insert the number at 0thcolumn
    return


def button_bs():
    e.delete(0)  # delete the number at 0thcolumn
    return


def button_clr():
    e.delete(0, END)  # delete the number at 0thcolumn
    return


def sub():
    first_num = int(e.get())
    global f_num
    f_num = [first_num, '-']
    e.delete(0, END)
    return f_num


def mul():
    first_num = int(e.get())
    global f_num
    f_num = [first_num, 'x']
    e.delete(0, END)
    return f_num


def div():
    first_num = int(e.get())
    global f_num
    f_num = [first_num, '/']
    e.delete(0, END)
    return f_num


def add():
    first_num = int(e.get())
    global f_num
    f_num = [first_num, '+']
    e.delete(0, END)
    return f_num


def eq():
    sec_num = int(e.get())
    e.delete(0, END)
    if f_num[1] is '+':
        e.insert(0, f_num[0] + sec_num)

    if f_num[1] is 'x':
        e.insert(0, f_num[0] * sec_num)

    if f_num[1] is '/':
        e.insert(0, int(f_num[0] / sec_num))

    if f_num[1] is '-':
        e.insert(0, f_num[0] - sec_num)

    return


x = 20
y = 5

root = Tk()

root.title('Simple Calc')
root.iconbitmap('E:\Bharath\Python\PYTHONprograms\Tkinter\Calculator.ico')

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# columnspan=3  since we need to divide the window after this into 3 columns
# IN this case padx and pady are used to give some space around the entryfield


Button_1 = Button(root, text='1', padx=x, pady=y, command=lambda: Buton_click(1))
Button_2 = Button(root, text='2', padx=x, pady=y, command=lambda: Buton_click(2))
Button_3 = Button(root, text='3', padx=x, pady=y, command=lambda: Buton_click(3))
Button_4 = Button(root, text='4', padx=x, pady=y, command=lambda: Buton_click(4))
Button_5 = Button(root, text='5', padx=x, pady=y, command=lambda: Buton_click(5))
Button_6 = Button(root, text='6', padx=x, pady=y, command=lambda: Buton_click(6))
Button_7 = Button(root, text='7', padx=x, pady=y, command=lambda: Buton_click(7))
Button_8 = Button(root, text='8', padx=x, pady=y, command=lambda: Buton_click(8))
Button_9 = Button(root, text='9', padx=x, pady=y, command=lambda: Buton_click(9))
Button_0 = Button(root, text='0', padx=x, pady=y, command=lambda: Buton_click(0))

Button_ad = Button(root, text='+', padx=x, pady=y, command=add)

Button_sub = Button(root, text='-', padx=x, pady=y, command=sub)

Button_mul = Button(root, text='x', padx=x, pady=y, command=mul)

Button_div = Button(root, text='/', padx=x, pady=y, command=div)

Button_eq = Button(root, text='=', padx=34, pady=y, command=eq)

Button_bs = Button(root, text='backspace', padx=9, pady=y, command=button_bs)

Button_clr = Button(root, text='clear', padx=48, pady=y, command=button_clr)

# put the buttons onthe screen

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)

Button_ad.grid(row=4, column=1)
Button_mul.grid(row=4, column=2)
Button_sub.grid(row=5, column=0)
Button_div.grid(row=6, column=0)

Button_bs.grid(row=5, column=1, columnspan=2)
Button_eq.grid(row=6, column=1, columnspan=2)
Button_clr.grid(row=7, column=0, columnspan=3)

root.mainloop()
