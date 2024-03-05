import tkinter as tk
from tkinter import ttk
import glob
import os
from PIL import *


root = tk.Tk()

root.geometry("1700x800")


canvas = tk.Canvas(root, height=800, width=1600, background="lavender")
canvas.grid(row=2, column=2)


ee1 = ttk.Combobox(canvas, values=["value1", "value2", "values3"])
ee1.grid(row=2, column=6, padx=20, sticky="w")


sp4 = tk.Spinbox(canvas, from_=0, to=100, increment=1)
sp4.grid(row=2, column=7)

btn30 = tk.Button(
    canvas,
    text="Widget type",
    bd=10,
    bg="light blue",
    font=("URW Chancery L", 12, "bold"),
)
btn30.grid(row=2, column=0)
btn31 = tk.Button(
    canvas, text="Tag widget", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn31.grid(row=2, column=1)
btn32 = tk.Button(
    canvas,
    text="Build Widget",
    bd=10,
    bg="lavender",
    font=("URW Chancery L", 12, "bold"),
)
btn32.grid(row=2, column=2)
btn33 = tk.Button(
    canvas, text="bg color", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn33.grid(row=2, column=3)
btn34 = tk.Button(
    canvas, text="fg color", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn34.grid(row=2, column=4)
btn35 = tk.Button(
    canvas, text="row column", bd=10, bg="lavender", font=("URW Chancery L", 12, "bold")
)
btn35.grid(row=2, column=5)


root.mainlopp()
