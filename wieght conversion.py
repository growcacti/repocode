from tkinter import *

# Creating a GUI root
root = Tk()


def from_kg():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


e1 = Label(root, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
e3 = Label(root, text="Gram")
e4 = Label(root, text="Pound")
e5 = Label(root, text="Ounce")

t1 = Text(root, height=5, width=30)
t2 = Text(root, height=5, width=30)
t3 = Text(root, height=5, width=30)

b1 = Button(root, text="Convert", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

root.mainloop()
