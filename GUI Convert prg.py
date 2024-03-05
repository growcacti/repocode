import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import math

r = tk.Tk()
r.geometry("1200x800")
r.title("APPS")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=0)
f0 = ttk.Frame(notebook)
notebook.add(f0, text="MAIN")
f1 = ttk.Frame(notebook)
f2 = ttk.Frame(notebook)
notebook.add(f1, text="1")
notebook.add(f2, text="2")

f3 = ttk.Frame(notebook)
notebook.add(f3, text="3")
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text="4")
f5 = ttk.Frame(notebook)
notebook.add(f5, text=" 5 ")
f6 = ttk.Frame(notebook)
notebook.add(f6, text="6")
f7 = ttk.Frame(notebook)
notebook.add(f7, text="7")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f9 = ttk.Frame(notebook)
notebook.add(f9, text="9")
f10 = ttk.Frame(notebook)
notebook.add(f10, text="10")


def c():

    pass


num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
tk.Label(f1, text="").grid(row=0, column=0)
tk.Label(f1, text="").grid(row=1, column=0)
tk.Label(f1, text="").grid(row=2, column=0)
tk.Label(f1, text="").grid(row=3, column=0)

tk.Entry(f1, textvariable=num1).grid(row=0, column=1)
tk.Entry(f1, textvariable=num2).grid(row=1, column=1)
tk.Entry(f1, textvariable=num3).grid(row=2, column=1)
tk.Entry(f1, textvariable=num4).grid(row=3, column=1)
lb1 = tk.Listbox(f1)
lb1.grid(row=6, column=1)


btn1 = tk.Button(f1, text="Calculate", command=c)
btn1.grid(row=4, column=1)


btn2 = tk.Button(f1, text="Send txt", command=c)
btn2.grid(row=5, column=1)


num5 = tk.StringVar()
num6 = tk.StringVar()
num7 = tk.StringVar()
num8 = tk.StringVar()
tk.Label(f2, text=" ").grid(row=0, column=0)
tk.Label(f2, text="").grid(row=1, column=0)
tk.Label(f2, text="").grid(row=2, column=0)
tk.Label(f2, text="").grid(row=3, column=0)

tk.Entry(f2, textvariable=num5).grid(row=0, column=1)
tk.Entry(f2, textvariable=num6).grid(row=1, column=1)
tk.Entry(f2, textvariable=num7).grid(row=2, column=1)
tk.Entry(f2, textvariable=num8).grid(row=3, column=1)
lb2 = tk.Listbox(f2)
lb2.grid(row=6, column=1)


def show2(*args):
    a = num5.get()
    b = num6.get()
    c = num7.get()
    d = num8.get()


btn4 = tk.Button(f2, text="Calculate", command=c)
btn4.grid(row=4, column=1)


btn6 = tk.Button(f2, text="Send txt", command=c)
btn6.grid(row=5, column=1)


num11 = tk.StringVar()
num22 = tk.StringVar()
num33 = tk.StringVar()
nume44 = tk.StringVar()
tk.Label(f3, text="").grid(row=0, column=0)
tk.Label(f3, text="").grid(row=1, column=0)
tk.Label(f3, text="").grid(row=2, column=0)
tk.Label(f3, text="").grid(row=3, column=0)

tk.Entry(f3, textvariable=num11).grid(row=0, column=1)
tk.Entry(f3, textvariable=num22).grid(row=1, column=1)
tk.Entry(f3, textvariable=num33).grid(row=2, column=1)
tk.Entry(f3, textvariable=nume44).grid(row=3, column=1)
text = tk.Text(f3, width=300, height=200)
text.grid(row=6, column=1)


btn22 = tk.Button(f3, text="Calculate", command=c)
btn22.grid(row=4, column=1)


btn33 = tk.Button(f3, text="Send txt", command=c)
btn33.grid(row=5, column=1)

num222 = tk.StringVar()
num333 = tk.StringVar()
num444 = tk.StringVar()
numout33 = tk.StringVar()
numout44 = tk.StringVar()
vvv1 = tk.StringVar()
vdiv1 = tk.StringVar()
tk.Label(f5, text=" ").grid(row=0, column=0)
tk.Label(f5, text="   ").grid(row=1, column=0)
tk.Label(f5, text="  ").grid(row=2, column=0)
tk.Entry(f5, textvariable=num111, bg="yellow").grid(row=0, column=1)
tk.Entry(f5, textvariable=num222, bg="yellow").grid(row=1, column=1)

tk.Entry(f5, textvariable=vvv1, bg="yellow").grid(row=2, column=1)
lb7 = tk.Listbox(f5, height=20)
lb7.grid(row=6, column=2)
lb9 = tk.Listbox(f5, height=20)
lb9.grid(row=6, column=1)
b1 = tk.Button(f5, text="Calculate", command=c)
b1.grid(row=6, column=0)
b3 = tk.Button(f5, text="Clear", command=c)
b3.grid(row=7, column=0)
num1234 = tk.StringVar()
num4567 = tk.StringVar()
num7891 = tk.StringVar()
num1112 = tk.StringVar()
vvv2 = tk.StringVar()
num9999 = tk.StringVar()
num8888 = tk.StringVar()
num7777 = tk.StringVar()
num6666 = tk.StringVar()

vdiv2 = tk.StringVar()
tk.Label(f5, text="  ").grid(row=0, column=4)
tk.Label(f5, text=" ").grid(row=1, column=4)
tk.Label(f5, text=" ").grid(row=2, column=4)
tk.Label(f5, text=" ").grid(row=3, column=4)
tk.Label(f5, text=" ").grid(row=4, column=4)
tk.Entry(f5, textvariable=num1234, bg="yellow").grid(row=0, column=5)
tk.Entry(f5, textvariable=num4567, bg="yellow").grid(row=1, column=5)
tk.Entry(f5, textvariable=num7891, bg="yellow").grid(row=2, column=5)
tk.Entry(f5, textvariable=num1112, bg="yellow").grid(row=3, column=5)
tk.Entry(f5, textvariable=vvv2, bg="yellow").grid(row=4, column=5)

b2 = tk.Button(f5, text="   ", command=c)
b2.grid(row=6, column=5)
b4 = tk.Button(f5, text="Clear", command=c)
b4.grid(row=7, column=5)


if __name__ == "__main__":
    r.mainloop()
