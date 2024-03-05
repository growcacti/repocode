import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1231
        height = 626
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

        GListBox_669 = tk.Listbox(root)
        GListBox_669["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_669["font"] = ft
        GListBox_669["fg"] = "#333333"
        GListBox_669["justify"] = "center"
        GListBox_669.place(x=230, y=100, width=197, height=378)

        GButton_940 = tk.Button(root)
        GButton_940["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#273134"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Button"
        GButton_940.place(x=30, y=100, width=70, height=25)
        GButton_940["command"] = self.GButton_940_command

        GButton_472 = tk.Button(root)
        GButton_472["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_472["font"] = ft
        GButton_472["fg"] = "#273134"
        GButton_472["justify"] = "center"
        GButton_472["text"] = "Button"
        GButton_472.place(x=30, y=130, width=70, height=25)
        GButton_472["command"] = self.GButton_472_command

        GButton_205 = tk.Button(root)
        GButton_205["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_205["font"] = ft
        GButton_205["fg"] = "#273134"
        GButton_205["justify"] = "center"
        GButton_205["text"] = "Button"
        GButton_205.place(x=30, y=160, width=70, height=25)
        GButton_205["command"] = self.GButton_205_command

        GButton_751 = tk.Button(root)
        GButton_751["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_751["font"] = ft
        GButton_751["fg"] = "#273134"
        GButton_751["justify"] = "center"
        GButton_751["text"] = "Button"
        GButton_751.place(x=30, y=190, width=70, height=25)
        GButton_751["command"] = self.GButton_751_command

        GButton_705 = tk.Button(root)
        GButton_705["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_705["font"] = ft
        GButton_705["fg"] = "#273134"
        GButton_705["justify"] = "center"
        GButton_705["text"] = "Button"
        GButton_705.place(x=30, y=220, width=70, height=25)
        GButton_705["command"] = self.GButton_705_command

        GButton_182 = tk.Button(root)
        GButton_182["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_182["font"] = ft
        GButton_182["fg"] = "#273134"
        GButton_182["justify"] = "center"
        GButton_182["text"] = "Button"
        GButton_182.place(x=30, y=250, width=70, height=25)
        GButton_182["command"] = self.GButton_182_command

        GButton_304 = tk.Button(root)
        GButton_304["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_304["font"] = ft
        GButton_304["fg"] = "#273134"
        GButton_304["justify"] = "center"
        GButton_304["text"] = "Button"
        GButton_304.place(x=30, y=280, width=70, height=25)
        GButton_304["command"] = self.GButton_304_command

        GListBox_718 = tk.Listbox(root)
        GListBox_718["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_718["font"] = ft
        GListBox_718["fg"] = "#333333"
        GListBox_718["justify"] = "center"
        GListBox_718.place(x=470, y=110, width=219, height=388)

        GButton_229 = tk.Button(root)
        GButton_229["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_229["font"] = ft
        GButton_229["fg"] = "#273134"
        GButton_229["justify"] = "center"
        GButton_229["text"] = "Button"
        GButton_229.place(x=30, y=310, width=70, height=25)
        GButton_229["command"] = self.GButton_229_command

        GButton_588 = tk.Button(root)
        GButton_588["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_588["font"] = ft
        GButton_588["fg"] = "#273134"
        GButton_588["justify"] = "center"
        GButton_588["text"] = "Button"
        GButton_588.place(x=30, y=340, width=70, height=25)
        GButton_588["command"] = self.GButton_588_command

        GButton_449 = tk.Button(root)
        GButton_449["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_449["font"] = ft
        GButton_449["fg"] = "#273134"
        GButton_449["justify"] = "center"
        GButton_449["text"] = "Button"
        GButton_449.place(x=30, y=370, width=70, height=25)
        GButton_449["command"] = self.GButton_449_command

        GLabel_534 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "label"
        GLabel_534.place(x=270, y=50, width=70, height=25)

        GLabel_64 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_64["font"] = ft
        GLabel_64["fg"] = "#333333"
        GLabel_64["justify"] = "center"
        GLabel_64["text"] = "label"
        GLabel_64.place(x=530, y=50, width=70, height=25)

    def GButton_940_command(self):
        print("command")

    def GButton_472_command(self):
        print("command")

    def GButton_205_command(self):
        print("command")

    def GButton_751_command(self):
        print("command")

    def GButton_705_command(self):
        print("command")

    def GButton_182_command(self):
        print("command")

    def GButton_304_command(self):
        print("command")

    def GButton_229_command(self):
        print("command")

    def GButton_588_command(self):
        print("command")

    def GButton_449_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
