#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser, font
import pyautogui as pg
import pyperclip
import os
import sys

# import subprocess
# import shutil
import pathlib
from PIL import Image, ImageTk
import runpy
import glob


r = tk.Tk()
r.geometry("1850x1080")
path = os.getcwd()
r.title("GUI TEMPLATE")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=1)
f1 = ttk.Frame(notebook, width=1900, height=1080)
f1.grid(row=0, column=1)
bf1 = ttk.Frame(f1)
bf1.grid(row=0, column=0)
spfrm = ttk.Frame(f1)
spfrm.grid(row=14, column=0)
# f1.columnconfigure(4, weight=3)
# f1.rowconfigure(10, weight=1)
notebook.add(f1, text="TAB1")


# ------------------------------
# Functions and call backs
# --------------------------------------------------------------------


def run(event):
    x = lb.curselection()[0]
    file = lb.get(x)
    runpy.run_path(path_name=file)


def opensystem(event):

    x = lb.curselection()[0]

    file = lb.get(x)
    with open(file, "r") as file:
        file = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, file)

        return


def showcontent(x):

    lb.focus()
    x = lb.curselection()[0]
    file = lb.get(x)
    with open(file, "r") as file:
        file = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, file)

        return


str_code_block = """
 -----------------------------------------------------------------------------
 GUI Magic Starts Here
 ----------------------------------------------------------------------------

r = tk.Tk()
r.geometry("1850x1080")
r.title("GUI TEMPLATE")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=1)
f1 = ttk.Frame(r, width=1800, height=1000)
f1.grid(row=0, column=1)
bf1 = ttk.Frame(f1)
bf1.grid(row=0, column=0)
spfrm = ttk.Frame(f1)
spfrm.grid(row=14, column=0)
# f1.columnconfigure(4, weight=3)
# f1.rowconfigure(10, weight=1)
notebook.add(f1, text="TAB1")


text = tk.Text(f1, height=60, width=150, bg="white")
text.insert("1.0", tk.END)
text.grid(row=0, column=3)
"""


def runpyprg(event):

    file = lb.get(ANCHOR)
    runpy.run_path(path_name=file)

    return


def run():
    x = lb.curselection()[0]

    runpy.run_path(path_name=lb.get(x))


