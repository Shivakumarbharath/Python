import tkinter as tk

i = 0
def text_mod():
    global i, btn           # btn can be omitted but not sure if should be
    txt = ("Vicariously", "I", "live", "as", "the", "whole", "world", "dies")
    btn['text'] = txt[i]    # the global object that is modified
    i = (i + 1) % len(txt)  # another global object that gets modified

root = tk.Tk()

btn = tk.Button(root, text="My Button")
btn['command'] = text_mod

btn.pack(fill='both', expand=True)

root.mainloop()