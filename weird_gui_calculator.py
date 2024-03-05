# Calculator
import math
from tkinter import *

w = Tk()
w.geometry("500x500")
w.title("Calculatorax")
w.configure(bg="#03befc")

# Functions(Keypad)
def calc1():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn1["text"]
    txt1.insert(0, b1)


def calc2():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn2["text"]
    txt1.insert(0, b1)


def calc3():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn3["text"]
    txt1.insert(0, b1)


def calc4():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn4["text"]
    txt1.insert(0, b1)


def calc5():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn5["text"]
    txt1.insert(0, b1)


def calc6():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn6["text"]
    txt1.insert(0, b1)


def calc7():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn7["text"]
    txt1.insert(0, b1)


def calc8():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn8["text"]
    txt1.insert(0, b1)


def calc9():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn9["text"]
    txt1.insert(0, b1)


def calc0():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn0["text"]
    txt1.insert(0, b1)


# Functions(operators)

x = 0


def add():
    global x
    add.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 1


def subtract():
    global x
    subtract.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 2


def get():
    b = txt1.get()


def equals():
    global x
    if x == 1:
        c = (eval(txt1.get())) + add.b
        cls()
        txt1.insert(0, c)

    elif x == 2:
        c = subtract.b - (eval(txt1.get()))
        cls()
        txt1.insert(0, c)

    elif x == 3:
        c = multiply.b * (eval(txt1.get()))
        cls()
        txt1.insert(0, c)
    elif x == 4:
        c = divide.b
        cls()
        txt1.insert(0, c)


def cls():
    global x
    x = 0
    txt1.delete(0, END)


def multiply():
    global x
    multiply.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 3


def divide():
    global x
    divide.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 4


def sin():
    global x
    math.sin(eval(txt1.get()))


fr = Frame(w)
fr.grid(row=7, column=1)


# Labels

lbl1 = Label(
    w, text="JH Calc", font=("Times New Roman", 35), fg="#232226", bg="#fc9d03"
)

# Entryboxes
txt1 = Entry(w, width=10, font=30)

# Buttons

btn1 = Button(fr, text="1", font=("Unispace", 25), command=calc1, bg="#c3c6d9")
btn2 = Button(fr, text="2", font=("Unispace", 25), command=calc2, bg="#c3c6d9")
btn3 = Button(fr, text="3", font=("Unispace", 25), command=calc3, bg="#c3c6d9")
btn4 = Button(fr, text="4", font=("Unispace", 25), command=calc4, bg="#c3c6d9")
btn5 = Button(fr, text="5", font=("Unispace", 25), command=calc5, bg="#c3c6d9")
btn6 = Button(fr, text="6", font=("Unispace", 25), command=calc6, bg="#c3c6d9")
btn7 = Button(fr, text="7", font=("Unispace", 25), command=calc7, bg="#c3c6d9")
btn8 = Button(fr, text="8", font=("Unispace", 25), command=calc8, bg="#c3c6d9")
btn9 = Button(fr, text="9", font=("Unispace", 25), command=calc9, bg="#c3c6d9")
btn0 = Button(fr, text="0", font=("Unispace", 25), command=calc0, bg="#c3c6d9")

btn_addition = Button(fr, text="+", font=("Unispace", 26), command=add, bg="#3954ed")
btn_equals = Button(
    fr,
    text="ANS",
    font=(
        "Unispace",
        24,
    ),
    command=equals,
    bg="#e876e6",
)
btn_clear = Button(
    fr,
    text="Clear",
    font=(
        "Unispace",
        24,
    ),
    command=cls,
    bg="#e876e6",
)
btn_subtract = Button(
    fr, text="-", font=("Unispace", 26), command=subtract, bg="#3954ed"
)
btn_multiplication = Button(
    fr, text="x", font=("Unispace", 26), command=multiply, bg="#3954ed"
)
btn_division = Button(fr, text="÷", font=("Unispace", 26), command=divide, bg="#3954ed")

# grid(row=1, column=1)ments(Labels)

lbl1.grid(row=1, column=4)

# grid(row=1, column=1)ments(entrybox)

txt1.grid(row=1, column=2)

# grid(row=1, column=1)ments(Buttons)
btn1.grid(row=10, column=1)
btn2.grid(row=10, column=2)
btn3.grid(row=10, column=3)
btn4.grid(row=9, column=1)
btn5.grid(row=9, column=2)
btn6.grid(row=9, column=3)
btn7.grid(row=8, column=1)
btn8.grid(row=8, column=2)
btn9.grid(row=8, column=3)
btn0.grid(row=11, column=2)

btn_addition.grid(row=10, column=4)
btn_equals.grid(row=12, column=4)
btn_clear.grid(row=11, column=4)
btn_subtract.grid(row=9, column=4)
btn_multiplication.grid(row=8, column=4)
btn_division.grid(row=8, column=4)

w.mainloop()
