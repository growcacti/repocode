from tkinter import *


class AppetiserClass:
    meal1 = 0
    root = Tk()
    app = Frame(self.root)

    def __init__(self):
        self.root.title("Appetiser Page")
        self.root.geometry("1920x1080")

        self.app.grid()

        Label(self.app, text="", width=75, height=20).grid(row=1, column=0, sticky=N)

        self.DisplayButton = Button(self.app, text=self.meal1)
        self.DisplayButton.grid(column=1, row=2, sticky=W)
        self.DisplayButton.config(height=10, width=10)

        self.Plus1Button = Button(self.app, text="+1", command=self.plus1, bg="green")
        self.Plus1Button.grid(column=2, row=2, sticky=W)
        self.Plus1Button.config(height=10, width=10)

        self.Neg1Button = Button(self.app, text="-1", command=self.neg1, bg="green")
        self.Neg1Button.grid(column=3, row=2, sticky=W)
        self.Neg1Button.config(height=10, width=10)

        self.root.mainloop()

    def plus1(self):
        self.meal1 += 1
        self.DisplayButton["text"] = str(self.meal1)

    def neg1(self):
        self.meal1 -= 1
        self.DisplayButton["text"] = str(self.meal1)


if __name__ == "__main__":
    AppetiserClass()
