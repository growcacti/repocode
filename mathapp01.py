import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font
import math
import random
import subprocess
import os

from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


root = tk.Tk()
notebook = ttk.Notebook(root)
f0 = ttk.Frame(notebook, height=800, width=1800)
notebook.grid(row=0, column=0)
notebook.add(f0, text="MAIN")
btnfrm = ttk.Frame(f0)
btnfrm.grid(row=3, column=7, columnspan=4, rowspan=3)
# This is to create a basic rootdow
###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression 
    input_text.set(expression)
    def opertran():
        input2_text.insert(str(item), 0)
        def op3():  
        
# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""




def sci_cal():
    global expression
    expression = ""
    num = expression 
    if num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F" "(", ")", "00"]:
        value += num
        try:
            ans = str(eval(value))
        except:
            ans = "Invalid Expression"

    elif num in ["+", "-", "/", "*", ".", "1/x", "sgn("]:
        value += num

    elif num in ["asin(", "acos(", "atan(", "sin(", "cos(", "tan("]:
        value += "math." + num

    elif num == "^":
        value += "**"

    elif num == "%":
        value += "/100"
        try:
            ans = str(eval(value))
        except:
             ans = "Invalid Expression"
    elif num == "^2":
        value += "**2"
        try:
            ans = str(eval(value))
        except:
            ans = "Invalid Expression"
    elif num == "^3":
        value += "**3"
        try:
            ans = str(eval(value))
        except:
            ans = "Invalid Expression"

    elif num == "√(":
        value += "math.sqrt("

    elif num == "e":
        value += "math.e"
        try:
            ans = str(eval(value))
        except:
            ans = "Invalid Expression"
    elif num == "π":
        value += "math.pi"
        try:
            ans = str(eval(value))
        except:
            ans = "Invalid Expression"
    elif num == "log(":
        value += "math.log10("
    elif num == "ln(":
        value += "math.log("
    elif num == "e^":
        value += "math.e**"
    elif num == "A":
        value += "10"
    elif num == "B":
        value += "11"
    elif num == "C":
        value += "12"
    elif num == "D":
        value += "13"
    elif num == "E":
        value += "14"
    elif num == "F":
        value += "15"
    elif num == "1/x":
        value += "*0.1"
    elif num == "A":
        value += 10
        
##tk.Label(f0, text="1").grid(row=1, column=5)
##tk.Label(f0, text="2").grid(row=2, column=6)
##tk.Label(f0, text="3").grid(row=3, column=7)
##tk.Label(f0, text="4").grid(row=7, column=8)
##tk.Label(f0, text="5").grid(row=4, column=9)
##tk.Label(f0, text="6").grid(row=1, column=10)

