import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1176
        height = 714
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

        GLineEdit_405 = tk.Entry(root)
        GLineEdit_405["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_405["font"] = ft
        GLineEdit_405["fg"] = "#333333"
        GLineEdit_405["justify"] = "center"
        GLineEdit_405["text"] = "Entry"
        GLineEdit_405.place(x=110, y=60, width=174, height=30)

        GLabel_4 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#333333"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "label"
        GLabel_4.place(x=110, y=20, width=70, height=25)

        GListBox_775 = tk.Listbox(root)
        GListBox_775["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_775["font"] = ft
        GListBox_775["fg"] = "#333333"
        GListBox_775["justify"] = "center"
        GListBox_775.place(x=100, y=100, width=186, height=364)

        GButton_550 = tk.Button(root)
        GButton_550["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_550["font"] = ft
        GButton_550["fg"] = "#273134"
        GButton_550["justify"] = "center"
        GButton_550["text"] = "Button"
        GButton_550.place(x=100, y=680, width=70, height=25)
        GButton_550["command"] = self.GButton_550_command

        GButton_974 = tk.Button(root)
        GButton_974["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_974["font"] = ft
        GButton_974["fg"] = "#273134"
        GButton_974["justify"] = "center"
        GButton_974["text"] = "Button"
        GButton_974.place(x=100, y=530, width=70, height=25)
        GButton_974["command"] = self.GButton_974_command

        GButton_623 = tk.Button(root)
        GButton_623["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_623["font"] = ft
        GButton_623["fg"] = "#273134"
        GButton_623["justify"] = "center"
        GButton_623["text"] = "Button"
        GButton_623.place(x=100, y=560, width=70, height=25)
        GButton_623["command"] = self.GButton_623_command

        GButton_577 = tk.Button(root)
        GButton_577["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_577["font"] = ft
        GButton_577["fg"] = "#273134"
        GButton_577["justify"] = "center"
        GButton_577["text"] = "Button"
        GButton_577.place(x=100, y=590, width=70, height=25)
        GButton_577["command"] = self.GButton_577_command

        GButton_745 = tk.Button(root)
        GButton_745["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_745["font"] = ft
        GButton_745["fg"] = "#273134"
        GButton_745["justify"] = "center"
        GButton_745["text"] = "Button"
        GButton_745.place(x=10, y=30, width=70, height=25)
        GButton_745["command"] = self.GButton_745_command

        GButton_536 = tk.Button(root)
        GButton_536["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_536["font"] = ft
        GButton_536["fg"] = "#273134"
        GButton_536["justify"] = "center"
        GButton_536["text"] = "Button"
        GButton_536.place(x=10, y=70, width=70, height=25)
        GButton_536["command"] = self.GButton_536_command

        GButton_153 = tk.Button(root)
        GButton_153["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_153["font"] = ft
        GButton_153["fg"] = "#273134"
        GButton_153["justify"] = "center"
        GButton_153["text"] = "Button"
        GButton_153.place(x=10, y=110, width=70, height=25)
        GButton_153["command"] = self.GButton_153_command

        GButton_667 = tk.Button(root)
        GButton_667["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_667["font"] = ft
        GButton_667["fg"] = "#273134"
        GButton_667["justify"] = "center"
        GButton_667["text"] = "Button"
        GButton_667.place(x=10, y=150, width=70, height=25)
        GButton_667["command"] = self.GButton_667_command

        GButton_299 = tk.Button(root)
        GButton_299["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_299["font"] = ft
        GButton_299["fg"] = "#273134"
        GButton_299["justify"] = "center"
        GButton_299["text"] = "Button"
        GButton_299.place(x=10, y=190, width=70, height=25)
        GButton_299["command"] = self.GButton_299_command

        GButton_212 = tk.Button(root)
        GButton_212["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_212["font"] = ft
        GButton_212["fg"] = "#273134"
        GButton_212["justify"] = "center"
        GButton_212["text"] = "Button"
        GButton_212.place(x=10, y=230, width=70, height=25)
        GButton_212["command"] = self.GButton_212_command

        GButton_525 = tk.Button(root)
        GButton_525["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_525["font"] = ft
        GButton_525["fg"] = "#273134"
        GButton_525["justify"] = "center"
        GButton_525["text"] = "Button"
        GButton_525.place(x=10, y=270, width=70, height=25)
        GButton_525["command"] = self.GButton_525_command

        GButton_516 = tk.Button(root)
        GButton_516["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#273134"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "Button"
        GButton_516.place(x=10, y=310, width=70, height=25)
        GButton_516["command"] = self.GButton_516_command

        GButton_445 = tk.Button(root)
        GButton_445["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_445["font"] = ft
        GButton_445["fg"] = "#273134"
        GButton_445["justify"] = "center"
        GButton_445["text"] = "Button"
        GButton_445.place(x=10, y=350, width=70, height=25)
        GButton_445["command"] = self.GButton_445_command

        GButton_494 = tk.Button(root)
        GButton_494["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_494["font"] = ft
        GButton_494["fg"] = "#273134"
        GButton_494["justify"] = "center"
        GButton_494["text"] = "Button"
        GButton_494.place(x=10, y=390, width=70, height=25)
        GButton_494["command"] = self.GButton_494_command

        GButton_230 = tk.Button(root)
        GButton_230["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_230["font"] = ft
        GButton_230["fg"] = "#273134"
        GButton_230["justify"] = "center"
        GButton_230["text"] = "Button"
        GButton_230.place(x=10, y=430, width=70, height=25)
        GButton_230["command"] = self.GButton_230_command

        GButton_415 = tk.Button(root)
        GButton_415["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_415["font"] = ft
        GButton_415["fg"] = "#273134"
        GButton_415["justify"] = "center"
        GButton_415["text"] = "Button"
        GButton_415.place(x=10, y=470, width=70, height=25)
        GButton_415["command"] = self.GButton_415_command

        GLineEdit_401 = tk.Entry(root)
        GLineEdit_401["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_401["font"] = ft
        GLineEdit_401["fg"] = "#333333"
        GLineEdit_401["justify"] = "center"
        GLineEdit_401["text"] = "Entry"
        GLineEdit_401.place(x=340, y=60, width=177, height=30)

        GLabel_612 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_612["font"] = ft
        GLabel_612["fg"] = "#333333"
        GLabel_612["justify"] = "center"
        GLabel_612["text"] = "label"
        GLabel_612.place(x=330, y=20, width=70, height=25)

        GButton_629 = tk.Button(root)
        GButton_629["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#273134"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Button"
        GButton_629.place(x=230, y=500, width=70, height=25)
        GButton_629["command"] = self.GButton_629_command

        GButton_566 = tk.Button(root)
        GButton_566["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_566["font"] = ft
        GButton_566["fg"] = "#273134"
        GButton_566["justify"] = "center"
        GButton_566["text"] = "Button"
        GButton_566.place(x=230, y=530, width=70, height=25)
        GButton_566["command"] = self.GButton_566_command

        GButton_15 = tk.Button(root)
        GButton_15["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_15["font"] = ft
        GButton_15["fg"] = "#273134"
        GButton_15["justify"] = "center"
        GButton_15["text"] = "Button"
        GButton_15.place(x=230, y=560, width=70, height=25)
        GButton_15["command"] = self.GButton_15_command

        GButton_649 = tk.Button(root)
        GButton_649["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_649["font"] = ft
        GButton_649["fg"] = "#273134"
        GButton_649["justify"] = "center"
        GButton_649["text"] = "Button"
        GButton_649.place(x=230, y=590, width=70, height=25)
        GButton_649["command"] = self.GButton_649_command

        GRadio_819 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_819["font"] = ft
        GRadio_819["fg"] = "#333333"
        GRadio_819["justify"] = "center"
        GRadio_819["text"] = "RadioButton"
        GRadio_819.place(x=340, y=120, width=85, height=25)
        GRadio_819["command"] = self.GRadio_819_command

        GRadio_84 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_84["font"] = ft
        GRadio_84["fg"] = "#333333"
        GRadio_84["justify"] = "center"
        GRadio_84["text"] = "RadioButton"
        GRadio_84.place(x=340, y=150, width=85, height=25)
        GRadio_84["command"] = self.GRadio_84_command

        GRadio_996 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_996["font"] = ft
        GRadio_996["fg"] = "#333333"
        GRadio_996["justify"] = "center"
        GRadio_996["text"] = "RadioButton"
        GRadio_996.place(x=340, y=180, width=85, height=25)
        GRadio_996["command"] = self.GRadio_996_command

        GRadio_957 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_957["font"] = ft
        GRadio_957["fg"] = "#333333"
        GRadio_957["justify"] = "center"
        GRadio_957["text"] = "RadioButton"
        GRadio_957.place(x=340, y=210, width=85, height=25)
        GRadio_957["command"] = self.GRadio_957_command

        GRadio_423 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_423["font"] = ft
        GRadio_423["fg"] = "#333333"
        GRadio_423["justify"] = "center"
        GRadio_423["text"] = "RadioButton"
        GRadio_423.place(x=340, y=240, width=85, height=25)
        GRadio_423["command"] = self.GRadio_423_command

        GRadio_153 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_153["font"] = ft
        GRadio_153["fg"] = "#333333"
        GRadio_153["justify"] = "center"
        GRadio_153["text"] = "RadioButton"
        GRadio_153.place(x=340, y=270, width=85, height=25)
        GRadio_153["command"] = self.GRadio_153_command

        GRadio_609 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_609["font"] = ft
        GRadio_609["fg"] = "#333333"
        GRadio_609["justify"] = "center"
        GRadio_609["text"] = "RadioButton"
        GRadio_609.place(x=340, y=300, width=85, height=25)
        GRadio_609["command"] = self.GRadio_609_command

        GRadio_345 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_345["font"] = ft
        GRadio_345["fg"] = "#333333"
        GRadio_345["justify"] = "center"
        GRadio_345["text"] = "RadioButton"
        GRadio_345.place(x=340, y=330, width=85, height=25)
        GRadio_345["command"] = self.GRadio_345_command

        GRadio_851 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_851["font"] = ft
        GRadio_851["fg"] = "#333333"
        GRadio_851["justify"] = "center"
        GRadio_851["text"] = "RadioButton"
        GRadio_851.place(x=340, y=360, width=85, height=25)
        GRadio_851["command"] = self.GRadio_851_command

        GRadio_20 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_20["font"] = ft
        GRadio_20["fg"] = "#333333"
        GRadio_20["justify"] = "center"
        GRadio_20["text"] = "RadioButton"
        GRadio_20.place(x=340, y=390, width=85, height=25)
        GRadio_20["command"] = self.GRadio_20_command

        GListBox_526 = tk.Listbox(root)
        GListBox_526["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_526["font"] = ft
        GListBox_526["fg"] = "#333333"
        GListBox_526["justify"] = "center"
        GListBox_526.place(x=450, y=100, width=285, height=400)

        GMessage_589 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_589["font"] = ft
        GMessage_589["fg"] = "#333333"
        GMessage_589["justify"] = "center"
        GMessage_589["text"] = "Message"
        GMessage_589.place(x=980, y=110, width=199, height=58)

        GMessage_848 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_848["font"] = ft
        GMessage_848["fg"] = "#333333"
        GMessage_848["justify"] = "center"
        GMessage_848["text"] = "Message"
        GMessage_848.place(x=1000, y=20, width=154, height=59)

        GMessage_939 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_939["font"] = ft
        GMessage_939["fg"] = "#333333"
        GMessage_939["justify"] = "center"
        GMessage_939["text"] = "Message"
        GMessage_939.place(x=980, y=190, width=181, height=109)

        GCheckBox_895 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_895["font"] = ft
        GCheckBox_895["fg"] = "#333333"
        GCheckBox_895["justify"] = "center"
        GCheckBox_895["text"] = "CheckBox"
        GCheckBox_895.place(x=880, y=40, width=70, height=25)
        GCheckBox_895["offvalue"] = "0"
        GCheckBox_895["onvalue"] = "1"
        GCheckBox_895["command"] = self.GCheckBox_895_command

        GCheckBox_904 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_904["font"] = ft
        GCheckBox_904["fg"] = "#333333"
        GCheckBox_904["justify"] = "center"
        GCheckBox_904["text"] = "CheckBox"
        GCheckBox_904.place(x=880, y=120, width=70, height=25)
        GCheckBox_904["offvalue"] = "0"
        GCheckBox_904["onvalue"] = "1"
        GCheckBox_904["command"] = self.GCheckBox_904_command

        GMessage_480 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_480["font"] = ft
        GMessage_480["fg"] = "#333333"
        GMessage_480["justify"] = "center"
        GMessage_480["text"] = "Message"
        GMessage_480.place(x=980, y=290, width=188, height=129)

        GCheckBox_945 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_945["font"] = ft
        GCheckBox_945["fg"] = "#333333"
        GCheckBox_945["justify"] = "center"
        GCheckBox_945["text"] = "CheckBox"
        GCheckBox_945.place(x=880, y=220, width=70, height=25)
        GCheckBox_945["offvalue"] = "0"
        GCheckBox_945["onvalue"] = "1"
        GCheckBox_945["command"] = self.GCheckBox_945_command

        GCheckBox_993 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_993["font"] = ft
        GCheckBox_993["fg"] = "#333333"
        GCheckBox_993["justify"] = "center"
        GCheckBox_993["text"] = "CheckBox"
        GCheckBox_993.place(x=880, y=330, width=70, height=25)
        GCheckBox_993["offvalue"] = "0"
        GCheckBox_993["onvalue"] = "1"
        GCheckBox_993["command"] = self.GCheckBox_993_command

        GButton_797 = tk.Button(root)
        GButton_797["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#273134"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Button"
        GButton_797.place(x=1070, y=590, width=70, height=25)
        GButton_797["command"] = self.GButton_797_command

        GButton_30 = tk.Button(root)
        GButton_30["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_30["font"] = ft
        GButton_30["fg"] = "#273134"
        GButton_30["justify"] = "center"
        GButton_30["text"] = "Button"
        GButton_30.place(x=1070, y=620, width=70, height=25)
        GButton_30["command"] = self.GButton_30_command

        GButton_526 = tk.Button(root)
        GButton_526["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_526["font"] = ft
        GButton_526["fg"] = "#273134"
        GButton_526["justify"] = "center"
        GButton_526["text"] = "Button"
        GButton_526.place(x=1070, y=650, width=70, height=25)
        GButton_526["command"] = self.GButton_526_command

        GButton_158 = tk.Button(root)
        GButton_158["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_158["font"] = ft
        GButton_158["fg"] = "#273134"
        GButton_158["justify"] = "center"
        GButton_158["text"] = "Button"
        GButton_158.place(x=1070, y=560, width=70, height=25)
        GButton_158["command"] = self.GButton_158_command

        GLineEdit_680 = tk.Entry(root)
        GLineEdit_680["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_680["font"] = ft
        GLineEdit_680["fg"] = "#333333"
        GLineEdit_680["justify"] = "center"
        GLineEdit_680["text"] = "Entry"
        GLineEdit_680.place(x=550, y=60, width=285, height=30)

        GRadio_868 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_868["font"] = ft
        GRadio_868["fg"] = "#333333"
        GRadio_868["justify"] = "center"
        GRadio_868["text"] = "RadioButton"
        GRadio_868.place(x=340, y=420, width=85, height=25)
        GRadio_868["command"] = self.GRadio_868_command

        GRadio_415 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_415["font"] = ft
        GRadio_415["fg"] = "#333333"
        GRadio_415["justify"] = "center"
        GRadio_415["text"] = "RadioButton"
        GRadio_415.place(x=340, y=450, width=85, height=25)
        GRadio_415["command"] = self.GRadio_415_command

        GRadio_865 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_865["font"] = ft
        GRadio_865["fg"] = "#333333"
        GRadio_865["justify"] = "center"
        GRadio_865["text"] = "RadioButton"
        GRadio_865.place(x=190, y=20, width=85, height=25)
        GRadio_865["command"] = self.GRadio_865_command

        GRadio_811 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_811["font"] = ft
        GRadio_811["fg"] = "#333333"
        GRadio_811["justify"] = "center"
        GRadio_811["text"] = "RadioButton"
        GRadio_811.place(x=740, y=20, width=85, height=25)
        GRadio_811["command"] = self.GRadio_811_command

        GRadio_450 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_450["font"] = ft
        GRadio_450["fg"] = "#333333"
        GRadio_450["justify"] = "center"
        GRadio_450["text"] = "RadioButton"
        GRadio_450.place(x=410, y=20, width=85, height=25)
        GRadio_450["command"] = self.GRadio_450_command

        GLabel_621 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_621["font"] = ft
        GLabel_621["fg"] = "#333333"
        GLabel_621["justify"] = "center"
        GLabel_621["text"] = "label"
        GLabel_621.place(x=560, y=20, width=70, height=25)

        GLabel_504 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_504["font"] = ft
        GLabel_504["fg"] = "#333333"
        GLabel_504["justify"] = "center"
        GLabel_504["text"] = "label"
        GLabel_504.place(x=470, y=540, width=70, height=25)

        GLabel_225 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_225["font"] = ft
        GLabel_225["fg"] = "#333333"
        GLabel_225["justify"] = "center"
        GLabel_225["text"] = "label"
        GLabel_225.place(x=610, y=540, width=70, height=25)

        GLabel_284 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_284["font"] = ft
        GLabel_284["fg"] = "#333333"
        GLabel_284["justify"] = "center"
        GLabel_284["text"] = "label"
        GLabel_284.place(x=790, y=540, width=70, height=25)

        GButton_406 = tk.Button(root)
        GButton_406["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_406["font"] = ft
        GButton_406["fg"] = "#273134"
        GButton_406["justify"] = "center"
        GButton_406["text"] = "Button"
        GButton_406.place(x=470, y=590, width=70, height=25)
        GButton_406["command"] = self.GButton_406_command

        GButton_589 = tk.Button(root)
        GButton_589["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_589["font"] = ft
        GButton_589["fg"] = "#273134"
        GButton_589["justify"] = "center"
        GButton_589["text"] = "Button"
        GButton_589.place(x=630, y=590, width=70, height=25)
        GButton_589["command"] = self.GButton_589_command

        GButton_70 = tk.Button(root)
        GButton_70["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_70["font"] = ft
        GButton_70["fg"] = "#273134"
        GButton_70["justify"] = "center"
        GButton_70["text"] = "Button"
        GButton_70.place(x=790, y=590, width=70, height=25)
        GButton_70["command"] = self.GButton_70_command

        GButton_729 = tk.Button(root)
        GButton_729["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_729["font"] = ft
        GButton_729["fg"] = "#273134"
        GButton_729["justify"] = "center"
        GButton_729["text"] = "Button"
        GButton_729.place(x=1070, y=530, width=70, height=25)
        GButton_729["command"] = self.GButton_729_command

        GButton_922 = tk.Button(root)
        GButton_922["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_922["font"] = ft
        GButton_922["fg"] = "#273134"
        GButton_922["justify"] = "center"
        GButton_922["text"] = "Button"
        GButton_922.place(x=990, y=650, width=70, height=25)
        GButton_922["command"] = self.GButton_922_command

        GButton_10 = tk.Button(root)
        GButton_10["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_10["font"] = ft
        GButton_10["fg"] = "#273134"
        GButton_10["justify"] = "center"
        GButton_10["text"] = "Button"
        GButton_10.place(x=990, y=620, width=70, height=25)
        GButton_10["command"] = self.GButton_10_command

        GButton_898 = tk.Button(root)
        GButton_898["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_898["font"] = ft
        GButton_898["fg"] = "#273134"
        GButton_898["justify"] = "center"
        GButton_898["text"] = "Button"
        GButton_898.place(x=990, y=590, width=70, height=25)
        GButton_898["command"] = self.GButton_898_command

        GButton_955 = tk.Button(root)
        GButton_955["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_955["font"] = ft
        GButton_955["fg"] = "#273134"
        GButton_955["justify"] = "center"
        GButton_955["text"] = "Button"
        GButton_955.place(x=990, y=560, width=70, height=25)
        GButton_955["command"] = self.GButton_955_command

        GLabel_221 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_221["font"] = ft
        GLabel_221["fg"] = "#333333"
        GLabel_221["justify"] = "center"
        GLabel_221["text"] = "label"
        GLabel_221.place(x=720, y=430, width=405, height=35)

        GButton_982 = tk.Button(root)
        GButton_982["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_982["font"] = ft
        GButton_982["fg"] = "#273134"
        GButton_982["justify"] = "center"
        GButton_982["text"] = "Button"
        GButton_982.place(x=990, y=530, width=70, height=25)
        GButton_982["command"] = self.GButton_982_command

        GButton_720 = tk.Button(root)
        GButton_720["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_720["font"] = ft
        GButton_720["fg"] = "#273134"
        GButton_720["justify"] = "center"
        GButton_720["text"] = "Button"
        GButton_720.place(x=10, y=510, width=70, height=25)
        GButton_720["command"] = self.GButton_720_command

        GButton_488 = tk.Button(root)
        GButton_488["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_488["font"] = ft
        GButton_488["fg"] = "#273134"
        GButton_488["justify"] = "center"
        GButton_488["text"] = "Button"
        GButton_488.place(x=10, y=550, width=70, height=25)
        GButton_488["command"] = self.GButton_488_command

        GButton_201 = tk.Button(root)
        GButton_201["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_201["font"] = ft
        GButton_201["fg"] = "#273134"
        GButton_201["justify"] = "center"
        GButton_201["text"] = "Button"
        GButton_201.place(x=10, y=590, width=70, height=25)
        GButton_201["command"] = self.GButton_201_command

        GButton_42 = tk.Button(root)
        GButton_42["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_42["font"] = ft
        GButton_42["fg"] = "#273134"
        GButton_42["justify"] = "center"
        GButton_42["text"] = "Button"
        GButton_42.place(x=10, y=630, width=70, height=25)
        GButton_42["command"] = self.GButton_42_command

        GButton_968 = tk.Button(root)
        GButton_968["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_968["font"] = ft
        GButton_968["fg"] = "#273134"
        GButton_968["justify"] = "center"
        GButton_968["text"] = "Button"
        GButton_968.place(x=10, y=670, width=70, height=25)
        GButton_968["command"] = self.GButton_968_command

        GRadio_233 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_233["font"] = ft
        GRadio_233["fg"] = "#333333"
        GRadio_233["justify"] = "center"
        GRadio_233["text"] = "RadioButton"
        GRadio_233.place(x=340, y=480, width=85, height=25)
        GRadio_233["command"] = self.GRadio_233_command

        GRadio_939 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_939["font"] = ft
        GRadio_939["fg"] = "#333333"
        GRadio_939["justify"] = "center"
        GRadio_939["text"] = "RadioButton"
        GRadio_939.place(x=340, y=510, width=85, height=25)
        GRadio_939["command"] = self.GRadio_939_command

        GRadio_612 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_612["font"] = ft
        GRadio_612["fg"] = "#333333"
        GRadio_612["justify"] = "center"
        GRadio_612["text"] = "RadioButton"
        GRadio_612.place(x=340, y=540, width=85, height=25)
        GRadio_612["command"] = self.GRadio_612_command

        GRadio_437 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_437["font"] = ft
        GRadio_437["fg"] = "#333333"
        GRadio_437["justify"] = "center"
        GRadio_437["text"] = "RadioButton"
        GRadio_437.place(x=340, y=570, width=85, height=25)
        GRadio_437["command"] = self.GRadio_437_command

        GRadio_621 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_621["font"] = ft
        GRadio_621["fg"] = "#333333"
        GRadio_621["justify"] = "center"
        GRadio_621["text"] = "RadioButton"
        GRadio_621.place(x=340, y=600, width=85, height=25)
        GRadio_621["command"] = self.GRadio_621_command

        GRadio_999 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_999["font"] = ft
        GRadio_999["fg"] = "#333333"
        GRadio_999["justify"] = "center"
        GRadio_999["text"] = "RadioButton"
        GRadio_999.place(x=340, y=630, width=85, height=25)
        GRadio_999["command"] = self.GRadio_999_command

        GButton_712 = tk.Button(root)
        GButton_712["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_712["font"] = ft
        GButton_712["fg"] = "#273134"
        GButton_712["justify"] = "center"
        GButton_712["text"] = "Button"
        GButton_712.place(x=100, y=620, width=70, height=25)
        GButton_712["command"] = self.GButton_712_command

        GButton_288 = tk.Button(root)
        GButton_288["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_288["font"] = ft
        GButton_288["fg"] = "#273134"
        GButton_288["justify"] = "center"
        GButton_288["text"] = "Button"
        GButton_288.place(x=230, y=620, width=70, height=25)
        GButton_288["command"] = self.GButton_288_command

        GButton_419 = tk.Button(root)
        GButton_419["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_419["font"] = ft
        GButton_419["fg"] = "#273134"
        GButton_419["justify"] = "center"
        GButton_419["text"] = "Button"
        GButton_419.place(x=100, y=650, width=70, height=25)
        GButton_419["command"] = self.GButton_419_command

        GButton_221 = tk.Button(root)
        GButton_221["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_221["font"] = ft
        GButton_221["fg"] = "#273134"
        GButton_221["justify"] = "center"
        GButton_221["text"] = "Button"
        GButton_221.place(x=230, y=650, width=70, height=25)
        GButton_221["command"] = self.GButton_221_command

        GButton_550 = tk.Button(root)
        GButton_550["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_550["font"] = ft
        GButton_550["fg"] = "#273134"
        GButton_550["justify"] = "center"
        GButton_550["text"] = "Button"
        GButton_550.place(x=100, y=680, width=70, height=25)
        GButton_550["command"] = self.GButton_550_command

        GButton_486 = tk.Button(root)
        GButton_486["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_486["font"] = ft
        GButton_486["fg"] = "#273134"
        GButton_486["justify"] = "center"
        GButton_486["text"] = "Button"
        GButton_486.place(x=230, y=680, width=70, height=25)
        GButton_486["command"] = self.GButton_486_command

        GRadio_791 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_791["font"] = ft
        GRadio_791["fg"] = "#333333"
        GRadio_791["justify"] = "center"
        GRadio_791["text"] = "RadioButton"
        GRadio_791.place(x=340, y=660, width=85, height=25)
        GRadio_791["command"] = self.GRadio_791_command

        GLineEdit_457 = tk.Entry(root)
        GLineEdit_457["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_457["font"] = ft
        GLineEdit_457["fg"] = "#333333"
        GLineEdit_457["justify"] = "center"
        GLineEdit_457["text"] = "Entry"
        GLineEdit_457.place(x=470, y=640, width=148, height=30)

        GLineEdit_867 = tk.Entry(root)
        GLineEdit_867["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_867["font"] = ft
        GLineEdit_867["fg"] = "#333333"
        GLineEdit_867["justify"] = "center"
        GLineEdit_867["text"] = "Entry"
        GLineEdit_867.place(x=640, y=640, width=70, height=25)

        GLineEdit_923 = tk.Entry(root)
        GLineEdit_923["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_923["font"] = ft
        GLineEdit_923["fg"] = "#333333"
        GLineEdit_923["justify"] = "center"
        GLineEdit_923["text"] = "Entry"
        GLineEdit_923.place(x=730, y=640, width=70, height=25)

        GButton_91 = tk.Button(root)
        GButton_91["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_91["font"] = ft
        GButton_91["fg"] = "#273134"
        GButton_91["justify"] = "center"
        GButton_91["text"] = "Button"
        GButton_91.place(x=500, y=670, width=70, height=25)
        GButton_91["command"] = self.GButton_91_command

        GButton_901 = tk.Button(root)
        GButton_901["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#273134"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "Button"
        GButton_901.place(x=730, y=670, width=70, height=25)
        GButton_901["command"] = self.GButton_901_command

        GButton_223 = tk.Button(root)
        GButton_223["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_223["font"] = ft
        GButton_223["fg"] = "#273134"
        GButton_223["justify"] = "center"
        GButton_223["text"] = "Button"
        GButton_223.place(x=640, y=670, width=70, height=25)
        GButton_223["command"] = self.GButton_223_command

        GLineEdit_392 = tk.Entry(root)
        GLineEdit_392["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_392["font"] = ft
        GLineEdit_392["fg"] = "#333333"
        GLineEdit_392["justify"] = "center"
        GLineEdit_392["text"] = "Entry"
        GLineEdit_392.place(x=820, y=640, width=70, height=25)

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#273134"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "Button"
        GButton_297.place(x=820, y=670, width=70, height=25)
        GButton_297["command"] = self.GButton_297_command

        GRadio_693 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_693["font"] = ft
        GRadio_693["fg"] = "#333333"
        GRadio_693["justify"] = "center"
        GRadio_693["text"] = "RadioButton"
        GRadio_693.place(x=190, y=0, width=85, height=25)
        GRadio_693["command"] = self.GRadio_693_command

        GRadio_173 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_173["font"] = ft
        GRadio_173["fg"] = "#333333"
        GRadio_173["justify"] = "center"
        GRadio_173["text"] = "RadioButton"
        GRadio_173.place(x=740, y=0, width=85, height=25)
        GRadio_173["command"] = self.GRadio_173_command

        GRadio_734 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_734["font"] = ft
        GRadio_734["fg"] = "#333333"
        GRadio_734["justify"] = "center"
        GRadio_734["text"] = "RadioButton"
        GRadio_734.place(x=410, y=0, width=85, height=25)
        GRadio_734["command"] = self.GRadio_734_command

    def GButton_550_command(self):
        print("command")

    def GButton_974_command(self):
        print("command")

    def GButton_623_command(self):
        print("command")

    def GButton_577_command(self):
        print("command")

    def GButton_745_command(self):
        print("command")

    def GButton_536_command(self):
        print("command")

    def GButton_153_command(self):
        print("command")

    def GButton_667_command(self):
        print("command")

    def GButton_299_command(self):
        print("command")

    def GButton_212_command(self):
        print("command")

    def GButton_525_command(self):
        print("command")

    def GButton_516_command(self):
        print("command")

    def GButton_445_command(self):
        print("command")

    def GButton_494_command(self):
        print("command")

    def GButton_230_command(self):
        print("command")

    def GButton_415_command(self):
        print("command")

    def GButton_629_command(self):
        print("command")

    def GButton_566_command(self):
        print("command")

    def GButton_15_command(self):
        print("command")

    def GButton_649_command(self):
        print("command")

    def GRadio_819_command(self):
        print("command")

    def GRadio_84_command(self):
        print("command")

    def GRadio_996_command(self):
        print("command")

    def GRadio_957_command(self):
        print("command")

    def GRadio_423_command(self):
        print("command")

    def GRadio_153_command(self):
        print("command")

    def GRadio_609_command(self):
        print("command")

    def GRadio_345_command(self):
        print("command")

    def GRadio_851_command(self):
        print("command")

    def GRadio_20_command(self):
        print("command")

    def GCheckBox_895_command(self):
        print("command")

    def GCheckBox_904_command(self):
        print("command")

    def GCheckBox_945_command(self):
        print("command")

    def GCheckBox_993_command(self):
        print("command")

    def GButton_797_command(self):
        print("command")

    def GButton_30_command(self):
        print("command")

    def GButton_526_command(self):
        print("command")

    def GButton_158_command(self):
        print("command")

    def GRadio_868_command(self):
        print("command")

    def GRadio_415_command(self):
        print("command")

    def GRadio_865_command(self):
        print("command")

    def GRadio_811_command(self):
        print("command")

    def GRadio_450_command(self):
        print("command")

    def GButton_406_command(self):
        print("command")

    def GButton_589_command(self):
        print("command")

    def GButton_70_command(self):
        print("command")

    def GButton_729_command(self):
        print("command")

    def GButton_922_command(self):
        print("command")

    def GButton_10_command(self):
        print("command")

    def GButton_898_command(self):
        print("command")

    def GButton_955_command(self):
        print("command")

    def GButton_982_command(self):
        print("command")

    def GButton_720_command(self):
        print("command")

    def GButton_488_command(self):
        print("command")

    def GButton_201_command(self):
        print("command")

    def GButton_42_command(self):
        print("command")

    def GButton_968_command(self):
        print("command")

    def GRadio_233_command(self):
        print("command")

    def GRadio_939_command(self):
        print("command")

    def GRadio_612_command(self):
        print("command")

    def GRadio_437_command(self):
        print("command")

    def GRadio_621_command(self):
        print("command")

    def GRadio_999_command(self):
        print("command")

    def GButton_712_command(self):
        print("command")

    def GButton_288_command(self):
        print("command")

    def GButton_419_command(self):
        print("command")

    def GButton_221_command(self):
        print("command")

    def GButton_550_command(self):
        print("command")

    def GButton_486_command(self):
        print("command")

    def GRadio_791_command(self):
        print("command")

    def GButton_91_command(self):
        print("command")

    def GButton_901_command(self):
        print("command")

    def GButton_223_command(self):
        print("command")

    def GButton_297_command(self):
        print("command")

    def GRadio_693_command(self):
        print("command")

    def GRadio_173_command(self):
        print("command")

    def GRadio_734_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
