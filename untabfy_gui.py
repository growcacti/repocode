import os
import sys
import tokenize
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    root = tk.Tk()
    app = TabReplacerApp(root)
    root.mainloop()

class TabReplacerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tab to Space Replacer")

        self.tabsize = tk.IntVar(value=4)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tab_label = tk.Label(frame, text="Tab Width:")
        tab_label.grid(row=0, column=0, sticky=tk.W)

        tab_entry = tk.Entry(frame, textvariable=self.tabsize)
        tab_entry.grid(row=0, column=1, padx=5)

        select_button = tk.Button(frame, text="Select Files", command=self.select_files)
        select_button.grid(row=1, column=0, columnspan=2, pady=5)

        self.file_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
        self.file_listbox.grid(row=2, column=0, columnspan=2, pady=5)

        process_button = tk.Button(frame, text="Replace Tabs", command=self.replace_tabs)
        process_button.grid(row=3, column=0, columnspan=2, pady=5)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("Python Files", "*.py"), ("All Files", "*.*"))
        )
        for file_path in file_paths:
            self.file_listbox.insert(tk.END, file_path)

    def replace_tabs(self):
        tabsize = self.tabsize.get()
        selected_files = self.file_listbox.get(0, tk.END)

        if not selected_files:
            messagebox.showwarning("Warning", "No files selected.")
            return

        for filename in selected_files:
            self.process(filename, tabsize)

        messagebox.showinfo("Info", "Tab replacement completed.")

    def process(self, filename, tabsize):
        try:
            with tokenize.open(filename) as f:
                text = f.read()
                encoding = f.encoding
        except IOError as msg:
            print(f"{filename}: I/O error: {msg}")
            return

        newtext = text.expandtabs(tabsize)
        if newtext == text:
            return

        backup = filename + "~"
        try:
            os.unlink(backup)
        except OSError:
            pass
        try:
            os.rename(filename, backup)
        except OSError:
            pass

        with open(filename, "w", encoding=encoding) as f:
            f.write(newtext)

        print(filename)

if __name__ == '__main__':
    main()