efrm = ttk.Frame(f0, height=50, width=100)
efrm.grid(row=1, column=0, columnspan=3, rowspan=4)
input_text = tk.Entry(f0)
input_text.grid(row=1, column=1)
input2_text = tk.Entry(f0)
input2_text.grid(row=1, column=2)
input3_text = tk.Entry(f0)
input3_text.grid(row=1, column=3)
input4_text = tk.Entry(f0)
input4_text(row=1, column=4)
## 
## 
##clear = Button(btnfrm, text = "C", fg = "black", width = 10, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 3, column = 0, columnspan = 3, padx = 1, pady = 1)
## 
##divide = Button(btnfrm, text = "/", fg = "black", width = 1
##                , height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 3, column = 3, padx = 1, pady = 1)
## 
### second row
## 
##seven = Button(btnfrm, text = "7", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 4, column = 0, padx = 1, pady = 1)
## 
##eight = Button(btnfrm, text = "8", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 4, column = 1, padx = 1, pady = 1)
## 
##nine = Button(btnfrm, text = "9", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 4, column = 2, padx = 1, pady = 1)
## 
##multiply = Button(btnfrm, text = "*", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 4, column = 3, padx = 1, pady = 1)
## 
### third row
## 
##four = Button(btnfrm, text = "4", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 5, column = 0, padx = 1, pady = 1)
## 
##five = Button(btnfrm, text = "5", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 5, column = 1, padx = 1, pady = 1)
## 
##six = Button(btnfrm, text = "6", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 5, column = 2, padx = 1, pady = 1)
## 
##minus = Button(btnfrm, text = "-", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 5, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##one = Button(btnfrm, text = "1", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 6, column = 0, padx = 1, pady = 1)
## 
##two = Button(btnfrm, text = "2", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 6, column = 1, padx = 1, pady = 1)
## 
##three = Button(btnfrm, text = "3", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 6, column = 2, padx = 1, pady = 1)
## 
##plus = Button(btnfrm, text = "+", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 6, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##hexf = Button(btnfrm, text = "F", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 7, column = 0, columnspan = 2, padx = 1, pady = 1)
## 
##hexe = Button(btnfrm, text = "E", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 7, column = 2, padx = 1, pady = 1)
## 
##hexd = Button(btnfrm, text = "D", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 7, column = 3, padx = 1, pady = 1)
###########################################################################################
##
##
##
##
##
##hexc = Button(btnfrm, text = "C", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 8, column = 0, padx = 1, pady = 1)
## 
##hexb = Button(btnfrm, text = "B", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 8, column = 1, padx = 1, pady = 1)
## 
##hexa = Button(btnfrm, text = "A", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 8, column = 2, padx = 1, pady = 1)
## 
##multiply = Button(btnfrm, text = "*", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 3, column = 3, padx = 1, pady = 1)
### 5th row
 
seven = Button(btnfrm, text = "7", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 9, column = 3, padx = 1, pady = 1)
 
eight = Button(btnfrm, text = "8", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 9, column = 4, padx = 1, pady = 1)
 
nine = Button(btnfrm, text = "9", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 9, column = 5, padx = 1, pady = 1)
 
multiply = Button(btnfrm, text = "*", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 9, column = 6, padx = 1, pady = 1)
 
# 6th row
 
four = Button(btnfrm, text = "4", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 10, column = 3, padx = 1, pady = 1)
 
five = Button(btnfrm, text = "5", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 10, column = 4, padx = 1, pady = 1)
 
six = Button(btnfrm, text = "6", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 10, column = 5, padx = 1, pady = 1)
 
minus = Button(btnfrm, text = "-", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 10, column = 6, padx = 1, pady = 1)
 
# 8th row
 
one = Button(btnfrm, text = "1", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 11, column = 3, padx = 1, pady = 1)
 
two = Button(btnfrm, text = "2", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 11, column = 4, padx = 1, pady = 1)
 
three = Button(btnfrm, text = "3", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 11, column = 5, padx = 1, pady = 1)
 
plus = Button(btnfrm, text = "+", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 11, column = 6, padx = 1, pady = 1)
 
# 9th row
 
##zero = Button(btnfrm, text = "cos", fg = "black", width = 1, height = 1, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 12, column = 3, columnspan = 2, padx = 1, pady = 1)
## 
##point = Button(btnfrm, text = "sin", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 12, column = 4, padx = 1, pady = 1)
## 
##equals = Button(btnfrm, text = "π", fg = "black", width = 1, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 12, column = 6, padx = 1, pady = 1)
## 



f1 = ttk.Frame(notebook)
notebook.add(f1, text="Ohms Law")

















def fontfamily():
    pass


def foo():
    pass


def codeview():
    import codeview


# ------------------------------------------------
# TAB1 & 2 create
# ------------------------------------------------
f2 = ttk.Frame(notebook)

notebook.add(f2, text="Sci_Calc")


def lc():
    import scicalc


def keypad():
    import keypad


# --------------------------------------------------------
# TAB 3 - 10 Create
# ---------------------------------------------------------
f3 = ttk.Frame(notebook, height=100, width=200)
notebook.add(f3, text="Base # Converter")
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text="Resonant Freq Calc")

f5 = ttk.Frame(notebook)
notebook.add(f5, text="Resistor Calc")
f6 = ttk.Frame(notebook)
notebook.add(f6, text="dBm2W&V")
f7 = ttk.Frame(notebook)
notebook.add(f7, text="7")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f9 = ttk.Frame(notebook)
notebook.add(f9, text="9")
f10 = ttk.Frame(notebook)
notebook.add(f10, text="10")

