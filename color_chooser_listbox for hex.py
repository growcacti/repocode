#!/usr/bin/env python3


from tkinter import Tk, Frame, Button, BOTH, SUNKEN, Listbox, Label, StringVar
from tkinter import colorchooser


root = Tk()

root.geometry("600x450+300+300")

frame = Frame(root, border=1, relief=SUNKEN, width=350, height=200)


def onChoose():

    (rgb, hx) = colorchooser.askcolor()
    frame.config(bg=hx)

    Label(root, text=rgb).grid(row=0, column=3)
    Label(root, text=hx).grid(row=0, column=4)

    lb1.insert(1, rgb)
    lb2.insert(1, hx)


lb1 = Listbox(root)
lb1.grid(row=3, column=3)
lb2 = Listbox(root)
lb2.grid(row=3, column=4)


btn = Button(root, text="Choose Color", command=onChoose)
btn.grid(row=2, column=2)

if __name__ == "__main__":
    root.mainloop()