lb = tk.Listbox(f1, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
lb.grid(row=0, column=2, sticky="nswe")
lb.focus()
lb.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb.insert(tk.END, item)
lb.bind("<Double-Button-1>", opensystem)
lb.bind("<<ListboxSelect>>", showcontent)
lb.bind("<Double-Button-2>", runpyprg)


def command():
    pass


def savef():
    a = text.get("1.0", tk.END)
    filepath = asksavefilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    with open(filepath, "w") as f:
        f.write(a)

        return f


def fname():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text.insert(tk.END, text)
        return filepath


def fname2():
    filepath2 = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text2 = input_file.read()
        text2.insert(tk.END, text)
        return filepath2


def newdirlist():
    a = "/home/jh/Desktop/Codeview_Project/"

    path = filedialog.askdirectory(initialdir=a)
    os.chdir(path)
    flist = os.listdir(path)
    lb.delete(0, tk.END)

    for item in flist:

        lb.insert(tk.END, item)
    return flist


def preselect():

    d = sp.get()
    if d == 1:
        path = "/home/jh/Dektop/codeview/"
    elif d == 2:
        path = "/home/jh/Dektop/codeview/ref"

    elif d == 3:
        path = "/home/jh/Desktop/Codeview_Project/code to evaluate for this project/"
    elif d == 4:
        path = "/home/jh/Desktop/Codeview_Project/TkGUIgen-master/"
    elif d == 5:
        path = "/home/jh/Dektop/codeview//home/jh/Desktop/Codeview_Project/tests/"
    elif d == 6:
        path = "/home/jh/Desktop/Clipboard_Project/"
    elif d == 7:
        path = "/home/jh/Desktop/Redirect project/"
    elif d == 8:
        path = "/home/jh/Desktop/PY_PROGRAMS WORKING WITH/"
    elif d == 9:
        path = "/home/jh/Dektop/codeview//home/jh/Desktop/canvas_subproject/"
    elif d == 10:
        path = "/home/jh/Desktop/VERY_USEFUL_ CODE GUI_EXAMPLES__/"
    elif d == 11:
        path = "/home/jh/Desktop/StringMalipulationtionGUIProj1/"
    elif d == 12:
        path = "/media/jh/Backup_Data/Python Master Set/Python_PROJECTS/CLI2GUI/"
    elif d == 13:
        path = "/media/jh/Backup_Data/Python_Notes&Projects/CODE_SNIPPETS__/CODE_BASE/"
    elif d == 14:
        path = "/home/jh/Dektop/codeview/"
    else:
        path = "/home/jh"

    os.chdir(path)
    flist = os.listdir(path)
    lb.delete(0, tk.END)
    for item in flist:

        lb.insert(tk.END, item)
    return flist


def tkfont():
    runpy.run_path(path_name="tkfontchooser.py")


def guigen():
    runpy.run_path(path_name="gui_gen.py")


def edit2():
    runpy.run_path(path_name="editor2.py")


def colorwordlist():
    runpy.run_path(path_name="colorlist.py")


def colorpic():
    runpy.run_path(path_name="color.py")

    # prgvar = "home/jh/Desktop/Codeview_Project/color.py"
    mycolor = color.get()

    # subprocess.Popen(["pyth


def py_jswon_veiwer():
    runpy.run_path(path_name="py_jswon_veiwer.py")


def runpyprg():
    file = lb.get(ANCHOR)
    runpy.run_path(path_name=file)
    return


##menubar = Menu(r)
##filemenu = Menu(menubar)
##filemenu.add_command(label="New", command=fname)
##filemenu.add_command(label="Open", command=fname2)
##filemenu.add_command(label="Save", command=savef)
##filemenu.add_command(label="Save As..", command=savef)
##filemenu.add_command(label="Quit", command=r.quit)
##menubar.add_cascade(label="File", menu=filemenu)


btn2 = tk.Button(bf1, text="GUI Generator", command=guigen)
btn2.grid(column=0, row=1)
btn3 = tk.Button(bf1, text="Editor2", command=edit2)
btn3.grid(column=0, row=2)
btn4 = tk.Button(bf1, text="fname", command=fname)
btn4.grid(column=0, row=3)
btn5 = tk.Button(bf1, text="RUN", command=run)
btn5.grid(column=0, row=4)
btn6 = tk.Button(bf1, text="Color Picker", command=colorpic)
btn6.grid(column=0, row=5)
btn7 = tk.Button(bf1, text="EXE PY PRG", command=runpyprg)
btn7.grid(column=0, row=6)


btn8 = tk.Button(bf1, text="color wordlist", command=colorwordlist)
btn8.grid(column=0, row=7)
btn9 = tk.Button(bf1, text="py_jswon_veiwer", command=py_jswon_veiwer)
btn9.grid(column=0, row=8)
btn10 = tk.Button(bf1, text="fname", command=fname)
btn10.grid(column=0, row=9)
btn11 = tk.Button(bf1, text="RUN", command=run)
btn11.grid(column=0, row=10)
btn12 = tk.Button(bf1, text="Color Picker", command=colorpic)
btn12.grid(column=0, row=11)
btn13 = tk.Button(bf1, text="EXE PY PRG", command=runpyprg)
btn13.grid(column=0, row=12)

btn14 = tk.Button(bf1, text="get dir", command=newdirlist)
btn14.grid(row=13, column=0)
btn15 = tk.Button(bf1, text="tk.Font View & Chose", command=tkfont)
btn15.grid(column=0, row=15)


# ---------------------------------------------------------------------
# Next Tab  TAB2 f2
# ---------------------------------------------------------------------


def key(event):
    tk.Label(f3, repr(event.char), text="pressed".grid(row=0, column=3))


def xypos(event):
    a = event.x
    b = event.y
    e1 = tk.Label(f3, text=a, font=("URW Chancery L", 12))
    e1.grid(row=0, column=5)
    e2 = tk.Label(f3, text=b, font=("URW Chancery L", 12))
    e2.grid(row=11, column=5)
    ttt.insert(
        tk.END,
        "X=",
    )
    ttt.insert(tk.END, a)
    ttt.insert(tk.END, "Y=")
    ttt.insert(tk.END, b)
    ttt.insert(tk.END, "\n")
    # print "clicked at", event.x, event.y


def cmdbtn():
    runpy.run_path(path_name="cmd_btn_console.py")


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)