f11 = ttk.Frame(notebook)
notebook.add(f11, text="11")


def command():
    pass


def mod1():
    import Ohms_Law_Singlecalc_v2


def mod2():
    import RPcalc


def mod3():
    import IPcalc


def mod4():
    import VPcalc


def lc_freq():
    import LC_Freq


##btn1 = tk.Button(f1, text="Ohms Law Calc", command=mod1).grid(column=0, row=3)
##btn2 = tk.Button(f1, text="Calc Resistance & Pwr", command=mod2).grid(column=0, row=4)
##btn3 = tk.Button(f1, text="Calc Current & Pwr", command=mod3).grid(column=0, row=5)
##btn4 = tk.Button(f1, text="Volts & Pwr", command=mod4).grid(column=0, row=6)
##btn5 = tk.Button(f1, text="b5", command=command).grid(column=0, row=7)
##btn6 = tk.Button(f1, text="b6", command=command).grid(column=0, row=8)
##awg_str = """  """
# --------------------------------------
#   TAB2 STUFF Sci Calc Eng, Info Label
# --------------------------------------
f2btn = tk.Button(f2, text="load calculator", bg="pink", command=lc)
f2btn.grid(row=2, column=2)
f3btn = tk.Button(f2, text="keyboard onscreen", bg="pink", command=keypad)
f3btn.grid(row=3, column=2)

##txt_str= """''tera'   : (1000000000000, 10**12),
##'giga'   : (1000000000, 10**9),
##'mega'   : (1000000, 10**6),
##'kilo'   : (1000, 10**3),
##'hecta'  : (100, 10**2),
##'deca'   : (10, 10),
##'base'   : (1,1),
##'deci'   : (0.1, 10**-1),
##'centi'  : (0.01, 10**-2),
##'milli'  : (0.001, 10**-3),
##'micro'  : (0.000001, 10**-6),
##'nano'   : (0.000000001, 10**-9)
##'pico'   : (0.000000000001, 10**-12)
##
##"""
##tk.Label(f2, text=txt_str).grid(row=3, column=3)
#
# ----------------------------------------------
#  TAB3  Number Base Converter
# ----------------------------------------------


def bin2dec():
    import FBIN

    # subprocess.run("python3", "FBIN")


def fromhex():
    import FHEX


def fromoct():
    import FOCT


def frombase():
    import DEC_2_36


def dectobin():
    import Dec2Bin


def infosec():
    import Info_Section


btn11 = tk.Button(f3, text="Decimal to Base 2 to 36", command=frombase).grid(
    column=3, row=3
)
btn22 = tk.Button(f3, text="HEX to DEC BIN OCT", command=fromhex).grid(column=3, row=4)
btn33 = tk.Button(f3, text="OCTAL TO DEC, HEX, BIN", command=fromoct).grid(
    column=3, row=5
)
btn44 = tk.Button(f3, text="BIN TO OCT, DEC, HEX", command=bin2dec).grid(
    column=3, row=6
)
btn55 = tk.Button(f3, text="DEC to BIN", command=dectobin).grid(column=3, row=7)
btn66 = tk.Button(f3, text="INFO", command=infosec).grid(column=3, row=8)
tk.Label(f3, text="Base Converter").grid(column=3, row=1)


# --------------------------------------
#   TAB4 Resonant Frequency Calc
# --------------------------------------
def lc_freq():
    import LC_Freq


def lfreq():
    import Freq_L_find_C


def cfreq():
    import Freq_C_find_L


btn77 = tk.Button(f4, text="LC Resonant Freq Calc", command=lc_freq).grid(
    column=3, row=3
)
btn78 = tk.Button(f4, text="Freq L Calc find C", command=lfreq).grid(column=3, row=4)
btn79 = tk.Button(f4, text="Freq C Calc find L", command=cfreq).grid(column=3, row=5)

if __name__ == "__main__":
    r.mainloop()
