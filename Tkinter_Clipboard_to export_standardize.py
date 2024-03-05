import tkinter as tk
from tkinter import *

fv = "Field value to output"  # returned from another part of the code

# triggered off left button click on text_field
def copy_text_to_clipboard(event):
    fv = text.get(
        "1.0", "end-1c"
    )  # get field value from event, but remove line return at end
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(fv)  # append new value to clipbaord


root = tk.Tk()

# setup frame and grid
frm = tk.Frame(root)
frm.grid()

# setup our inline label and widget
Label(frm, text="Field Label").grid(row=0, column=0)
text = tk.Text(frm, height=1, borderwidth=0)
text.insert(1.0, fv)
text.grid(row=0, column=1)

# Bind left click on text widget to copy_text_to_clipboard() function
text.bind("<Button-1>", copy_text_to_clipboard)
root.mainloop()
