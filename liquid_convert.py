import tkinter as tk
from tkinter import ttk, END

# Conversion factors for liquid volume
LIQUID_CONVERSION_FACTORS = {
    "ml": {
        "liters": 0.001,
        "fl oz": 0.033814,
        "cup": 0.00416667,
        "pint": 0.00211338,
        "quart": 0.00105669,
        "gallon": 0.000264172,
    },
    "liters": {
        "ml": 1000,
        "fl oz": 33.814,
        "cup": 4.16667,
        "pint": 2.11338,
        "quart": 1.05669,
        "gallon": 0.264172,
    },
    "fl oz": {
        "ml": 29.5735,
        "liters": 0.0295735,
        "cup": 0.123223,
        "pint": 0.0625,
        "quart": 0.03125,
        "gallon": 0.0078125,
    },
    "cup": {
        "ml": 240,
        "liters": 0.24,
        "fl oz": 8.11537,
        "pint": 0.50721,
        "quart": 0.253605,
        "gallon": 0.0634013,
    },
    "pint": {
        "ml": 473.176,
        "liters": 0.473176,
        "fl oz": 16,
        "cup": 1.97157,
        "quart": 0.5,
        "gallon": 0.125,
    },
    "quart": {
        "ml": 946.353,
        "liters": 0.946353,
        "fl oz": 32,
        "cup": 3.94314,
        "pint": 2,
        "gallon": 0.25,
    },
    "gallon": {
        "ml": 3785.41,
        "liters": 3.78541,
        "fl oz": 128,
        "cup": 15.7725,
        "pint": 7.74597,
        "quart": 4,
    },
}


def convert(cb1, e1):
    try:
        unit1 = cb1.get()
        unit2 = cb2.get()

        if (
            unit1 in LIQUID_CONVERSION_FACTORS
            and unit2 in LIQUID_CONVERSION_FACTORS[unit1]
        ):
            factor = LIQUID_CONVERSION_FACTORS[unit1][unit2]
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
root.title("Liquid Unit Converter")
root.geometry("600x350")

from_units = list(LIQUID_CONVERSION_FACTORS.keys())
to_units = ["ml", "liters", "fl oz", "cup", "pint", "quart", "gallon"]

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
