import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *

root = tk.Tk()
root.geometry("400x250")
root.title("Unit Conversion")

length_options = ["m", "cm", "mm", "in", "ft", "yd", "mi"]
liquid_options = ["ml", "loz", "gal", "pint", "quart"]

l1 = tk.Label(root, text="Length", font=("Arial", 14))
l1.grid(row=0, column=0)
l = tk.Entry(root, bg="yellow", font=("Arial", 14))
l.grid(row=1, column=0)

n2 = ttk.Combobox(root, values=length_options, font=("Arial", 14))
n2.set("m")
n2.grid(row=1, column=1)

c1 = tk.Label(root, text="Liquid", font=("Arial", 14))
c1.grid(row=2, column=0)
c = tk.Entry(root, bg="light blue", font=("Arial", 14))
c.grid(row=3, column=0)

n = ttk.Combobox(root, values=liquid_options, font=("Arial", 14))
n.set("ml")
n.grid(row=3, column=1)


def clear_entries():
    l.delete(0, END)
    c.delete(0, END)
    lb5.delete(0, END)
    lb6.delete(0, END)


def convert_units():
    length = float(l.get())
    length_unit = n2.get()
    liquid = float(c.get())
    liquid_unit = n.get()

    length_conversion = {
        "m": length,
        "cm": length * 100,
        "mm": length * 1000,
        "in": length * 39.37,
        "ft": length * 3.281,
        "yd": length * 1.094,
        "mi": length * 0.0006214,
    }

    liquid_conversion = {
        "ml": liquid,
        "loz": liquid * 0.03381,
        "gal": liquid * 0.0002642,
        "pint": liquid * 0.002113,
        "quart": liquid * 0.001057,
    }

    converted_length = length_conversion[length_unit]
    converted_liquid = liquid_conversion[liquid_unit]

    lb5.insert(1, f"{converted_length:.4f} {length_unit}")
    lb5.insert(2, f"{converted_liquid:.4f} {liquid_unit}")


lb5 = tk.Listbox(root, width=30)
lb5.grid(row=5, column=0, columnspan=2)
lb6 = tk.Listbox(root, width=30)
lb6.grid(row=5, column=4, columnspan=2)

convert_btn = tk.Button(
    root, text="Convert", bg="orange", font=("Arial Black", 12), command=convert_units
)
convert_btn.grid(row=4, column=1)

clr_btn = tk.Button(
    root, text="Clear", bg="orange", font=("Arial Black", 12), command=clear_entries
)
clr_btn.grid(row=4, column=0)

root.mainloop()
