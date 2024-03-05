#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame
from tkinter import *

root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
f1 = ttk.Frame(notebook)
f1.grid(row=0, column=0)

notebook.add(f1, text="1")



sp1 = tk.Spinbox(f1, from_=0.01, to=2000, increment=1)
# To show the content in the window
sp1.grid(row=0, column=0)
sp2 = tk.Spinbox(f1, from_=0.01, to=2000, increment=1)
# To show the content in the window
sp2.grid(row=1, column=0)
sp3 = tk.Spinbox(f1, from_=0.01, to=2000, increment=1)
# To show the content in the window
sp3.grid(row=2, column=0)
sp4 = tk.Spinbox(f1, from_=1, to=2000, increment=1)
# To show the content in the window
sp4.grid(row=3, column=0)
btn = tk.Button(f1,text="enter", command=lambda : checkered(sp1.get().sp2.get()))
btn.grid(row=8,column=0)
f2 = ttk.Frame(notebook)
f2.grid(row=0, column=0)

notebook.add(f2, text="2")


def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


canvas_width = 1800
canvas_height = 900
wow = Canvas(f2, width=canvas_width, height=canvas_height)
wow.grid(row=0, column=0)
wow.create_line(sp1.get(),sp2.get(),sp3.get(), sp4.get(), fill="black", width=4)
wow.create_line(sp1.get(),sp2.get(),sp3.get(), sp4.get(), fill="black", width=4)
