from tkinter import *
from random import randint


def wynik():
    w.config(text=str(v1.get() * v2.get()))
    w.config(font=("Arial", 80), foreground="#" + ("%06x" % randint(0, 16777215)))


o = Tk()
v1 = IntVar()
v2 = IntVar()

for i in range(1, 11):
    Radiobutton(o, text=str(i), variable=v1, value=i, command=wynik).grid(
        row=0, column=i
    )
    Radiobutton(o, text=str(i), variable=v2, value=i, command=wynik).grid(
        row=i, column=0
    )

w = Label(o, text="0")
w.place(x=130, y=80)
w.config(font=("Arial", 80), foreground="magenta")
o.mainloop()
