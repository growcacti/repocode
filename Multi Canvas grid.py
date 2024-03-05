import tkinter as tk
from tkinter import ttk

from tkinter import *

root = tk.Tk()
frm = ttk.Frame(root, height=400, width=500)
frm.grid(row=0, column=0)
canvas = tk.Canvas(root, bg="wheat")
canvas.grid(row=1, column=1)
canvas.config(width = 200 , height = 300)
canvas2 = Canvas(root, bg="green")
canvas2.grid(row=5, column=0)
line = canvas.create_line(60,160, 140,60 , fill ='red', width = 7)
line = canvas.create_line(60,160, 150,230 , fill ='red', width = 7)
canvas2.config(width = 10 , height = 10)
line = canvas.create_line(60,60, 60,240 , fill ='red', width = 7)

line = canvas.create_line(0,160, 60,160 , fill ='black', width = 8)
line = canvas.create_line(140,200, 150,230 , fill ='red', width = 10)
line = canvas.create_line(150,230, 100,220 , fill ='red', width = 10)
def create_circle(x, y, r, canvas): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, width = 7)

create_circle(100, 150, 100, canvas)










##canvas3 = Canvas(root bg="red")
##canvas3.grid(row=6, column=3)
##canvas3.config(width = 10 , height = 10)
##
##canvas4 = Canvas(root  bg="wheat")
##canvas4.grid(row=8, column=2)
##canvas4.config(width = 10, height = 10)


root.mainloop()