def clear():
    txt_edit.delete("1.0", tk.END)


def ggtxt():
    a = text.get("1.0", tk.END)
    txt_edit.insert(tk.END, a)


def ggtxt2():
    a = text2.get("1.0", tk.END)
    txt_edit.insert(tk.END, a)


def newdirlist():

    os.chdir(path)
    flist = os.listdir(path)
    lbox.delete(0, tk.END)
    for item in flist:

        lbox.insert(tk.END, item)
    return flist


def guicodelist():
    path = "/home/jh/Desktop/VERY_USEFUL_ CODE GUI_EXAMPLES__/"
    os.chdir(path)
    flist = os.listdir(path)
    lbox.delete(0, tk.END)
    for item in flist:

        lbox.insert(tk.END, item)


def guicodelist2():
    path = "/home/jh/Desktop/VERY_USEFUL_ CODE GUI_EXAMPLES__/"
    path = filedialog.askdirectory()
    os.chdir(path)
    flist = os.listdir(path)
    lbox.delete(0, tk.END)
    for item in flist:
        lbox.insert(tk.END, item)
        return path


f2 = ttk.Frame(notebook)
notebook.add(f2, text="TAB2")

txt_edit = tk.Text(f2, height=500, width=500)
fr_buttons = tk.Frame(f2, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=1, column=0)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_save.grid(row=2, column=0)
btn_clear = tk.Button(fr_buttons, text="Clear", command=clear)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_grab = tk.Button(fr_buttons, text="Grab", command=ggtxt)
btn_grab.grid(row=4, column=0)
# btn_s.grid(row=1, column=0, sticky="ew", padx=5)
btn_grab2 = tk.Button(fr_buttons, text="Grab Tab6", command=ggtxt2)
btn_grab2.grid(row=5, column=0)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


f3 = ttk.Frame(notebook)
notebook.add(f3, text="TAB3")
canvas_width = 1800
canvas_height = 900
w = Canvas(f3, width=canvas_width, height=canvas_height, bg="wheat")
w.grid(row=0, column=0)
w.bind("<Key>", key)
w.bind("<Button-1>", xypos)
f4 = ttk.Frame(r)
notebook.add(f4, text="4")

ttt = tk.Text(f4, height=40, width=20)
ttt.grid(row=1, column=1)

llbx = tk.Listbox(f4)
llbx.grid(row=1, column=4)

ccom = [
    "s.capitalize()",
    "s.count()",
    "s.count()",
    "s.index()",
    "s.title()",
    "s.replace()",
    "s.upper()",
    "s.lower()",
    "s.find()",
]
stuff = ["for i in range(  ):"]
comb = ttk.Combobox(f4, values=ccom)
comb.grid(row=1, column=2)

comb2 = ttk.Combobox(f4, values=stuff)
comb.grid(row=1, column=3)


f5 = ttk.Frame(notebook)
notebook.add(f5, text="TAB5")


