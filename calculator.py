import tkinter as Tk
from tkinter import *

root_var = Tk()
root_var.title("Calculator")

e = Entry(root_var, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number=None):

#e.delete(0, END)
current = e.get()
e.delete(0, END)
e.insert(0, str(current) + str(number) )

def button_clear():
e.delete(0, END)


def button_add():
first_number = e.get()
global f_num
f_num = int(first_number)
e.delete(0, END)


def button_subtract():
second_number = e.get()
e.delete(0, END)
e.insert(0, f_num + int(second_number))


def button_multiply():
third_number = e.get()
e.delete(0, END)
e.insert(0, f_num + int(third_number))



def button_divide():
fourth_number = e.get()
e.delete(0, END)
e.insert(0, f_num + int(fourth_number))



def button_exponents():
fifth_number = e.get()
e.delete(0, END)
e.insert(0, f_num + int(fifth_number))

def button_equal():
sixth_number = e.get()
e.delete(0, END)
e.insert(0, f_num + int(sixth_number))

 button_1 = Button(root_var, text="1", padx=50, pady=10, command=lambda: button_click(1))
 button_2 = Button(root_var, text="2", padx=50, pady=10, command=lambda: button_click(2))
 button_3 = Button(root_var, text="3", padx=50, pady=10, command=lambda: button_click(3))
 button_4 = Button(root_var, text="4", padx=50, pady=10, command=lambda: button_click(4))
 button_5 = Button(root_var, text="5", padx=50, pady=10, command=lambda: button_click(5))
 button_6 = Button(root_var, text="6", padx=50, pady=10, command=lambda: button_click(6))
 button_7 = Button(root_var, text="7", padx=50, pady=10, command=lambda: button_click(7))
 button_8 = Button(root_var, text="8", padx=50, pady=10, command=lambda: button_click(8))
 button_9 = Button(root_var, text="9", padx=50, pady=10, command=lambda: button_click(9))
 button_0 = Button(root_var, text="0", padx=50, pady=10, command=lambda: button_click(0))

 button_addition = Button(root_var, text="+", padx=50, pady=10, command=button_add)
 button_subtraction = Button(root_var, text="-", padx=50, pady=10, command=button_subtract)
 button_multiplication = Button(root_var, text="*", padx=50, pady=10, command=button_multiply)
 button_division = Button(root_var, text="/", padx=50, pady=10, command=button_divide)
 button_exponents = Button(root_var, text="^", padx=50, pady=10, command=button_exponents)

 button_equals = Button(root_var, text="=", padx=50, pady=10, command=button_equal)

 button_clear = Button(root_var, text="C", padx=50, pady=10, command=button_clear)

  button_1.grid(row=3, column=2)
  button_2.grid(row=3, column=1)
  button_3.grid(row=3, column=0)

  button_4.grid(row=2, column=2)
  button_5.grid(row=2, column=1)
  button_6.grid(row=2, column=0)

  button_7.grid(row=1, column=2)
  button_8.grid(row=1, column=1)
  button_9.grid(row=1, column=0)

  button_0.grid(row=4, column=0)
  button_addition.grid(row=4, column=1)
  button_subtraction.grid(row=4, column=2)

  button_multiplication.grid(row=5, column=0)
  button_division.grid(row=5, column=1)
  button_exponents.grid(row=5, column=2)

  button_equals.grid(row=6, column=0)
  button_clear.grid(row=6, column=1)


  root_var.mainloop()
