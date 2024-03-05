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

        GButton_39 = tk.Button(root)
        GButton_39["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_39["font"] = ft
        GButton_39["fg"] = "#000000"
        GButton_39["justify"] = "center"
        GButton_39["text"] = "Button"
        GButton_39.place(x=10, y=10, width=70, height=25)
        GButton_39["command"] = self.GButton_39_command

        GButton_171 = tk.Button(root)
        GButton_171["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_171["font"] = ft
        GButton_171["fg"] = "#000000"
        GButton_171["justify"] = "center"
        GButton_171["text"] = "Button"
        GButton_171.place(x=80, y=10, width=70, height=25)
        GButton_171["command"] = self.GButton_171_command

        GButton_55 = tk.Button(root)
        GButton_55["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_55["font"] = ft
        GButton_55["fg"] = "#000000"
        GButton_55["justify"] = "center"
        GButton_55["text"] = "Button"
        GButton_55.place(x=150, y=10, width=70, height=25)
        GButton_55["command"] = self.GButton_55_command

        GButton_488 = tk.Button(root)
        GButton_488["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_488["font"] = ft
        GButton_488["fg"] = "#000000"
        GButton_488["justify"] = "center"
        GButton_488["text"] = "Button"
        GButton_488.place(x=220, y=10, width=70, height=25)
        GButton_488["command"] = self.GButton_488_command

        GButton_429 = tk.Button(root)
        GButton_429["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_429["font"] = ft
        GButton_429["fg"] = "#000000"
        GButton_429["justify"] = "center"
        GButton_429["text"] = "Button"
        GButton_429.place(x=290, y=10, width=70, height=25)
        GButton_429["command"] = self.GButton_429_command

        GButton_882 = tk.Button(root)
        GButton_882["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_882["font"] = ft
        GButton_882["fg"] = "#000000"
        GButton_882["justify"] = "center"
        GButton_882["text"] = "Button"
        GButton_882.place(x=360, y=10, width=70, height=25)
        GButton_882["command"] = self.GButton_882_command

        GButton_32 = tk.Button(root)
        GButton_32["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_32["font"] = ft
        GButton_32["fg"] = "#000000"
        GButton_32["justify"] = "center"
        GButton_32["text"] = "Button"
        GButton_32.place(x=430, y=10, width=70, height=25)
        GButton_32["command"] = self.GButton_32_command

        GButton_434 = tk.Button(root)
        GButton_434["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_434["font"] = ft
        GButton_434["fg"] = "#000000"
        GButton_434["justify"] = "center"
        GButton_434["text"] = "Button"
        GButton_434.place(x=500, y=10, width=70, height=25)
        GButton_434["command"] = self.GButton_434_command

        GLabel_200 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_200["font"] = ft
        GLabel_200["fg"] = "#333333"
        GLabel_200["justify"] = "center"
        GLabel_200["text"] = "label"
        GLabel_200.place(x=0, y=60, width=70, height=25)

        GLineEdit_478 = tk.Entry(root)
        GLineEdit_478["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_478["font"] = ft
        GLineEdit_478["fg"] = "#333333"
        GLineEdit_478["justify"] = "center"
        GLineEdit_478["text"] = "Entry"
        GLineEdit_478.place(x=0, y=100, width=70, height=25)

        GLabel_512 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_512["font"] = ft
        GLabel_512["fg"] = "#333333"
        GLabel_512["justify"] = "center"
        GLabel_512["text"] = "label"
        GLabel_512.place(x=80, y=60, width=70, height=25)

        GLineEdit_131 = tk.Entry(root)
        GLineEdit_131["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_131["font"] = ft
        GLineEdit_131["fg"] = "#333333"
        GLineEdit_131["justify"] = "center"
        GLineEdit_131["text"] = "Entry"
        GLineEdit_131.place(x=80, y=100, width=70, height=25)

        GLabel_139 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = "label"
        GLabel_139.place(x=160, y=60, width=70, height=25)

        GLineEdit_922 = tk.Entry(root)
        GLineEdit_922["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_922["font"] = ft
        GLineEdit_922["fg"] = "#333333"
        GLineEdit_922["justify"] = "center"
        GLineEdit_922["text"] = "Entry"
        GLineEdit_922.place(x=170, y=100, width=70, height=25)

        GLabel_563 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_563["font"] = ft
        GLabel_563["fg"] = "#333333"
        GLabel_563["justify"] = "center"
        GLabel_563["text"] = "label"
        GLabel_563.place(x=260, y=60, width=70, height=25)

        GLineEdit_534 = tk.Entry(root)
        GLineEdit_534["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_534["font"] = ft
        GLineEdit_534["fg"] = "#333333"
        GLineEdit_534["justify"] = "center"
        GLineEdit_534["text"] = "Entry"
        GLineEdit_534.place(x=260, y=100, width=70, height=25)

        GListBox_223 = tk.Listbox(root)
        GListBox_223["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_223["font"] = ft
        GListBox_223["fg"] = "#333333"
        GListBox_223["justify"] = "center"
        GListBox_223.place(x=30, y=210, width=80, height=25)

        GListBox_91 = tk.Listbox(root)
        GListBox_91["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_91["font"] = ft
        GListBox_91["fg"] = "#333333"
        GListBox_91["justify"] = "center"
        GListBox_91.place(x=170, y=210, width=80, height=25)

        GLabel_353 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_353["font"] = ft
        GLabel_353["fg"] = "#333333"
        GLabel_353["justify"] = "center"
        GLabel_353["text"] = "label"
        GLabel_353.place(x=10, y=170, width=70, height=25)

        GLabel_438 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_438["font"] = ft
        GLabel_438["fg"] = "#333333"
        GLabel_438["justify"] = "center"
        GLabel_438["text"] = "label"
        GLabel_438.place(x=160, y=170, width=70, height=25)

        GRadio_334 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_334["font"] = ft
        GRadio_334["fg"] = "#333333"
        GRadio_334["justify"] = "center"
        GRadio_334["text"] = "RadioButton"
        GRadio_334.place(x=490, y=90, width=85, height=25)
        GRadio_334["command"] = self.GRadio_334_command

        GRadio_210 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_210["font"] = ft
        GRadio_210["fg"] = "#333333"
        GRadio_210["justify"] = "center"
        GRadio_210["text"] = "RadioButton"
        GRadio_210.place(x=490, y=130, width=85, height=25)
        GRadio_210["command"] = self.GRadio_210_command

        GRadio_250 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_250["font"] = ft
        GRadio_250["fg"] = "#333333"
        GRadio_250["justify"] = "center"
        GRadio_250["text"] = "RadioButton"
        GRadio_250.place(x=490, y=180, width=85, height=25)
        GRadio_250["command"] = self.GRadio_250_command

        GRadio_263 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_263["font"] = ft
        GRadio_263["fg"] = "#333333"
        GRadio_263["justify"] = "center"
        GRadio_263["text"] = "RadioButton"
        GRadio_263.place(x=490, y=220, width=85, height=25)
        GRadio_263["command"] = self.GRadio_263_command

        GRadio_928 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_928["font"] = ft
        GRadio_928["fg"] = "#333333"
        GRadio_928["justify"] = "center"
        GRadio_928["text"] = "RadioButton"
        GRadio_928.place(x=490, y=260, width=85, height=25)
        GRadio_928["command"] = self.GRadio_928_command

        GRadio_59 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_59["font"] = ft
        GRadio_59["fg"] = "#333333"
        GRadio_59["justify"] = "center"
        GRadio_59["text"] = "RadioButton"
        GRadio_59.place(x=490, y=300, width=85, height=25)
        GRadio_59["command"] = self.GRadio_59_command

        GRadio_688 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_688["font"] = ft
        GRadio_688["fg"] = "#333333"
        GRadio_688["justify"] = "center"
        GRadio_688["text"] = "RadioButton"
        GRadio_688.place(x=490, y=340, width=85, height=25)
        GRadio_688["command"] = self.GRadio_688_command

        GButton_484 = tk.Button(root)
        GButton_484["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_484["font"] = ft
        GButton_484["fg"] = "#000000"
        GButton_484["justify"] = "center"
        GButton_484["text"] = "Button"
        GButton_484.place(x=480, y=390, width=70, height=25)
        GButton_484["command"] = self.GButton_484_command

        GButton_638 = tk.Button(root)
        GButton_638["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_638["font"] = ft
        GButton_638["fg"] = "#000000"
        GButton_638["justify"] = "center"
        GButton_638["text"] = "Button"
        GButton_638.place(x=480, y=420, width=70, height=25)
        GButton_638["command"] = self.GButton_638_command

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#000000"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "Button"
        GButton_297.place(x=480, y=450, width=70, height=25)
        GButton_297["command"] = self.GButton_297_command

        GButton_189 = tk.Button(root)
        GButton_189["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_189["font"] = ft
        GButton_189["fg"] = "#000000"
        GButton_189["justify"] = "center"
        GButton_189["text"] = "Button"
        GButton_189.place(x=10, y=140, width=70, height=25)
        GButton_189["command"] = self.GButton_189_command

        GButton_629 = tk.Button(root)
        GButton_629["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Button"
        GButton_629.place(x=90, y=140, width=70, height=25)
        GButton_629["command"] = self.GButton_629_command

        GButton_963 = tk.Button(root)
        GButton_963["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_963["font"] = ft
        GButton_963["fg"] = "#000000"
        GButton_963["justify"] = "center"
        GButton_963["text"] = "Button"
        GButton_963.place(x=170, y=140, width=70, height=25)
        GButton_963["command"] = self.GButton_963_command

        GButton_295 = tk.Button(root)
        GButton_295["bg"] = "#dedfe3"
        ft = tkFont.Font(family="Times", size=10)
        GButton_295["font"] = ft
        GButton_295["fg"] = "#000000"
        GButton_295["justify"] = "center"
        GButton_295["text"] = "Button"
        GButton_295.place(x=260, y=140, width=70, height=25)
        GButton_295["command"] = self.GButton_295_command

    def GButton_39_command(self):
        print("command")

    def GButton_171_command(self):
        print("command")

    def GButton_55_command(self):
        print("command")

    def GButton_488_command(self):
        print("command")

    def GButton_429_command(self):
        print("command")

    def GButton_882_command(self):
        print("command")

    def GButton_32_command(self):
        print("command")

    def GButton_434_command(self):
        print("command")

    def GRadio_334_command(self):
        print("command")

    def GRadio_210_command(self):
        print("command")

    def GRadio_250_command(self):
        print("command")

    def GRadio_263_command(self):
        print("command")

    def GRadio_928_command(self):
        print("command")

    def GRadio_59_command(self):
        print("command")

    def GRadio_688_command(self):
        print("command")

    def GButton_484_command(self):
        print("command")

    def GButton_638_command(self):
        print("command")

    def GButton_297_command(self):
        print("command")

    def GButton_189_command(self):
        print("command")

    def GButton_629_command(self):
        print("command")

    def GButton_963_command(self):
        print("command")

    def GButton_295_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
