import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 715
        height = 655
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

        GListBox_800 = tk.Listbox(root)
        GListBox_800["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_800["font"] = ft
        GListBox_800["fg"] = "#333333"
        GListBox_800["justify"] = "center"
        GListBox_800.place(x=80, y=30, width=179, height=435)

        GLineEdit_582 = tk.Entry(root)
        GLineEdit_582["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_582["font"] = ft
        GLineEdit_582["fg"] = "#333333"
        GLineEdit_582["justify"] = "center"
        GLineEdit_582["text"] = "Entry"
        GLineEdit_582.place(x=80, y=470, width=416, height=34)

        GButton_553 = tk.Button(root)
        GButton_553["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_553["font"] = ft
        GButton_553["fg"] = "#273134"
        GButton_553["justify"] = "center"
        GButton_553["text"] = "Button"
        GButton_553.place(x=0, y=10, width=70, height=25)
        GButton_553["command"] = self.GButton_553_command

        GButton_679 = tk.Button(root)
        GButton_679["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_679["font"] = ft
        GButton_679["fg"] = "#273134"
        GButton_679["justify"] = "center"
        GButton_679["text"] = "Button"
        GButton_679.place(x=0, y=40, width=70, height=25)
        GButton_679["command"] = self.GButton_679_command

        GButton_82 = tk.Button(root)
        GButton_82["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_82["font"] = ft
        GButton_82["fg"] = "#273134"
        GButton_82["justify"] = "center"
        GButton_82["text"] = "Button"
        GButton_82.place(x=0, y=70, width=70, height=25)
        GButton_82["command"] = self.GButton_82_command

        GButton_441 = tk.Button(root)
        GButton_441["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_441["font"] = ft
        GButton_441["fg"] = "#273134"
        GButton_441["justify"] = "center"
        GButton_441["text"] = "Button"
        GButton_441.place(x=0, y=100, width=70, height=25)
        GButton_441["command"] = self.GButton_441_command

        GButton_922 = tk.Button(root)
        GButton_922["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_922["font"] = ft
        GButton_922["fg"] = "#273134"
        GButton_922["justify"] = "center"
        GButton_922["text"] = "Button"
        GButton_922.place(x=0, y=130, width=70, height=25)
        GButton_922["command"] = self.GButton_922_command

        GButton_506 = tk.Button(root)
        GButton_506["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_506["font"] = ft
        GButton_506["fg"] = "#273134"
        GButton_506["justify"] = "center"
        GButton_506["text"] = "Button"
        GButton_506.place(x=0, y=160, width=70, height=25)
        GButton_506["command"] = self.GButton_506_command

        GButton_995 = tk.Button(root)
        GButton_995["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_995["font"] = ft
        GButton_995["fg"] = "#273134"
        GButton_995["justify"] = "center"
        GButton_995["text"] = "Button"
        GButton_995.place(x=0, y=190, width=70, height=25)
        GButton_995["command"] = self.GButton_995_command

        GButton_570 = tk.Button(root)
        GButton_570["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#273134"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Button"
        GButton_570.place(x=0, y=220, width=70, height=25)
        GButton_570["command"] = self.GButton_570_command

        GButton_172 = tk.Button(root)
        GButton_172["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_172["font"] = ft
        GButton_172["fg"] = "#273134"
        GButton_172["justify"] = "center"
        GButton_172["text"] = "Button"
        GButton_172.place(x=0, y=250, width=70, height=25)
        GButton_172["command"] = self.GButton_172_command

        GButton_653 = tk.Button(root)
        GButton_653["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_653["font"] = ft
        GButton_653["fg"] = "#273134"
        GButton_653["justify"] = "center"
        GButton_653["text"] = "Button"
        GButton_653.place(x=0, y=280, width=70, height=25)
        GButton_653["command"] = self.GButton_653_command

        GButton_93 = tk.Button(root)
        GButton_93["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_93["font"] = ft
        GButton_93["fg"] = "#273134"
        GButton_93["justify"] = "center"
        GButton_93["text"] = "Button"
        GButton_93.place(x=0, y=310, width=70, height=25)
        GButton_93["command"] = self.GButton_93_command

        GButton_518 = tk.Button(root)
        GButton_518["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_518["font"] = ft
        GButton_518["fg"] = "#273134"
        GButton_518["justify"] = "center"
        GButton_518["text"] = "Button"
        GButton_518.place(x=0, y=340, width=70, height=25)
        GButton_518["command"] = self.GButton_518_command

        GButton_62 = tk.Button(root)
        GButton_62["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_62["font"] = ft
        GButton_62["fg"] = "#273134"
        GButton_62["justify"] = "center"
        GButton_62["text"] = "Button"
        GButton_62.place(x=0, y=370, width=70, height=25)
        GButton_62["command"] = self.GButton_62_command

        GButton_159 = tk.Button(root)
        GButton_159["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_159["font"] = ft
        GButton_159["fg"] = "#273134"
        GButton_159["justify"] = "center"
        GButton_159["text"] = "Button"
        GButton_159.place(x=0, y=400, width=70, height=25)
        GButton_159["command"] = self.GButton_159_command

        GMessage_944 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_944["font"] = ft
        GMessage_944["fg"] = "#333333"
        GMessage_944["justify"] = "center"
        GMessage_944["text"] = "Message"
        GMessage_944.place(x=280, y=40, width=417, height=30)

        GMessage_761 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_761["font"] = ft
        GMessage_761["fg"] = "#333333"
        GMessage_761["justify"] = "center"
        GMessage_761["text"] = "Message"
        GMessage_761.place(x=330, y=170, width=340, height=176)

        GMessage_945 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_945["font"] = ft
        GMessage_945["fg"] = "#333333"
        GMessage_945["justify"] = "center"
        GMessage_945["text"] = "Message"
        GMessage_945.place(x=170, y=530, width=226, height=77)

        GButton_558 = tk.Button(root)
        GButton_558["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_558["font"] = ft
        GButton_558["fg"] = "#273134"
        GButton_558["justify"] = "center"
        GButton_558["text"] = "Button"
        GButton_558.place(x=0, y=590, width=70, height=25)
        GButton_558["command"] = self.GButton_558_command

        GButton_919 = tk.Button(root)
        GButton_919["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_919["font"] = ft
        GButton_919["fg"] = "#273134"
        GButton_919["justify"] = "center"
        GButton_919["text"] = "Button"
        GButton_919.place(x=0, y=500, width=70, height=25)
        GButton_919["command"] = self.GButton_919_command

        GButton_992 = tk.Button(root)
        GButton_992["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_992["font"] = ft
        GButton_992["fg"] = "#273134"
        GButton_992["justify"] = "center"
        GButton_992["text"] = "Button"
        GButton_992.place(x=0, y=530, width=70, height=25)
        GButton_992["command"] = self.GButton_992_command

        GButton_104 = tk.Button(root)
        GButton_104["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_104["font"] = ft
        GButton_104["fg"] = "#273134"
        GButton_104["justify"] = "center"
        GButton_104["text"] = "Button"
        GButton_104.place(x=0, y=560, width=70, height=25)
        GButton_104["command"] = self.GButton_104_command

        GButton_227 = tk.Button(root)
        GButton_227["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_227["font"] = ft
        GButton_227["fg"] = "#273134"
        GButton_227["justify"] = "center"
        GButton_227["text"] = "Button"
        GButton_227.place(x=630, y=610, width=70, height=25)
        GButton_227["command"] = self.GButton_227_command

        GButton_251 = tk.Button(root)
        GButton_251["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_251["font"] = ft
        GButton_251["fg"] = "#273134"
        GButton_251["justify"] = "center"
        GButton_251["text"] = "Button"
        GButton_251.place(x=550, y=610, width=70, height=25)
        GButton_251["command"] = self.GButton_251_command

    def GButton_553_command(self):
        print("command")

    def GButton_679_command(self):
        print("command")

    def GButton_82_command(self):
        print("command")

    def GButton_441_command(self):
        print("command")

    def GButton_922_command(self):
        print("command")

    def GButton_506_command(self):
        print("command")

    def GButton_995_command(self):
        print("command")

    def GButton_570_command(self):
        print("command")

    def GButton_172_command(self):
        print("command")

    def GButton_653_command(self):
        print("command")

    def GButton_93_command(self):
        print("command")

    def GButton_518_command(self):
        print("command")

    def GButton_62_command(self):
        print("command")

    def GButton_159_command(self):
        print("command")

    def GButton_558_command(self):
        print("command")

    def GButton_919_command(self):
        print("command")

    def GButton_992_command(self):
        print("command")

    def GButton_104_command(self):
        print("command")

    def GButton_227_command(self):
        print("command")

    def GButton_251_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