def checkered(canvas, line_distance):
    # graph like line reference horizontal
    canvas.create_line(10, 400, 1900, 400, fill="blue", width=4)
    # graph like line vertical
    canvas.create_line(910, 10, 910, 900, fill="green", width=4)

    canvas.create_line(50, 390, 50, 410, fill="blue", width=4)
    canvas.create_line(100, 390, 100, 410, fill="blue", width=4)
    canvas.create_line(150, 390, 150, 410, fill="blue", width=4)
    canvas.create_line(200, 390, 200, 410, fill="blue", width=4)
    canvas.create_line(250, 390, 250, 410, fill="blue", width=4)
    canvas.create_line(300, 390, 300, 410, fill="blue", width=4)
    canvas.create_line(350, 390, 350, 410, fill="blue", width=4)
    canvas.create_line(400, 390, 400, 410, fill="blue", width=4)
    canvas.create_line(450, 390, 450, 410, fill="blue", width=4)
    canvas.create_line(500, 390, 500, 410, fill="blue", width=4)
    canvas.create_line(550, 390, 550, 410, fill="blue", width=4)
    canvas.create_line(600, 390, 600, 410, fill="blue", width=4)
    canvas.create_line(650, 390, 650, 410, fill="blue", width=4)
    canvas.create_line(700, 390, 700, 410, fill="blue", width=4)
    canvas.create_line(750, 390, 750, 410, fill="blue", width=4)
    canvas.create_line(800, 390, 800, 410, fill="blue", width=4)
    canvas.create_line(850, 390, 850, 410, fill="blue", width=4)
    canvas.create_line(900, 390, 900, 410, fill="blue", width=4)
    canvas.create_line(950, 390, 950, 410, fill="blue", width=4)
    canvas.create_line(1000, 390, 1000, 410, fill="blue", width=4)
    canvas.create_line(1050, 390, 1050, 410, fill="blue", width=4)
    canvas.create_line(1100, 390, 1100, 410, fill="blue", width=4)
    canvas.create_line(1150, 390, 1150, 410, fill="blue", width=4)
    canvas.create_line(1200, 390, 1200, 410, fill="blue", width=4)
    canvas.create_line(1250, 390, 1250, 410, fill="blue", width=4)
    canvas.create_line(1300, 390, 1300, 410, fill="blue", width=4)
    canvas.create_line(1350, 390, 1350, 410, fill="blue", width=4)
    canvas.create_line(1400, 390, 1400, 410, fill="blue", width=4)
    canvas.create_line(1450, 390, 1450, 410, fill="blue", width=4)
    canvas.create_line(1500, 390, 1500, 410, fill="blue", width=4)
    canvas.create_line(1550, 390, 1550, 410, fill="blue", width=4)
    canvas.create_line(1600, 390, 1600, 410, fill="blue", width=4)
    canvas.create_line(1650, 390, 1650, 410, fill="blue", width=4)
    canvas.create_line(1700, 390, 1700, 410, fill="blue", width=4)
    canvas.create_line(1750, 390, 1750, 410, fill="blue", width=4)
    canvas.create_line(1800, 390, 1800, 410, fill="blue", width=4)

    canvas.create_line(900, 20, 920, 20, fill="blue", width=4)
    canvas.create_line(900, 30, 920, 30, fill="blue", width=4)
    canvas.create_line(900, 50, 920, 50, fill="blue", width=4)
    canvas.create_line(900, 100, 920, 100, fill="blue", width=4)
    canvas.create_line(900, 150, 920, 150, fill="blue", width=4)
    canvas.create_line(900, 200, 920, 200, fill="blue", width=4)
    canvas.create_line(900, 250, 920, 250, fill="blue", width=4)
    canvas.create_line(900, 300, 920, 300, fill="blue", width=4)
    canvas.create_line(900, 350, 920, 350, fill="blue", width=4)
    canvas.create_line(900, 400, 920, 400, fill="blue", width=4)
    canvas.create_line(900, 450, 920, 450, fill="blue", width=4)
    canvas.create_line(900, 500, 920, 500, fill="blue", width=4)
    canvas.create_line(900, 550, 920, 550, fill="blue", width=4)
    canvas.create_line(900, 600, 920, 600, fill="blue", width=4)
    canvas.create_line(900, 650, 920, 650, fill="blue", width=4)
    canvas.create_line(900, 700, 920, 700, fill="blue", width=4)
    canvas.create_line(900, 750, 920, 750, fill="blue", width=4)
    canvas.create_line(900, 900, 920, 900, fill="blue", width=4)
    canvas.create_line(900, 850, 920, 850, fill="blue", width=4)
    canvas.create_line(900, 900, 920, 900, fill="blue", width=4)
    canvas.create_line(900, 950, 920, 950, fill="blue", width=4)
    canvas.create_line(900, 1000, 920, 1000, fill="blue", width=4)
    canvas.create_text(
        300, 50, text="300x50", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        300, 450, text="300x450", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        50, 450, text="50x450", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        800, 800, text="800x800", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        400, 600, text="400x600", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        200, 150, text="200x150", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1300, 500, text="1300x500", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1700, 800, text="1700x800", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1600, 250, text="1600x250", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1500, 150, text="1500x150", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1400, 650, text="1400x650", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1300, 450, text="1300x450", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1200, 700, text="1200x700", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1100, 900, text="1100x900", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        1000, 50, text="1000x50", fill="black", font=("URW Chancery L", 15)
    )
    canvas.create_text(
        900, 750, text="900x750", fill="black", font=("URW Chancery L", 15)
    )

    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


# canvas_width = 1900
# canvas_height = 900
# canvas = Canvas(f5, width=canvas_width, height=canvas_height, bg='SeaGreen1')
# canvas.grid(row=0, column=0)


