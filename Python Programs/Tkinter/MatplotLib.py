from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.geometry("400x200")


def graph():
    house_price = np.random.normal(20000, 250000, 500)
    plt.hist(house_price, 50)
    plt.show()


mu_btn = Button(root, text="graph", command=graph)
mu_btn.pack()

root.mainloop()
