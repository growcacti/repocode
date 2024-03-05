import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 982
        height = 669
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

        GListBox_545 = tk.Listbox(root)
        GListBox_545["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_545["font"] = ft
        GListBox_545["fg"] = "#333333"
        GListBox_545["justify"] = "center"
        GListBox_545.place(x=470, y=50, width=144, height=347)

        GListBox_955 = tk.Listbox(root)
        GListBox_955["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_955["font"] = ft
        GListBox_955["fg"] = "#333333"
        GListBox_955["justify"] = "center"
        GListBox_955.place(x=310, y=50, width=147, height=327)

        GListBox_444 = tk.Listbox(root)
        GListBox_444["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_444["font"] = ft
        GListBox_444["fg"] = "#333333"
        GListBox_444["justify"] = "center"
        GListBox_444.place(x=100, y=50, width=189, height=328)

        GListBox_565 = tk.Listbox(root)
        GListBox_565["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_565["font"] = ft
        GListBox_565["fg"] = "#333333"
        GListBox_565["justify"] = "center"
        GListBox_565.place(x=640, y=50, width=213, height=357)

        GButton_304 = tk.Button(root)
        GButton_304["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_304["font"] = ft
        GButton_304["fg"] = "#273134"
        GButton_304["justify"] = "center"
        GButton_304["text"] = "Button"
        GButton_304.place(x=10, y=20, width=70, height=25)
        GButton_304["command"] = self.GButton_304_command

        GButton_753 = tk.Button(root)
        GButton_753["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_753["font"] = ft
        GButton_753["fg"] = "#273134"
        GButton_753["justify"] = "center"
        GButton_753["text"] = "Button"
        GButton_753.place(x=10, y=50, width=70, height=25)
        GButton_753["command"] = self.GButton_753_command

        GButton_49 = tk.Button(root)
        GButton_49["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_49["font"] = ft
        GButton_49["fg"] = "#273134"
        GButton_49["justify"] = "center"
        GButton_49["text"] = "Button"
        GButton_49.place(x=10, y=80, width=70, height=25)
        GButton_49["command"] = self.GButton_49_command

        GButton_922 = tk.Button(root)
        GButton_922["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_922["font"] = ft
        GButton_922["fg"] = "#273134"
        GButton_922["justify"] = "center"
        GButton_922["text"] = "Button"
        GButton_922.place(x=10, y=110, width=70, height=25)
        GButton_922["command"] = self.GButton_922_command

        GLineEdit_233 = tk.Entry(root)
        GLineEdit_233["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_233["font"] = ft
        GLineEdit_233["fg"] = "#333333"
        GLineEdit_233["justify"] = "center"
        GLineEdit_233["text"] = "Entry"
        GLineEdit_233.place(x=110, y=20, width=188, height=30)

        GLineEdit_363 = tk.Entry(root)
        GLineEdit_363["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_363["font"] = ft
        GLineEdit_363["fg"] = "#333333"
        GLineEdit_363["justify"] = "center"
        GLineEdit_363["text"] = "Entry"
        GLineEdit_363.place(x=320, y=20, width=138, height=30)

        GLineEdit_527 = tk.Entry(root)
        GLineEdit_527["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_527["font"] = ft
        GLineEdit_527["fg"] = "#333333"
        GLineEdit_527["justify"] = "center"
        GLineEdit_527["text"] = "Entry"
        GLineEdit_527.place(x=480, y=20, width=132, height=30)

        GLineEdit_489 = tk.Entry(root)
        GLineEdit_489["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_489["font"] = ft
        GLineEdit_489["fg"] = "#333333"
        GLineEdit_489["justify"] = "center"
        GLineEdit_489["text"] = "Entry"
        GLineEdit_489.place(x=640, y=20, width=210, height=30)

        GButton_955 = tk.Button(root)
        GButton_955["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_955["font"] = ft
        GButton_955["fg"] = "#273134"
        GButton_955["justify"] = "center"
        GButton_955["text"] = "Button"
        GButton_955.place(x=10, y=140, width=70, height=25)
        GButton_955["command"] = self.GButton_955_command

        GButton_740 = tk.Button(root)
        GButton_740["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_740["font"] = ft
        GButton_740["fg"] = "#273134"
        GButton_740["justify"] = "center"
        GButton_740["text"] = "Button"
        GButton_740.place(x=10, y=170, width=70, height=25)
        GButton_740["command"] = self.GButton_740_command

        GLabel_572 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_572["font"] = ft
        GLabel_572["fg"] = "#333333"
        GLabel_572["justify"] = "center"
        GLabel_572["text"] = "label"
        GLabel_572.place(x=170, y=420, width=70, height=25)

        GLabel_141 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_141["font"] = ft
        GLabel_141["fg"] = "#333333"
        GLabel_141["justify"] = "center"
        GLabel_141["text"] = "label"
        GLabel_141.place(x=350, y=420, width=70, height=25)

        GLabel_271 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_271["font"] = ft
        GLabel_271["fg"] = "#333333"
        GLabel_271["justify"] = "center"
        GLabel_271["text"] = "label"
        GLabel_271.place(x=510, y=420, width=70, height=25)

        GLabel_775 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_775["font"] = ft
        GLabel_775["fg"] = "#333333"
        GLabel_775["justify"] = "center"
        GLabel_775["text"] = "label"
        GLabel_775.place(x=710, y=420, width=70, height=25)

        GButton_168 = tk.Button(root)
        GButton_168["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_168["font"] = ft
        GButton_168["fg"] = "#273134"
        GButton_168["justify"] = "center"
        GButton_168["text"] = "Button"
        GButton_168.place(x=10, y=200, width=70, height=25)
        GButton_168["command"] = self.GButton_168_command

        GButton_761 = tk.Button(root)
        GButton_761["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_761["font"] = ft
        GButton_761["fg"] = "#273134"
        GButton_761["justify"] = "center"
        GButton_761["text"] = "Button"
        GButton_761.place(x=10, y=230, width=70, height=25)
        GButton_761["command"] = self.GButton_761_command

        GButton_634 = tk.Button(root)
        GButton_634["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_634["font"] = ft
        GButton_634["fg"] = "#273134"
        GButton_634["justify"] = "center"
        GButton_634["text"] = "Button"
        GButton_634.place(x=10, y=260, width=70, height=25)
        GButton_634["command"] = self.GButton_634_command

        GButton_243 = tk.Button(root)
        GButton_243["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_243["font"] = ft
        GButton_243["fg"] = "#273134"
        GButton_243["justify"] = "center"
        GButton_243["text"] = "Button"
        GButton_243.place(x=10, y=290, width=70, height=25)
        GButton_243["command"] = self.GButton_243_command

        GButton_460 = tk.Button(root)
        GButton_460["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_460["font"] = ft
        GButton_460["fg"] = "#273134"
        GButton_460["justify"] = "center"
        GButton_460["text"] = "Button"
        GButton_460.place(x=10, y=320, width=70, height=25)
        GButton_460["command"] = self.GButton_460_command

        GButton_925 = tk.Button(root)
        GButton_925["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_925["font"] = ft
        GButton_925["fg"] = "#273134"
        GButton_925["justify"] = "center"
        GButton_925["text"] = "Button"
        GButton_925.place(x=10, y=350, width=70, height=25)
        GButton_925["command"] = self.GButton_925_command

        GButton_237 = tk.Button(root)
        GButton_237["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_237["font"] = ft
        GButton_237["fg"] = "#273134"
        GButton_237["justify"] = "center"
        GButton_237["text"] = "Button"
        GButton_237.place(x=10, y=380, width=70, height=25)
        GButton_237["command"] = self.GButton_237_command

        GButton_570 = tk.Button(root)
        GButton_570["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#273134"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Button"
        GButton_570.place(x=110, y=460, width=70, height=25)
        GButton_570["command"] = self.GButton_570_command

        GButton_691 = tk.Button(root)
        GButton_691["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_691["font"] = ft
        GButton_691["fg"] = "#273134"
        GButton_691["justify"] = "center"
        GButton_691["text"] = "Button"
        GButton_691.place(x=360, y=470, width=70, height=25)
        GButton_691["command"] = self.GButton_691_command

        GButton_555 = tk.Button(root)
        GButton_555["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_555["font"] = ft
        GButton_555["fg"] = "#273134"
        GButton_555["justify"] = "center"
        GButton_555["text"] = "Button"
        GButton_555.place(x=110, y=500, width=70, height=25)
        GButton_555["command"] = self.GButton_555_command

        GButton_459 = tk.Button(root)
        GButton_459["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#273134"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "Button"
        GButton_459.place(x=110, y=540, width=70, height=25)
        GButton_459["command"] = self.GButton_459_command

        GButton_572 = tk.Button(root)
        GButton_572["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#273134"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Button"
        GButton_572.place(x=360, y=510, width=70, height=25)
        GButton_572["command"] = self.GButton_572_command

        GButton_267 = tk.Button(root)
        GButton_267["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_267["font"] = ft
        GButton_267["fg"] = "#273134"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "Button"
        GButton_267.place(x=360, y=550, width=70, height=25)
        GButton_267["command"] = self.GButton_267_command

        GButton_116 = tk.Button(root)
        GButton_116["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_116["font"] = ft
        GButton_116["fg"] = "#273134"
        GButton_116["justify"] = "center"
        GButton_116["text"] = "Button"
        GButton_116.place(x=520, y=460, width=70, height=25)
        GButton_116["command"] = self.GButton_116_command

        GButton_789 = tk.Button(root)
        GButton_789["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_789["font"] = ft
        GButton_789["fg"] = "#273134"
        GButton_789["justify"] = "center"
        GButton_789["text"] = "Button"
        GButton_789.place(x=520, y=500, width=70, height=25)
        GButton_789["command"] = self.GButton_789_command

        GButton_286 = tk.Button(root)
        GButton_286["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_286["font"] = ft
        GButton_286["fg"] = "#273134"
        GButton_286["justify"] = "center"
        GButton_286["text"] = "Button"
        GButton_286.place(x=520, y=550, width=70, height=25)
        GButton_286["command"] = self.GButton_286_command

        GButton_192 = tk.Button(root)
        GButton_192["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_192["font"] = ft
        GButton_192["fg"] = "#273134"
        GButton_192["justify"] = "center"
        GButton_192["text"] = "Button"
        GButton_192.place(x=710, y=460, width=70, height=25)
        GButton_192["command"] = self.GButton_192_command

        GButton_666 = tk.Button(root)
        GButton_666["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_666["font"] = ft
        GButton_666["fg"] = "#273134"
        GButton_666["justify"] = "center"
        GButton_666["text"] = "Button"
        GButton_666.place(x=710, y=500, width=70, height=25)
        GButton_666["command"] = self.GButton_666_command

        GButton_786 = tk.Button(root)
        GButton_786["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_786["font"] = ft
        GButton_786["fg"] = "#273134"
        GButton_786["justify"] = "center"
        GButton_786["text"] = "Button"
        GButton_786.place(x=710, y=550, width=70, height=25)
        GButton_786["command"] = self.GButton_786_command

        GRadio_811 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_811["font"] = ft
        GRadio_811["fg"] = "#333333"
        GRadio_811["justify"] = "center"
        GRadio_811["text"] = "RadioButton"
        GRadio_811.place(x=880, y=20, width=85, height=25)
        GRadio_811["command"] = self.GRadio_811_command

        GRadio_500 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_500["font"] = ft
        GRadio_500["fg"] = "#333333"
        GRadio_500["justify"] = "center"
        GRadio_500["text"] = "RadioButton"
        GRadio_500.place(x=880, y=40, width=85, height=25)
        GRadio_500["command"] = self.GRadio_500_command

        GRadio_398 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_398["font"] = ft
        GRadio_398["fg"] = "#333333"
        GRadio_398["justify"] = "center"
        GRadio_398["text"] = "RadioButton"
        GRadio_398.place(x=880, y=60, width=85, height=25)
        GRadio_398["command"] = self.GRadio_398_command

        GRadio_414 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_414["font"] = ft
        GRadio_414["fg"] = "#333333"
        GRadio_414["justify"] = "center"
        GRadio_414["text"] = "RadioButton"
        GRadio_414.place(x=880, y=80, width=85, height=25)
        GRadio_414["command"] = self.GRadio_414_command

        GRadio_727 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_727["font"] = ft
        GRadio_727["fg"] = "#333333"
        GRadio_727["justify"] = "center"
        GRadio_727["text"] = "RadioButton"
        GRadio_727.place(x=880, y=100, width=85, height=25)
        GRadio_727["command"] = self.GRadio_727_command

        GRadio_473 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_473["font"] = ft
        GRadio_473["fg"] = "#333333"
        GRadio_473["justify"] = "center"
        GRadio_473["text"] = "RadioButton"
        GRadio_473.place(x=880, y=120, width=85, height=25)
        GRadio_473["command"] = self.GRadio_473_command

        GCheckBox_183 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_183["font"] = ft
        GCheckBox_183["fg"] = "#333333"
        GCheckBox_183["justify"] = "center"
        GCheckBox_183["text"] = "CheckBox"
        GCheckBox_183.place(x=850, y=450, width=70, height=25)
        GCheckBox_183["offvalue"] = "0"
        GCheckBox_183["onvalue"] = "1"
        GCheckBox_183["command"] = self.GCheckBox_183_command

        GCheckBox_632 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_632["font"] = ft
        GCheckBox_632["fg"] = "#333333"
        GCheckBox_632["justify"] = "center"
        GCheckBox_632["text"] = "CheckBox"
        GCheckBox_632.place(x=850, y=470, width=70, height=25)
        GCheckBox_632["offvalue"] = "0"
        GCheckBox_632["onvalue"] = "1"
        GCheckBox_632["command"] = self.GCheckBox_632_command

        GCheckBox_656 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_656["font"] = ft
        GCheckBox_656["fg"] = "#333333"
        GCheckBox_656["justify"] = "center"
        GCheckBox_656["text"] = "CheckBox"
        GCheckBox_656.place(x=120, y=590, width=70, height=25)
        GCheckBox_656["offvalue"] = "0"
        GCheckBox_656["onvalue"] = "1"
        GCheckBox_656["command"] = self.GCheckBox_656_command

        GCheckBox_648 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_648["font"] = ft
        GCheckBox_648["fg"] = "#333333"
        GCheckBox_648["justify"] = "center"
        GCheckBox_648["text"] = "CheckBox"
        GCheckBox_648.place(x=360, y=590, width=70, height=25)
        GCheckBox_648["offvalue"] = "0"
        GCheckBox_648["onvalue"] = "1"
        GCheckBox_648["command"] = self.GCheckBox_648_command

        GCheckBox_225 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_225["font"] = ft
        GCheckBox_225["fg"] = "#333333"
        GCheckBox_225["justify"] = "center"
        GCheckBox_225["text"] = "CheckBox"
        GCheckBox_225.place(x=510, y=590, width=70, height=25)
        GCheckBox_225["offvalue"] = "0"
        GCheckBox_225["onvalue"] = "1"
        GCheckBox_225["command"] = self.GCheckBox_225_command

        GCheckBox_3 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_3["font"] = ft
        GCheckBox_3["fg"] = "#333333"
        GCheckBox_3["justify"] = "center"
        GCheckBox_3["text"] = "CheckBox"
        GCheckBox_3.place(x=710, y=590, width=70, height=25)
        GCheckBox_3["offvalue"] = "0"
        GCheckBox_3["onvalue"] = "1"
        GCheckBox_3["command"] = self.GCheckBox_3_command

        GCheckBox_484 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_484["font"] = ft
        GCheckBox_484["fg"] = "#333333"
        GCheckBox_484["justify"] = "center"
        GCheckBox_484["text"] = "CheckBox"
        GCheckBox_484.place(x=850, y=490, width=70, height=25)
        GCheckBox_484["offvalue"] = "0"
        GCheckBox_484["onvalue"] = "1"
        GCheckBox_484["command"] = self.GCheckBox_484_command

        GCheckBox_125 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_125["font"] = ft
        GCheckBox_125["fg"] = "#333333"
        GCheckBox_125["justify"] = "center"
        GCheckBox_125["text"] = "CheckBox"
        GCheckBox_125.place(x=850, y=510, width=70, height=25)
        GCheckBox_125["offvalue"] = "0"
        GCheckBox_125["onvalue"] = "1"
        GCheckBox_125["command"] = self.GCheckBox_125_command

        GCheckBox_190 = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GCheckBox_190["font"] = ft
        GCheckBox_190["fg"] = "#333333"
        GCheckBox_190["justify"] = "center"
        GCheckBox_190["text"] = "CheckBox"
        GCheckBox_190.place(x=850, y=530, width=70, height=25)
        GCheckBox_190["offvalue"] = "0"
        GCheckBox_190["onvalue"] = "1"
        GCheckBox_190["command"] = self.GCheckBox_190_command

        GRadio_437 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_437["font"] = ft
        GRadio_437["fg"] = "#333333"
        GRadio_437["justify"] = "center"
        GRadio_437["text"] = "RadioButton"
        GRadio_437.place(x=880, y=140, width=85, height=25)
        GRadio_437["command"] = self.GRadio_437_command

        GRadio_887 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_887["font"] = ft
        GRadio_887["fg"] = "#333333"
        GRadio_887["justify"] = "center"
        GRadio_887["text"] = "RadioButton"
        GRadio_887.place(x=880, y=160, width=85, height=25)
        GRadio_887["command"] = self.GRadio_887_command

        GButton_449 = tk.Button(root)
        GButton_449["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_449["font"] = ft
        GButton_449["fg"] = "#273134"
        GButton_449["justify"] = "center"
        GButton_449["text"] = "Button"
        GButton_449.place(x=10, y=410, width=70, height=25)
        GButton_449["command"] = self.GButton_449_command

        GButton_377 = tk.Button(root)
        GButton_377["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_377["font"] = ft
        GButton_377["fg"] = "#273134"
        GButton_377["justify"] = "center"
        GButton_377["text"] = "Button"
        GButton_377.place(x=10, y=440, width=70, height=25)
        GButton_377["command"] = self.GButton_377_command

        GButton_938 = tk.Button(root)
        GButton_938["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_938["font"] = ft
        GButton_938["fg"] = "#273134"
        GButton_938["justify"] = "center"
        GButton_938["text"] = "Button"
        GButton_938.place(x=10, y=470, width=70, height=25)
        GButton_938["command"] = self.GButton_938_command

        GButton_603 = tk.Button(root)
        GButton_603["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_603["font"] = ft
        GButton_603["fg"] = "#273134"
        GButton_603["justify"] = "center"
        GButton_603["text"] = "Button"
        GButton_603.place(x=10, y=500, width=70, height=25)
        GButton_603["command"] = self.GButton_603_command

        GButton_506 = tk.Button(root)
        GButton_506["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_506["font"] = ft
        GButton_506["fg"] = "#273134"
        GButton_506["justify"] = "center"
        GButton_506["text"] = "Button"
        GButton_506.place(x=10, y=530, width=70, height=25)
        GButton_506["command"] = self.GButton_506_command

    def GButton_304_command(self):
        print("command")

    def GButton_753_command(self):
        print("command")

    def GButton_49_command(self):
        print("command")

    def GButton_922_command(self):
        print("command")

    def GButton_955_command(self):
        print("command")

    def GButton_740_command(self):
        print("command")

    def GButton_168_command(self):
        print("command")

    def GButton_761_command(self):
        print("command")

    def GButton_634_command(self):
        print("command")

    def GButton_243_command(self):
        print("command")

    def GButton_460_command(self):
        print("command")

    def GButton_925_command(self):
        print("command")

    def GButton_237_command(self):
        print("command")

    def GButton_570_command(self):
        print("command")

    def GButton_691_command(self):
        print("command")

    def GButton_555_command(self):
        print("command")

    def GButton_459_command(self):
        print("command")

    def GButton_572_command(self):
        print("command")

    def GButton_267_command(self):
        print("command")

    def GButton_116_command(self):
        print("command")

    def GButton_789_command(self):
        print("command")

    def GButton_286_command(self):
        print("command")

    def GButton_192_command(self):
        print("command")

    def GButton_666_command(self):
        print("command")

    def GButton_786_command(self):
        print("command")

    def GRadio_811_command(self):
        print("command")

    def GRadio_500_command(self):
        print("command")

    def GRadio_398_command(self):
        print("command")

    def GRadio_414_command(self):
        print("command")

    def GRadio_727_command(self):
        print("command")

    def GRadio_473_command(self):
        print("command")

    def GCheckBox_183_command(self):
        print("command")

    def GCheckBox_632_command(self):
        print("command")

    def GCheckBox_656_command(self):
        print("command")

    def GCheckBox_648_command(self):
        print("command")

    def GCheckBox_225_command(self):
        print("command")

    def GCheckBox_3_command(self):
        print("command")

    def GCheckBox_484_command(self):
        print("command")

    def GCheckBox_125_command(self):
        print("command")

    def GCheckBox_190_command(self):
        print("command")

    def GRadio_437_command(self):
        print("command")

    def GRadio_887_command(self):
        print("command")

    def GButton_449_command(self):
        print("command")

    def GButton_377_command(self):
        print("command")

    def GButton_938_command(self):
        print("command")

    def GButton_603_command(self):
        print("command")

    def GButton_506_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