checkered(w, 10)
###Functions for TAB 6


def lboxfun(event):

    lbox.focus()
    lbox.configure(selectmode="")
    x1 = lbox.get(ANCHOR)


def showcontent2(x):

    lb.focus()
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file, "r") as file:
        file = file.read()
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, file)
        lboxfun()
        return


def opensystem2(event):

    x = lbox.curselection()[0]

    file = lbox.get(x)
    with open(file, "r") as file:
        file = file.read()
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, file)

        return


def op():
    path = "/home/jh/Desktop/Codeview_Project/ref/"
    files = os.listdir()
    for file in files:
        lbox.insert(tk.END, file)
        return


f6 = ttk.Frame(notebook)
notebook.add(f6, text="TAB6")
ff6 = ttk.Frame(f6)
ff6.grid(row=0, column=0, rowspan=4)
##
##
##
##text2 = tk.Text(f6, height=60, width=150, bg='white')
##text2.insert('1.0', tk.END)
##text2.grid(row=0, column=0)
text2 = tk.Text(f6, height=55, width=100, bg="white")
text2.insert("1.0", tk.END)
text2.grid(row=1, column=5)
lbox = tk.Listbox(f6, bg="light blue", exportselection=False, selectmode=tk.MULTIPLE)
lbox.grid(row=1, column=3, sticky="nswe")
lbox.focus()
lbox.configure(selectmode="")
btnf6 = tk.Button(ff6, text="get dir", command=newdirlist)
btnf6.grid(row=0, column=0)
btnf7 = tk.Button(ff6, text="Go GUI", command=guicodelist)
btnf7.grid(row=1, column=0)

btn200 = tk.Button(ff6, text="veiw2", command=guicodelist2)
btn200.grid(column=0, row=2)
btn3 = tk.Button(ff6, text="Help Files", command=op)
btn3.grid(column=0, row=3)
btn4 = tk.Button(ff6, text="btn", command=fname)
btn4.grid(column=0, row=4)
btn5 = tk.Button(ff6, text="btn", command=run)
btn5.grid(column=0, row=5)
btn6 = tk.Button(ff6, text="btn", command=colorpic)
btn6.grid(column=0, row=6)
btn7 = tk.Button(ff6, text="button", command=runpyprg)
btn7.grid(column=0, row=7)

lbox.bind("<<ListboxSelect>>", showcontent2)
lbox.bind("<Double-Button-1>", opensystem2)
##########################################################
#####Function2 for Tab 7
##########################################################

ecount = 1
btncount = 1
btncount2 = 1
labelcount = 1
canvascount = 1
lboxcount = 1
rowcount = 1
columncount = 1
combocount = 1
spincount = 1
textcount = 1
slidercount = 1
scrollcount = 1
projectcount = 1


start_string = """
#! /usr/bin/python3
# proj_str
root = tk.Tk()
root.title("Tkinter widget helper")

frame1 = tk.Frame(root, height=300, width=300)
frame1.grid(row=0, rowspan=10, column=5, columnspan=10)
frame2 = tk.Frame(root, height=300, width=300)
frame2.grid(row=0, column=0, rowspan=5, columnspan=5)
"""


def e_code():
    global ecount, rowcount
    w_str = """
display1 = tk.StringVar()
entry1 = tk.e(root,
    relief=tk.FLAT,
    textvariable=display1,
    justify='right',
    bg='orange')
entry1.grid(row=1, column=4)
entry1["font"] = "arial 12 bold"
    """
    w_str2 = w_str.replace("display1", "display" + str(ecount))
    w_str3 = w_str2.replace("entry1", "entry" + str(ecount))
    w_str4 = w_str3.replace("row=1", "row=" + str(rowcount))
    textt.insert(tk.END, w_str4)
    ecount += 1
    rowcount += 1


def entrycol():
    global ecount, columncount
    w_str = """
display1 = tk.StringVar()
entry1 = tk.e(root,
    relief=tk.FLAT,
    textvariable=display1,
    justify='right',
    bg='orange')
entry1.grid(row=1, column=4)
entry1["font"] = "arial 12 bold"
    """
    w_str2 = w_str.replace("display1", "display" + str(ecount))
    w_str3 = w_str2.replace("entry1", "entry" + str(ecount))
    w_str4 = w_str3.replace("column1", "column=" + str(columncount))
    textt.insert(tk.END, w_str4)
    ecount += 1
    columncount += 1


