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

        GLabel_652 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_652["font"] = ft
        GLabel_652["fg"] = "#333333"
        GLabel_652["justify"] = "center"
        GLabel_652["text"] = "label"
        GLabel_652.place(x=70, y=30, width=70, height=25)

        GLabel_148 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_148["font"] = ft
        GLabel_148["fg"] = "#333333"
        GLabel_148["justify"] = "center"
        GLabel_148["text"] = "label"
        GLabel_148.place(x=160, y=30, width=70, height=25)

        GLabel_158 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_158["font"] = ft
        GLabel_158["fg"] = "#333333"
        GLabel_158["justify"] = "center"
        GLabel_158["text"] = "label"
        GLabel_158.place(x=260, y=30, width=70, height=25)

        GLabel_373 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_373["font"] = ft
        GLabel_373["fg"] = "#333333"
        GLabel_373["justify"] = "center"
        GLabel_373["text"] = "label"
        GLabel_373.place(x=340, y=30, width=70, height=25)

        GLineEdit_70 = tk.Entry(root)
        GLineEdit_70["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_70["font"] = ft
        GLineEdit_70["fg"] = "#333333"
        GLineEdit_70["justify"] = "center"
        GLineEdit_70["text"] = "Entry"
        GLineEdit_70.place(x=70, y=80, width=70, height=25)

        GLineEdit_910 = tk.Entry(root)
        GLineEdit_910["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_910["font"] = ft
        GLineEdit_910["fg"] = "#333333"
        GLineEdit_910["justify"] = "center"
        GLineEdit_910["text"] = "Entry"
        GLineEdit_910.place(x=160, y=80, width=70, height=25)

        GLineEdit_708 = tk.Entry(root)
        GLineEdit_708["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_708["font"] = ft
        GLineEdit_708["fg"] = "#333333"
        GLineEdit_708["justify"] = "center"
        GLineEdit_708["text"] = "Entry"
        GLineEdit_708.place(x=250, y=80, width=70, height=25)

        GLineEdit_911 = tk.Entry(root)
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "center"
        GLineEdit_911["text"] = "Entry"
        GLineEdit_911.place(x=340, y=80, width=70, height=25)

        GMessage_70 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_70["font"] = ft
        GMessage_70["fg"] = "#333333"
        GMessage_70["justify"] = "center"
        GMessage_70["text"] = "Message"
        GMessage_70.place(x=70, y=140, width=338, height=35)

        GLineEdit_712 = tk.Entry(root)
        GLineEdit_712["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_712["font"] = ft
        GLineEdit_712["fg"] = "#333333"
        GLineEdit_712["justify"] = "center"
        GLineEdit_712["text"] = "Entry"
        GLineEdit_712.place(x=70, y=210, width=70, height=25)

        GLineEdit_378 = tk.Entry(root)
        GLineEdit_378["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_378["font"] = ft
        GLineEdit_378["fg"] = "#333333"
        GLineEdit_378["justify"] = "center"
        GLineEdit_378["text"] = "Entry"
        GLineEdit_378.place(x=160, y=210, width=70, height=25)

        GLineEdit_107 = tk.Entry(root)
        GLineEdit_107["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_107["font"] = ft
        GLineEdit_107["fg"] = "#333333"
        GLineEdit_107["justify"] = "center"
        GLineEdit_107["text"] = "Entry"
        GLineEdit_107.place(x=70, y=260, width=70, height=25)

        GLineEdit_620 = tk.Entry(root)
        GLineEdit_620["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_620["font"] = ft
        GLineEdit_620["fg"] = "#333333"
        GLineEdit_620["justify"] = "center"
        GLineEdit_620["text"] = "Entry"
        GLineEdit_620.place(x=160, y=260, width=70, height=25)

        GLabel_477 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_477["font"] = ft
        GLabel_477["fg"] = "#333333"
        GLabel_477["justify"] = "center"
        GLabel_477["text"] = "label"
        GLabel_477.place(x=70, y=170, width=70, height=25)

        GLabel_870 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_870["font"] = ft
        GLabel_870["fg"] = "#333333"
        GLabel_870["justify"] = "center"
        GLabel_870["text"] = "label"
        GLabel_870.place(x=160, y=170, width=70, height=25)

        GLabel_63 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#333333"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = "label"
        GLabel_63.place(x=70, y=310, width=70, height=25)

        GLabel_224 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_224["font"] = ft
        GLabel_224["fg"] = "#333333"
        GLabel_224["justify"] = "center"
        GLabel_224["text"] = "label"
        GLabel_224.place(x=160, y=310, width=70, height=25)

        GButton_478 = tk.Button(root)
        GButton_478["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_478["font"] = ft
        GButton_478["fg"] = "#273134"
        GButton_478["justify"] = "center"
        GButton_478["text"] = "Button"
        GButton_478.place(x=70, y=360, width=70, height=25)
        GButton_478["command"] = self.GButton_478_command

        GButton_383 = tk.Button(root)
        GButton_383["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_383["font"] = ft
        GButton_383["fg"] = "#273134"
        GButton_383["justify"] = "center"
        GButton_383["text"] = "Button"
        GButton_383.place(x=70, y=400, width=70, height=25)
        GButton_383["command"] = self.GButton_383_command

        GButton_47 = tk.Button(root)
        GButton_47["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_47["font"] = ft
        GButton_47["fg"] = "#273134"
        GButton_47["justify"] = "center"
        GButton_47["text"] = "Button"
        GButton_47.place(x=160, y=360, width=70, height=25)
        GButton_47["command"] = self.GButton_47_command

        GButton_272 = tk.Button(root)
        GButton_272["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_272["font"] = ft
        GButton_272["fg"] = "#273134"
        GButton_272["justify"] = "center"
        GButton_272["text"] = "Button"
        GButton_272.place(x=160, y=400, width=70, height=25)
        GButton_272["command"] = self.GButton_272_command

        GButton_880 = tk.Button(root)
        GButton_880["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_880["font"] = ft
        GButton_880["fg"] = "#273134"
        GButton_880["justify"] = "center"
        GButton_880["text"] = "Button"
        GButton_880.place(x=70, y=440, width=70, height=25)
        GButton_880["command"] = self.GButton_880_command

        GButton_745 = tk.Button(root)
        GButton_745["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_745["font"] = ft
        GButton_745["fg"] = "#273134"
        GButton_745["justify"] = "center"
        GButton_745["text"] = "Button"
        GButton_745.place(x=160, y=440, width=70, height=25)
        GButton_745["command"] = self.GButton_745_command

        GButton_81 = tk.Button(root)
        GButton_81["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_81["font"] = ft
        GButton_81["fg"] = "#273134"
        GButton_81["justify"] = "center"
        GButton_81["text"] = "Button"
        GButton_81.place(x=490, y=40, width=70, height=25)
        GButton_81["command"] = self.GButton_81_command

        GButton_522 = tk.Button(root)
        GButton_522["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#273134"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "Button"
        GButton_522.place(x=490, y=80, width=70, height=25)
        GButton_522["command"] = self.GButton_522_command

        GButton_595 = tk.Button(root)
        GButton_595["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_595["font"] = ft
        GButton_595["fg"] = "#273134"
        GButton_595["justify"] = "center"
        GButton_595["text"] = "Button"
        GButton_595.place(x=490, y=120, width=70, height=25)
        GButton_595["command"] = self.GButton_595_command

        GButton_694 = tk.Button(root)
        GButton_694["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_694["font"] = ft
        GButton_694["fg"] = "#273134"
        GButton_694["justify"] = "center"
        GButton_694["text"] = "Button"
        GButton_694.place(x=490, y=160, width=70, height=25)
        GButton_694["command"] = self.GButton_694_command

        GButton_5 = tk.Button(root)
        GButton_5["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_5["font"] = ft
        GButton_5["fg"] = "#273134"
        GButton_5["justify"] = "center"
        GButton_5["text"] = "Button"
        GButton_5.place(x=490, y=200, width=70, height=25)
        GButton_5["command"] = self.GButton_5_command

        GButton_909 = tk.Button(root)
        GButton_909["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_909["font"] = ft
        GButton_909["fg"] = "#273134"
        GButton_909["justify"] = "center"
        GButton_909["text"] = "Button"
        GButton_909.place(x=490, y=240, width=70, height=25)
        GButton_909["command"] = self.GButton_909_command

        GButton_566 = tk.Button(root)
        GButton_566["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_566["font"] = ft
        GButton_566["fg"] = "#273134"
        GButton_566["justify"] = "center"
        GButton_566["text"] = "Button"
        GButton_566.place(x=490, y=280, width=70, height=25)
        GButton_566["command"] = self.GButton_566_command

        GButton_231 = tk.Button(root)
        GButton_231["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_231["font"] = ft
        GButton_231["fg"] = "#273134"
        GButton_231["justify"] = "center"
        GButton_231["text"] = "Button"
        GButton_231.place(x=490, y=320, width=70, height=25)
        GButton_231["command"] = self.GButton_231_command

        GButton_207 = tk.Button(root)
        GButton_207["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#273134"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "Button"
        GButton_207.place(x=490, y=360, width=70, height=25)
        GButton_207["command"] = self.GButton_207_command

        GButton_872 = tk.Button(root)
        GButton_872["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_872["font"] = ft
        GButton_872["fg"] = "#273134"
        GButton_872["justify"] = "center"
        GButton_872["text"] = "Button"
        GButton_872.place(x=490, y=400, width=70, height=25)
        GButton_872["command"] = self.GButton_872_command

    def GButton_478_command(self):
        print("command")

    def GButton_383_command(self):
        print("command")

    def GButton_47_command(self):
        print("command")

    def GButton_272_command(self):
        print("command")

    def GButton_880_command(self):
        print("command")

    def GButton_745_command(self):
        print("command")

    def GButton_81_command(self):
        print("command")

    def GButton_522_command(self):
        print("command")

    def GButton_595_command(self):
        print("command")

    def GButton_694_command(self):
        print("command")

    def GButton_5_command(self):
        print("command")

    def GButton_909_command(self):
        print("command")

    def GButton_566_command(self):
        print("command")

    def GButton_231_command(self):
        print("command")

    def GButton_207_command(self):
        print("command")

    def GButton_872_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
