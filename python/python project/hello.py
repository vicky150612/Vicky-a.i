from tkinter import *
from tkinter import ttk
import random

root = Tk()
label = Label(root, text="Enter the maximum number and click the button", font="arial")

z = Entry(root, textvariable=IntVar())


def set():
    c = int(z.get())
    r = random.randint(1, c)
    label2 = Label(root, text=r)
    label2.pack()


Button2 = Button(root, text="random", command=set)
label.pack()
z.pack()
Button2.pack()
root.mainloop()
