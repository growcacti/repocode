import tkinter as tk
from tkinter import ttk
import glob
import os
from PIL import *


root = tk.Tk()

root.geometry("4+00x800")


canvas = tk.Canvas(root, height=800, width=100, background="lavender")
canvas.grid(row=0, column=2, rowspan=10)


ee1 = ttk.Combobox(canvas, values=["value1", "value2", "values3"])
ee1.grid(row=1, column=2, padx=20, sticky="w")


sp4 = tk.Spinbox(canvas, from_=0, to=100, increment=1)
sp4.grid(row=2, column=2)

btn30 = tk.Button(
    canvas,
    text="Widget type",
    bd=10,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
)
btn30.grid(row=3, column=2)
btn31 = tk.Button(
    canvas, text="Tag widget", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn31.grid(row=4, column=2)
btn32 = tk.Button(
    canvas,
    text="Build Widget",
    bd=10,
    bg="lavender",
    font=("URW Chancery L", 12, "bold"),
)
btn32.grid(row=5, column=2)
btn33 = tk.Button(
    canvas, text="bg color", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn33.grid(row=6, column=2)
btn34 = tk.Button(
    canvas, text="fg color", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn34.grid(row=7, column=2)
btn35 = tk.Button(
    canvas, text="row column", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn35.grid(row=9, column=2)


root.mainlopp()
