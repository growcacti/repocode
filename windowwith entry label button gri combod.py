from tkinter import *
from tkinter.ttk import *
window = Tk()

window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello")
window.geometry('350x200')
lbl.grid(column=0, row=0)

window.mainloop()
# big and bold
lbl = Label(window, text="Hello", font=("Arial Bold", 50))








window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item

combo.grid(column=0, row=0)

window.mainloop()

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=0)
#chk_state = IntVar()

#chk_state.set(0) #uncheck

#chk_state.set(1) #check
from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

rad1 = Radiobutton(window,text='First', value=1)

rad2 = Radiobutton(window,text='Second', value=2)

rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

window.mainloop()
window.mainloop()
