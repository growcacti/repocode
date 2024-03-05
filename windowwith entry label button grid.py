from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello")
window.geometry('350x200')
lbl.grid(column=0, row=0)

window.mainloop()
# big and bold
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