def button_code1():
    global btncount, rowcount
    w_str = """
b1 = tk.Button(root,
            #relief=tk.FLAT,
            compound=tk.LEFT,
            text="new",
            #command=None,

            )
b1.grid(row=1, column=2)
"""
    w_str2 = w_str.replace("b1", "b" + str(btncount))
    w_str3 = w_str2.replace("row=1", "row=" + str(rowcount))
    textt.insert(tk.END, w_str3)
    btncount += 1
    rowcount += 1


def button_code2():
    global btncount2, columncount
    w_str = """
btn1 = tk.Button(root,
            #relief=tk.FLAT,
            compound=tk.LEFT,
            text="new",
            #command=None,

            )
btn1.grid(row=2, column=1)
"""
    w_str2 = w_str.replace("btn1", "btn" + str(btncount2))
    w_str3 = w_str2.replace("column=1", "column=" + str(columncount))
    textt.insert(tk.END, w_str3)
    btncount2 += 1
    columncount += 1


def label_code1():
    global labelcount, rowcount
    label_str = """
label1 = tk.Label(root
        ft = tkFont.Font(family='Ariel Black',size=10)
        label1["font"] = ft
        label1["fg"] = "#333333",
        label1["justify"] = "center",
        label1["text"] = "label",
        width=100,height=25)
        label1.grid(row=4, column=2) """
    label_str2 = label_str.replace("label1", "label" + str(labelcount))
    label_str3 = label_str2.replace("row=1", "row=" + str(rowcount))
    textt.insert(tk.END, label_str3)
    labelcount += 1
    rowcount += 1


def label_code2():
    global labelcount, columncount
    label_str = """
label1 = tk.Label(root
        ft = tkFont.Font(family='Ariel Black',size=10)
        label1["font"] = ft
        label1["fg"] = "#333333",
        label1["justify"] = "center",
        label1["text"] = "label",
        width=100,height=25)
        label1.grid(row=5, column=2) """
    label_str2 = label_str.replace("label1", "label" + str(labelcount))
    label_str3 = label_str2.replace("column=1", "column=" + str(columncount))
    textt.insert(tk.END, label_str3)
    labelcount += 1
    columncount += 1


def listbox_code():
    global lboxcount
    lbox_str = """
lbox1=tk.Listbox(root, width=80, height=25)
    lbox1["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    lbox1["font"] = ft
    lbox1["fg"] = "#333333"
    lbox1["justify"] = "center"
    lbox1.grid(row=9, coloumn=3)  """
    lbox_str2 = lbox_str.replace("lbox1", "lbox" + str(lboxcount))
    textt.insert(tk.END, lbox_str2)
    lboxcount += 1


def menu1_code():
    menu1_str = """
root.option_add('*tearOff',False)
    menubar = Menu(root)
    root.config(menu = menubar)
    File = Menu(menubar)
    Edit = Menu(menubar)
    Help_ = Menu(menubar)
    menubar.add_cascade( menu = File , label = 'File')
    menubar.add_cascade( menu = Edit , label = 'Edit')
    menubar.add_cascade( menu = Help_, label = 'Help')
    File.add_command( label = 'New', command = lambda: print(" New File"))
    File.add_separator()
    File.add_command( label = 'Open',command = lambda: print("Open File"))
    File.add_separator()
    save = Menu(File)
    File.add_cascade( menu = save , label ='Save')
    save.add_command(label ='Save_as', command = lambda: print(" Save as"))
    save.add_command(label ='Save_all',command = lambda: print(" Save all"))
    """
    textt.insert(tk.END, menu1_str)


