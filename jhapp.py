import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Toplevel
import os.path
from pathlib import Path
import runpy


def main():

    try:

        path = Path
        root = tk.Tk()
        top = Toplevel()
        root.geometry("600x700")
        frm2 = ttk.Frame(root, height=40)
        frm2.grid(row=2, column=2, rowspan=10)
        frm11 = ttk.Frame(root, height=20)
        frm11.grid(row=0, column=1)
        frm = ttk.Frame(root, height=50, width=10)
        frm.grid(row=0, column=0, rowspan=7)
        path = "/home/jh/Desktop/VERY_USEFUL_ CODE GUI_EXAMPLES__/"

        def clear():
            lb.delete(0, tk.END)

        def cleartxt():
            text.delete("1.0", tk.END)

        def runpyprg(event):

            file = lb.get(ANCHOR)
            runpy.run_path(path_name=file)

            return

        def opensystem(event):

            x = lb.curselection()[0]

            file = lb.get(x)
            with open(file, "r") as file:
                file = file.read()
                text.delete("1.0", tk.END)
                text.insert(tk.END, file)

                return

        def showcontent(x):

            lb.focus()
            x = lb.curselection()[0]
            file = lb.get(x)
            with open(file, "r") as file:
                file = file.read()
                text.delete("1.0", tk.END)
                text.insert(tk.END, file)

                return

        def newdirlist():
            a = "/home/jh/Desktop/Codeview_Project/"

            path = filedialog.askdirectory(initialdir=a)
            os.chdir(path)
            flist = os.listdir()
            lb.delete(0, tk.END)
            for item in flist:
                lb.insert(tk.END, item)
                return flist

        def path_change():
            path = filedialog.askdirectory()
            lb.delete(0, tk.END)
            flist = os.listdir(path)
            for item in flist:
                lb.insert(tk.END, item)
                return

        lb = tk.Listbox(frm2, height=48, bg="light blue")
        lb.grid(row=0, column=1, rowspan=7, sticky="nswe")
        lb.focus()
        lb.configure(selectmode="")
        flist = os.listdir()
        for item in flist:
            lb.insert(tk.END, item)
        lb.bind("<Double-Button-1>", opensystem)
        lb.bind("<<ListboxSelect>>", showcontent)
        lb.bind("<Double-Button-2>", runpyprg)

        def loadlist1():
            flist = os.listdir()
            for item in flist:
                lb.insert(tk.END, item)

        text = tk.Text(top, height=48, width=150)
        text.grid(row=0, column=0)
        btn4 = tk.Button(frm, text="loadlist1", command=loadlist1)
        btn4.grid(column=0, row=7)
        btn5 = tk.Button(frm, text="Run", command=runpyprg)
        btn5.grid(column=0, row=8)
        btn7 = tk.Button(frm, text="CLR LB", command=clear)
        btn7.grid(column=0, row=11)
        btn8 = tk.Button(frm, text="Clear Text", command=cleartxt)
        btn8.grid(column=0, row=12)
    except Exception as ex:
        text.insert(tk.END, ex)

    root.mainloop()


if __name__ == "__main__":

    main()
