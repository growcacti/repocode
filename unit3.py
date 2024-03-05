import tkinter as tk
from tkinter import ttk, END

# Conversion factors
CONVERSION_FACTORS = {
    "cm": {"inch": 1 / 2.54, "mm": 10, "m": 0.01, "ft": 1 / 30.48, "mi": 1 / 160934.4},
    "inch": {"cm": 2.54, "mm": 25.4, "m": 0.0254, "ft": 1 / 12, "mi": 1 / 63360},
    "m": {"cm": 100, "inch": 39.37, "mm": 1000, "ft": 3.28084, "mi": 0.000621371},
    "ft": {"cm": 30.48, "inch": 12, "mm": 304.8, "m": 0.3048, "mi": 1 / 5280},
    "km": {
        "mi": 0.621371,
        "ft": 3280.84,
        "inch": 39370.1,
        "cm": 100000,
        "mm": 1000000,
        "m": 1000,
    },
}


def convert(cb1, e1):
    try:
        unit1 = cb1.get()
        unit2 = cb2.get()

        if unit1 in CONVERSION_FACTORS and unit2 in CONVERSION_FACTORS[unit1]:
            factor = CONVERSION_FACTORS[unit1][unit2]
            value = float(e1.get())
            converted_value = value * factor
            lb1.insert(0, converted_value)
            lb2.insert(0, unit2)

    except ValueError:
        pass


def clear():
    e1.delete(0, END)
    lb1.delete(0, END)
    lb2.delete(0, END)


root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x350")

from_units = list(CONVERSION_FACTORS.keys())
to_units = ["inch", "m", "cm", "mm", "ft", "mi"]

# GUI code...

e1 = tk.Entry(root, bd=5, bg="seashell")
e1.grid(row=0, column=0)

cb1 = ttk.Combobox(root, values=from_units)
cb1.grid(row=0, column=1)

cb2 = ttk.Combobox(root, values=to_units)
cb2.grid(row=2, column=1)

lb1 = tk.Listbox(root, width=30)
lb1.grid(row=5, column=0)

lb2 = tk.Listbox(root, width=30)
lb2.grid(row=5, column=1)

btn1 = tk.Button(
    root, text="Calculate", bd=5, bg="light green", command=lambda: convert(cb1, e1)
)
btn1.grid(row=4, column=0)

btn2 = tk.Button(root, text="Clear", bd=5, bg="light blue", command=clear)
btn2.grid(row=4, column=1)

root.mainloop()
