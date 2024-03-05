import tkinter as tk
from tkinter import ttk, END


def convert(cb1, e1):
    try:
        if cb1 == "cm":
            cm = float(e1)
            inch = cm / 2.54
            mm = cm * 10
            m = cm / 100
            ft = inch / 12
            mi = ft / 5280

            lb1.insert(0, inch)
            lb1.insert(1, m)
            lb1.insert(2, cm)
            lb1.insert(3, mm)
            lb1.insert(4, inch)
            lb1.insert(5, ft)
            lb1.insert(6, mi)

            lb2.insert(0, "inch")
            lb2.insert(1, "m")
            lb2.insert(2, "cm")
            lb2.insert(3, "mm")
            lb2.insert(4, "inch")
            lb2.insert(5, "ft")
            lb2.insert(6, "mi")
        if cb1 == "inch":
            inch = float(e1)
            cm = 1 / 2.54
            mm = cm * 10
            m = cm / 100
            ft = inch / 12
            mi = ft / 5280

            lb1.insert(0, inch)
            lb1.insert(1, m)
            lb1.insert(2, cm)
            lb1.insert(3, mm)
            lb1.insert(4, inch)
            lb1.insert(5, ft)
            lb1.insert(6, mi)

            lb2.insert(0, "inch")
            lb2.insert(1, "m")
            lb2.insert(2, "cm")
            lb2.insert(3, "mm")
            lb2.insert(4, "inch")
            lb2.insert(5, "ft")
            lb2.insert(6, "mi")
        if cb1 == "m":
            m = float(e1)
            ft = m * 3.28084
            inch = 1 / 12 * ft
            cm = m / 100
            mm = cm * 10
            m = cm / 100
            yd = 1.09 * M
            mi = ft / 5280

            lb1.insert(0, m)
            lb1.insert(1, inch)
            lb1.insert(2, cm)
            lb1.insert(3, mm)
            lb1.insert(4, yd)
            lb1.insert(5, ft)
            lb1.insert(6, mi)

            lb2.insert(0, "m")
            lb2.insert(1, "inch")
            lb2.insert(2, "cm")
            lb2.insert(3, "mm")
            lb2.insert(4, "yd")
            lb2.insert(5, "ft")
            lb2.insert(6, "mi")
        if cb1 == "ft":
            ft = float(e1)
            inch = ft * 12
            cm = inch * 2.54
            mm = cm * 10
            m = cm / 100
            ft = inch / 12
            mi = ft / 5280

            lb1.insert(0, inch)
            lb1.insert(1, m)
            lb1.insert(2, cm)
            lb1.insert(3, mm)
            lb1.insert(4, inch)
            lb1.insert(5, ft)
            lb1.insert(6, mi)

            lb2.insert(0, "inch")
            lb2.insert(1, "m")
            lb2.insert(2, "cm")
            lb2.insert(3, "mm")
            lb2.insert(4, "inch")
            lb2.insert(5, "ft")
            lb2.insert(6, "mi")

        if cb1 == "km":
            km = float(e1)
            mi = 0.6213712 * km
            ft = mi * 5280
            inch = ft * 12
            cm = inch * 2.54
            mm = cm * 10
            m = cm / 100
            yd = ft / 3

            lb1.insert(0, km)
            lb1.insert(1, mi)
            lb1.insert(2, ft)
            lb1.insert(3, inch)
            lb1.insert(4, cm)
            lb1.insert(5, mm)
            lb1.insert(6, yd)
            lb1.insert(7, m)

            lb2.insert(0, "km")
            lb2.insert(1, "mi")
            lb2.insert(2, "ft")
            lb2.insert(3, "inch")
            lb2.insert(4, "cm")
            lb2.insert(5, "mm")
            lb2.insert(6, "yd")
            lb2.insert(7, "m")

        tk.Label(root, text="inches").grid(row=2, column=2)
    except ValueError:
        pass


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    lb1.delete(0, END)
    lb2.delete(0, END)


root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x350")

from_units = ["km", "cm", "m", "mm", "inch", "ft", "mi"]
to_units = ["km", "cm", "m", "km", "inch", "ft", "mi"]

tk.Label(root, text="-").grid(row=0, column=0)
tk.Label(root, text="_").grid(row=1, column=0)
tk.Label(root, text="_").grid(row=2, column=0)
tk.Label(root, text="_").grid(row=3, column=0)

e1 = tk.Entry(root, bd=5, bg="seashell")
e1.grid(row=0, column=0)

cb1 = ttk.Combobox(root, values=from_units)
cb1.grid(row=0, column=1)

cb2 = ttk.Combobox(root, values=to_units)
cb2.grid(row=2, column=2)

lb1 = tk.Listbox(root, width=30)
lb1.grid(row=5, column=0)

lb2 = tk.Listbox(root, width=30)
lb2.grid(row=5, column=1)

e2 = tk.Entry(root, bd=5, bg="seashell")
e2.grid(row=2, column=1)

e3 = tk.Entry(root, bd=5, bg="seashell")
e3.grid(row=3, column=1)

btn1 = tk.Button(
    root,
    text="Calculate",
    bd=5,
    bg="light green",
    command=lambda: convert(cb1.get(), e1.get()),
)
btn1.grid(row=4, column=0)

btn2 = tk.Button(root, text="Clear", bd=5, bg="light blue", command=clear)
btn2.grid(row=4, column=1)

root.mainloop()
