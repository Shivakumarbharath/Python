import xlsxwriter as xl
import xlsxwriter.exceptions
from tkinter import *
from tkinter import ttk

# pyinstaller -h -F filename
# this creates .exe file without any extra window
workbook = xl.Workbook("Entries.xlsx")

# create a sheet
sheet1 = workbook.add_worksheet("Brand")

root = Tk()
root.title("Data Entry")
root.geometry("500x370")

xLab = 0.05
xEnt = 0.13
w = 70
num = 5


def Enter():
    global num
    title = titleE.get()
    type1 = typeE.get()
    link = linkE.get()
    price = int(mrpE.get())

    titleE.delete(0, END)
    linkE.delete(0, END)
    mrpE.delete(0, END)

    y = title.split(' ')
    brand = y[0]
    l = title.split(" L ")
    liters = int(l[0][-3:])
    st = title.split(" Star ")
    stars = st[0][-1]
    m = title.split(' (')
    det = m[-1].split(', ')
    model = det[-1][:-1]
    colour = det[0]
    attributes = "Capacity:{} Liters;Type:{};Colour:{};Stars:{} Stars".format(liters, type1, colour, stars)
    print(title)
    print(attributes)
    print(model)
    send = [title, attributes, link, price, model, brand]
    column = ["A", "B", "C", "D", "E", 'F']

    for a, b in zip(send, column):
        sheet1.write(b + str(num), a)
    num = num + 1
    print(num)

    text = 'Last Entry'
    for i, e in enumerate(send):
        if i != 2:
            text = text + '\n' + str(e)

    show = Label(root, text=text)
    show.place(relx=0, rely=0.7)


def Save():
    while True:
        try:
            workbook.close()
        except xl.exceptions.FileCreateError as e:
            # For Python 3 use input() instead of raw_input().
            decision = input("Exception caught in workbook.close(): %s\n"
                             "Please close the file if it is open in Excel.\n"
                             "Try to write file again? [Y/n]: " % e)
            if decision != 'n':
                continue

        break

    root.quit()


# Labels and Entries
MainLabel = Label(root, text="Entry Form", relief="solid", font=("ariel", 20, "bold"))
MainLabel.place(relx=0.3, rely=0.04)

title_Label = Label(root, text="Title :")
title_Label.place(relx=xLab, rely=0.2)

titleE = Entry(root, width=w)
titleE.place(relx=xEnt, rely=0.2)

type_Label = Label(root, text="Type :")
type_Label.place(relx=xLab, rely=0.3)

typeE = ttk.Combobox(root, value=["Top Freezer Refrigerator", "Top Mount", "Top Freezer", "Side-by-Side Refrigerator",
                                  "French Door Refrigerator", "Bottom Mount"], width=67)
typeE.place(relx=xEnt, rely=0.3)

link_Label = Label(root, text="Link :")
link_Label.place(relx=xLab, rely=0.4)

linkE = Entry(root, width=w)
linkE.place(relx=xEnt, rely=0.4)

mrp_Label = Label(root, text="MRP :")
mrp_Label.place(relx=xLab, rely=0.5)

mrpE = Entry(root, width=w)
mrpE.place(relx=xEnt, rely=0.5)

# Buttons
enter = Button(root, text="Enter", command=Enter)
enter.place(relx=0.3, rely=0.6)

save = Button(root, text="Save", command=Save)
save.place(relx=0.5, rely=0.6)

root.mainloop()
