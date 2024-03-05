from tkinter import *

root = Tk()
canvas = Canvas(root)
canvas.grid(row=1, column=1)
canvas.config(width = 700 , height = 800)

line = canvas.create_line(40,70, 79,140 , fill ='red', width = 7)

root.mainloop()
