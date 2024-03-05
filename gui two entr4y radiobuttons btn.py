import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GRadio_531 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_531["font"] = ft
        GRadio_531["fg"] = "#333333"
        GRadio_531["justify"] = "center"
        GRadio_531["text"] = "RadioButton"
        GRadio_531.place(x=440, y=30, width=85, height=25)
        GRadio_531["command"] = self.GRadio_531_command

        GRadio_122 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_122["font"] = ft
        GRadio_122["fg"] = "#333333"
        GRadio_122["justify"] = "center"
        GRadio_122["text"] = "RadioButton"
        GRadio_122.place(x=440, y=60, width=85, height=25)
        GRadio_122["command"] = self.GRadio_122_command

        GRadio_918 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_918["font"] = ft
        GRadio_918["fg"] = "#333333"
        GRadio_918["justify"] = "center"
        GRadio_918["text"] = "RadioButton"
        GRadio_918.place(x=440, y=90, width=85, height=25)
        GRadio_918["command"] = self.GRadio_918_command

        GLineEdit_207 = tk.Entry(root)
        GLineEdit_207["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_207["font"] = ft
        GLineEdit_207["fg"] = "#333333"
        GLineEdit_207["justify"] = "center"
        GLineEdit_207["text"] = "Entry"
        GLineEdit_207.place(x=50, y=30, width=70, height=25)

        GLineEdit_430 = tk.Entry(root)
        GLineEdit_430["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_430["font"] = ft
        GLineEdit_430["fg"] = "#333333"
        GLineEdit_430["justify"] = "center"
        GLineEdit_430["text"] = "Entry"
        GLineEdit_430.place(x=140, y=30, width=70, height=25)

        GButton_398 = tk.Button(root)
        GButton_398["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_398["font"] = ft
        GButton_398["fg"] = "#273134"
        GButton_398["justify"] = "center"
        GButton_398["text"] = "Button"
        GButton_398.place(x=50, y=60, width=70, height=25)
        GButton_398["command"] = self.GButton_398_command

        GButton_615 = tk.Button(root)
        GButton_615["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_615["font"] = ft
        GButton_615["fg"] = "#273134"
        GButton_615["justify"] = "center"
        GButton_615["text"] = "Button"
        GButton_615.place(x=140, y=60, width=70, height=25)
        GButton_615["command"] = self.GButton_615_command

    def GRadio_531_command(self):
        print("command")

    def GRadio_122_command(self):
        print("command")

    def GRadio_918_command(self):
        print("command")

    def GButton_398_command(self):
        print("command")

    def GButton_615_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
