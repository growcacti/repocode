from tkinter import *

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

Var1 = IntVar()
Var2 = IntVar()

ChkBttn = Checkbutton(frame, width=15, variable=Var1)
ChkBttn.pack(padx=5, pady=5)

ChkBttn2 = Checkbutton(frame, width=15, variable=Var2)
ChkBttn2.pack(padx=5, pady=5)
