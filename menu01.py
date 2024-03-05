import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys

root = tk.Tk()
root.geometry("600x600")


def get_filename(_type=""):
    "Returns the path and name of file selected"
    # _type=".txt" to get txt file name

    filename = filedialog.askopenfilename(
        initialdir=".",  # same dir of this script
        title="Select file",
        filetypes=(("", _type), ("all files", "*.*")),
    )
    return filename


# main_menu = OptionMenu(root, clicked, "C++", "Java", "Python", "Rust","Go","Ruby")
# main_menu.grid(row=1, column=2)


# filename = get_filename("")
# name = messagebox.showinfo(
# title="Name of the file you picked" , message=filename)

menubar = tk.Menu(root)
menubar.add_command(label="Click me", command=None)
menubar.add_command(label="File", command=get_filename)
menubar.add_command(label="Call", command=None)
menubar.add_command(label="Insert", command=None)
menubar.add_command(label="Run", command=None)
menubar.add_command(label="1", command=None)
menubar.add_command(label="2", command=None)
menubar.add_command(label="3", command=None)
menubar.add_command(label="4", command=None)
menubar.add_command(label="5", command=None)


root.config(menu=menubar)


if __name__ == "__main__":

    root.mainloop()
