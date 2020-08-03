'''

Using a Canvas for scrolling
What we'll be doing is creating a Canvas, and inside it creating a window.

The window can have as much content as we like, but it's the Canvas that we'll be placing inside our application.

That means that we'll be able to set the Canvas size to whatever we want, and then when we scroll we'll be moving along the window inside it.

In order to do so, we must also specify what the scrollable area will be. Often, the scrollable area matches the contents of the inner window—but it can also be different if we wish.

Let's start off by creating all the widgets we'll need. Those are:

An application window (a tk.Tk object)
A container frame for our canvas and scrollbar
The canvas
The scrollbar
A frame that will become the scrollable frame
Almost all these widgets will work like normal Tkinter widgets (i.e. you place them in their container and then use Pack or Grid). However, the scrollable frame will behave differently. We will create it, giving it the canvas as its container, but instead of using Pack or Grid, we will using the canvas' create_window method to create a window within the canvas that shows the scrollable frame's content.

Creating the widgets is straightforward enough:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
Now let's add some code that will call a function whenever the contents of the scrollable frame change. This is necessary because we must tell the canvas how large the frame will be, so that it knows how much it can scroll:

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
The <Configure> event we're binding here triggers whenever the scrollable_frame changes size—i.e. usually when we add or remove widgets from within it.

Only when it changes size do we want to change any of the scrolling properties.

The change is we modify the canvas' scrollregion to have a size of canvas.bbox("all").

Calling canvas.bbox("all") gives us a 4-value tuple describing the position of two corners of a rectangle which is the scroll region.

Next up we have to tell the canvas to actually draw the scrollable_frame inside itself:

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
The values (0, 0) tell the canvas on which position to draw the window. The argument anchor="nw" tells the canvas to place the frame's top left corner on position (0, 0).

Finally, we have to configure the canvas so that when its y-position changes, the scrollbar moves:

canvas.configure(yscrollcommand=scrollbar.set)
Once you've done this, you can add elements to the scrollable_frame, and it'll work as you'd expect!

Also, don't forget to use Pack or Grid to add the container, canvas, and scrollbar to the application window.

The final code might look something like this:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
A reusable ScrollableFrame class
To make creating scrollable frames a bit easier, you might be tempted to code up an easy to use class.

We've done it for you, so you don't have to!

Here's a ScrollableFrame class that you can just use as a normal frame!

import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
If you wanted to use this class, remember to place things inside self.scrollable_frame, and not directly into an object of this class:

root = tk.Tk()

frame = ScrollableFrame(root)

for i in range(50):
    ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

frame.pack()
root.mainloop()

'''