def menu2_code():
    menu2_str = """
    def open():
    messagebox.shorootfo('From My Computer','Your File has been Opened')
    def close():
    messagebox.shorootfo('From My Computer','Your File has been Closed')
    def nothing():
    messagebox.shorootfo('From My Computer','Are You Feeling Well')

    menubar = Menu(root)

    filemenu = Menu(menubar)
    filemenu.add_command(label="Open File",command=open)
    filemenu.add_command(label="New File",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Save",command=nothing)
    filemenu.add_command(label="Save As",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Close",command=close)
    filemenu.add_command(label="Close Tab",command=nothing)
    filemenu.add_command(label="Close window",command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.quit)

    menubar.add_cascade(label="File", menu = filemenu)

    editmenu = Menu(menubar)
    editmenu.add_command(label="Undo",command=nothing)
    editmenu.add_command(label="Redo",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Copy",command=nothing)
    editmenu.add_command(label="Paste",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Columns",command=nothing)
    editmenu.add_command(label="Lines",command=nothing)
    editmenu.add_command(label="Text",command=nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Exit",command=root.quit)

    menubar.add_cascade(label="Edit", menu = editmenu)

    root.config(menu = menubar)
    """
    textt.insert(tk.END, menu2_str)


def canvas_code():
    global canvascount
    canvas_str = """
canvas1 = Canvas(root)
    canvas.grid(row=1, column=1)
    canvas.config(width = 700 , height = 800)

    line = canvas.create_line(40,70, 79,140 , fill ='red', width = 7)

    """

    canvas_str2 = canvas_str.replace("canvas1", "canvas" + str(canvascount))
    textt.insert(tk.END, canvas_str2)
    canvascount += 1


def combo_code():
    global combo_str, combocount
    combo_str = """
cbox1 = ttk.Combobox(root, values=["Value1", "value2, "value3"])
cbox1.grid(column=0, row=1)"""
    combo_str2 = combo_str.replace("cbox1", "cbox" + str(combocount))
    textt.insert(tk.END, combo_str2)
    combocount += 1


def spin_code():
    global spincount
    spin_str = """
sp1 = tk.Spinbox(root, from_=1.0, to=1000.0, increment=0.1)
    sp1.grid(row=1, column=0)"""
    spin_str2 = spin_str.replace("sp1", "sp" + str(spincount))
    textt.insert(tk.END, spin_str2)
    spincount += 1


def text_code():
    global textcount, spincount
    txt_str = """ 
txt1 = tk.Text(root, height=60, width=150, bg='white')
txt1.insert('1.0', tk.END)
txt1.grid(row=2, column=3)"""
    txt_str2 = txt_str.replace("txt1", "txt" + str(txtcount))
    textt.insert(tk.END, txt_str2)
    textcount += 1


def slider():

    sld_str = """
slider1 = ttk.Scale(slider_str2 = slidar_str.replace("slider1", "slider" + str(slidercount))
    text.insert(tk.END, slider_str2)
    slidercount += 1"""
    textt.insert(tk.END, sld_str)


def scrollbar():

    # scrollcount not goint to add counter for this yet
    scr_str1 = """
scrollbar = tk.Scrollbar(command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

text['yscrollcommand'] = scrollbar.set
"""
    textt.insert(tk.END, scr_str1)


def scrollbarh():

    # scrollcount not goint to add counter for this yet
    scrh_str = """
scrollbar = tk.Scrollbar(command=text.xview)
scrollbar.grid(row=0, column=1, sticky='ns')

text['xscrollcommand'] = scrollbar.set
"""
    textt.insert(tk.END, scr_str1)


def restartstr():
    textt.insert(tk.END, start_string)


def cleartext():
    textt.delete("1.0", tk.END)


def open_code():
    # file type
    filetypes = [
        ("Python files", "*.py"),
        ("text files", "*.txt"),
        ("All files", "*.*"),
    ]
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert("1.0", f.readlines())


def save_code():
    global textt, projectpy, start_string
    str_last = """
root.mainloop"""
    textt.insert(tk.END, str_last)
    filetypes = [
        ("Python files", "*.py"),
        ("Text files", "*.txt"),
        ("All files", "*.*"),
    ]
    f = filedialog.asksaveasfile(
        title="Open a file", initialdir="/home/jh/Desktop", filetypes=filetypes
    )


def runcode():
    filetypes = [("Python files", "*.py"), ("All files", "*.*")]
    # show the open file dialog
    f = filedialog.askopenfilename(filetypes=filetypes)
    runpy.run_path(path_name=f)


str_win_position = """

root = tk.Tk() # create a Tk root window

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))"""

filename = "project.py"


def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  # line 0 coloum 0


def saveFile():
    global filename
    t = text.get(0.0, END)  # store all the text from text box
    f = open(filename, "w")  # open the file
    f.write(t)  # store
    f.close()


def saveAs():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file..")


