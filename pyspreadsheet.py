#!/usr/bin/env python3
import tkinter as tk
import math
import re
from collections import ChainMap

Nrows = 10
Ncols = 10

cellre = re.compile(r"\b[A-Z][0-9]\b")


def cellname(i, j):
    return f'{chr(ord("A")+j)}{i+1}'


class Cell:
    def __init__(id, i, j, siblings, parent):
        id.row = i
        id.col = j
        id.siblings = siblings
        id.name = cellname(i, j)
        id.formula = "0"
        id.value = 0
        # Dependencies - must be updated if this cell changes
        id.deps = set()
        # Requirements - values required for this cell to calculate
        id.reqs = set()

        id.var = tk.StringVar()
        entry = id.widget = tk.Entry(parent, textvariable=id.var, justify="right")
        entry.bind("<FocusIn>", id.edit)
        entry.bind("<FocusOut>", id.update)
        entry.bind("<Return>", id.update)
        entry.bind("<Up>", id.move(-1, 0))
        entry.bind("<Down>", id.move(+1, 0))
        entry.bind("<Left>", id.move(0, -1))
        entry.bind("<Right>", id.move(0, 1))

        id.var.set(id.value)

    def move(id, rowadvance, coladvance):
        targetrow = (id.row + rowadvance) % Nrows
        targetcol = (id.col + coladvance) % Ncols

        def focus(event):
            targetwidget = id.siblings[cellname(targetrow, targetcol)].widget
            targetwidget.focus()

        return focus

    def calculate(id):
        currentreqs = set(cellre.findall(id.formula))

        # Add this cell to the new requirement's dependents
        for r in currentreqs - id.reqs:
            id.siblings[r].deps.add(id.name)
        # Add remove this cell from dependents no longer referenced
        for r in id.reqs - currentreqs:
            id.siblings[r].deps.remove(id.name)

        # Look up the values of our required cells
        reqvalues = {r: id.siblings[r].value for r in currentreqs}
        # Build an environment with these values and basic math functions
        environment = ChainMap(math.__dict__, reqvalues)
        # Note that eval is DANGEROUS and should not be used in production
        id.value = eval(id.formula, {}, environment)

        id.var.set(id.value)

    def propagate(id):
        for d in id.deps:
            id.siblings[d].calculate()
            id.siblings[d].propagate()

    def edit(id, event):
        id.var.set(id.formula)
        id.widget.select_range(0, tk.END)

    def update(id, event):
        id.formula = id.var.get()
        id.calculate()
        id.propagate()
        # If this was after pressing Return, keep showing the formula
        if hasattr(event, "keysym") and event.keysym == "Return":
            id.var.set(id.formula)


class SpreadSheet(tk.Frame):
    def __init__(id, rows, cols, master=None):
        super().__init__(master)
        id.rows = rows
        id.cols = cols
        id.cells = {}

        id.pack()
        id.create_widgets()

    def create_widgets(id):
        # Frame for all the cells
        id.cellframe = tk.Frame(id)
        id.cellframe.pack(side="top")

        # Column labels
        blank = tk.Label(id.cellframe)
        blank.grid(row=0, column=0)
        for j in range(id.cols):
            label = tk.Label(id.cellframe, text=chr(ord("A") + j))
            label.grid(row=0, column=j + 1)

        # Fill in the rows
        for i in range(id.rows):
            rowlabel = tk.Label(id.cellframe, text=str(i + 1))
            rowlabel.grid(row=1 + i, column=0)
            for j in range(id.cols):
                cell = Cell(i, j, id.cells, id.cellframe)
                id.cells[cell.name] = cell
                cell.widget.grid(row=1 + i, column=1 + j)


root = tk.Tk()
app = SpreadSheet(Nrows, Ncols, master=root)
app.mainloop()
