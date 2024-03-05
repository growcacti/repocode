import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"


class NewprojectWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(NewprojectWidget, self).__init__(master, **kw)
        self.button70 = ttk.Button(self)
        self.button70.configure(text="button70")
        self.button70.pack(side="top")
        self.button71 = ttk.Button(self)
        self.button71.configure(text="button71")
        self.button71.pack(side="top")
        self.button72 = ttk.Button(self)
        self.button72.configure(text="button72")
        self.button72.pack(side="top")
        self.button73 = ttk.Button(self)
        self.button73.configure(text="button73")
        self.button73.pack(side="top")
        self.button74 = ttk.Button(self)
        self.button74.configure(text="button74")
        self.button74.pack(side="top")
        self.button75 = ttk.Button(self)
        self.button75.configure(text="button75")
        self.button75.pack(side="top")
        self.button76 = ttk.Button(self)
        self.button76.configure(text="button76")
        self.button76.pack(side="top")
        self.button77 = ttk.Button(self)
        self.button77.configure(text="button77")
        self.button77.pack(side="top")
        self.button78 = ttk.Button(self)
        self.button78.configure(text="button78")
        self.button78.pack(side="top")
        self.button79 = ttk.Button(self)
        self.button79.configure(text="button79")
        self.button79.pack(side="top")
        self.button80 = ttk.Button(self)
        self.button80.configure(text="button80")
        self.button80.pack(side="top")
        self.button81 = ttk.Button(self)
        self.button81.configure(text="button81")
        self.button81.pack(side="top")
        self.button82 = ttk.Button(self)
        self.button82.configure(text="button82")
        self.button82.pack(side="top")
        self.button83 = ttk.Button(self)
        self.button83.configure(text="button83")
        self.button83.pack(side="top")


if __name__ == "__main__":
    root = tk.Tk()
    widget = NewprojectWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