def openFile():
    f = askopenfile(mode="r")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, tk.END)


f7 = ttk.Frame(notebook)
notebook.add(f7, text="TAB7")
ff7 = ttk.Frame(f7, height=40, width=30)
ff7.grid(row=0, column=4, columnspan=2, rowspan=6)
##tk.Label(f7, text="  ").grid(row=0, column=0)
##tk.Label(f7, text="                        ").grid(row=0, column=1)
##tk.Label(f7, text="c2                      ").grid(row=0, column=2)
##tk.Label(f7, text="c3                       ").grid(row=0, column=3)
##tk.Label(f7, text="c4                            ").grid(row=0, column=4)
##tk.Label(f7, text="c5                                   ").grid(row=0, column=5)


text = tk.Text(f1, height=60, width=100, bg="white")
text.insert("1.0", tk.END)
text.grid(row=0, column=3)


textt = tk.Text(f7, height=60, width=50)
textt.grid(row=4, column=1)
textt.insert(tk.END, start_string)

scrollbar = tk.Scrollbar(f1)
scrollbar.grid(row=0, column=4, sticky="nswe")
scrollbar.config(command=text.yview)


# tt = tk.Toplevel(f7)

###############################################################
# Button control have to be on another tab no show in with text widget
###############################################################
##
##
##f7 = ttk.Frame(r)
##notebook.add(f7, text="TAB8")
##
##tk.Label(f7, text="  ").grid(row=0, column=0)
##tk.Label(f7, text="                        ").grid(row=0, column=1)
##tk.Label(f7, text="c2                      ").grid(row=0, column=2)
##tk.Label(f7, text="c3                       ").grid(row=0, column=3)
##tk.Label(f7, text="c4                            ").grid(row=0, column=4)
##tk.Label(f7, text="c5                                   ").grid(row=0, column=5)
b111 = tk.Button(ff7, text="Entry Widget", command=e_code)
b111.grid(row=4, column=4)

b112 = tk.Button(ff7, text="Entry2 column", command=entrycol)
b112.grid(row=4, column=4)


b222 = tk.Button(ff7, text="Insert Button row", command=button_code1)
b222.grid(row=5, column=4)
b55 = tk.Button(ff7, text="Insert Button column", command=button_code2)
b55.grid(row=6, column=4)
b44 = tk.Button(ff7, text="Insert label row", command=label_code1)
b44.grid(row=7, column=4)
b57 = tk.Button(ff7, text="List Box", command=listbox_code)
b57.grid(row=8, column=4)
b64 = tk.Button(ff7, text="Menu1", command=menu1_code)
b64.grid(row=9, column=4)
b78 = tk.Button(ff7, text="Menu2", command=menu2_code)
b78.grid(row=10, column=4)
b80 = tk.Button(ff7, text="Canvas", command=canvas_code)
b80.grid(row=11, column=4)
b97 = tk.Button(ff7, text="Combobox", command=combo_code)
b97.grid(row=12, column=4)
bba = tk.Button(ff7, text="Spinbox", command=spin_code)
bba.grid(row=13, column=4)
bb1 = tk.Button(ff7, text="Text Box", command=text_code)
bb1.grid(row=14, column=4)
b149 = tk.Button(ff7, text="insert label col", command=label_code2)
b149.grid(row=15, column=4)
b151 = tk.Button(ff7, text="Slider Widget", command=slider)
b151.grid(row=16, column=4)
b162 = tk.Button(ff7, text="Scroll Bar", command=scrollbar)
b162.grid(row=17, column=4)
b163 = tk.Button(ff7, text="Scroll Bar Hozontal", command=scrollbarh)
b163.grid(row=17, column=5)
b177 = tk.Button(ff7, text="Clear Code Box", command=cleartext)
b177.grid(row=18, column=4)
b188 = tk.Button(ff7, text="Restart 1st Code Block", command=restartstr)
b188.grid(row=19, column=4)
b199 = tk.Button(ff7, text="Finish & Save", command=save_code)
b199.grid(row=20, column=4)
b203 = tk.Button(ff7, text="Open File", command=open_code)
b203.grid(row=21, column=4)

b21 = tk.Button(ff7, text="Run project", command=runcode)
b21.grid(row=21, column=4)


###################################################################


if __name__ == "__main__":
    r.mainloop()
