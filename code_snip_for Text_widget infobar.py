import tkinter

master = tkinter.Tk()

labelframe = tkinter.LabelFrame(master, labelanchor="s")
labelframe.grid(row=0, column=0, sticky="nsew")

text = tkinter.Text(labelframe, width=80, height=24)
text.grid(row=0, column=0, sticky="nsew")


def rowcol(ev=None):
    r, c = text.index("insert").split(".")
    labelframe["text"] = f"{r} | {c}"


text.event_add(
    "<<REACT>>", *("<Motion>", "<ButtonRelease>", "<KeyPress>", "<KeyRelease>")
)
b = text.bind("<<REACT>>", rowcol)
rowcol()  # get the ball rolling
text.focus()

master.mainloop()
