import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
import os
import datetime

class FindReplaceApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Find and Replace Application")
        
        # GUI Components
        self.setup_gui()

    def setup_gui(self):
        # Frame for control widgets
        self.control_frame = tk.Frame(self.parent)
        self.control_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # Select Directory Button
        select_button = tk.Button(self.control_frame, text="Select Directory", command=self.select_directory)
        select_button.grid(row=0, column=0, padx=10, pady=5)

        # Directory Label
        self.directory_label = tk.Label(self.control_frame, text="Select a directory", fg="blue")
        self.directory_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Find and Replace Entries
        self.setup_find_replace_entries()

        # Spinbox for skipping lines
        tk.Label(self.control_frame, text="Skip Lines:").grid(row=6, column=0, sticky='e', padx=10)
        self.skip_lines_spinbox = tk.Spinbox(self.control_frame, from_=0, to=10, width=5)
        self.skip_lines_spinbox.grid(row=6, column=1, padx=10, pady=5)

        # Buttons
        self.setup_buttons()

        # List Box
        self.list_box = Listbox(self.parent, width=80, height=20)
        self.list_box.grid(row=0, column=1, rowspan=6, padx=10, pady=10)

    def setup_find_replace_entries(self):
        tk.Label(self.control_frame, text="Find:").grid(row=2, column=0, sticky='e', padx=10)
        self.find_entry = tk.Entry(self.control_frame)
        self.find_entry.grid(row=2, column=1, padx=10)

        tk.Label(self.control_frame, text="Replace With:").grid(row=3, column=0, sticky='e', padx=10)
        self.replace_entry = tk.Entry(self.control_frame)
        self.replace_entry.grid(row=3, column=1, padx=10)

    def setup_buttons(self):
        find_button = tk.Button(self.control_frame, text="Find", command=self.find_in_files)
        find_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        replace_button = tk.Button(self.control_frame, text="Replace", command=lambda: self.find_in_files(True))
        replace_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        skiplines_button = tk.Button(self.control_frame, text="Skip # Line Replace", command=self.skip_line_replace)
        skiplines_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_label.config(text=directory)

    def skip_line_replace(self):
        skip_lines = int(self.skip_lines_spinbox.get())
        self.find_in_files(replace=True, skip_lines=skip_lines)

    def find_in_files(self, replace=False, skip_lines=0):
        directory = self.directory_label.cget("text")
        find_word = self.find_entry.get()
        replace_word = self.replace_entry.get() if replace else None

        self.list_box.delete(0, tk.END)  # Clear existing entries in the list box

        if replace:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_directory = os.path.join(directory, f"Modified_Files_{timestamp}")
            os.makedirs(output_directory, exist_ok=True)

        for parent, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(parent, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='ISO-8859-1') as f:
                            lines = f.readlines()
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while processing {file_path}: {e}")
                        continue

                occurrences = 0
                new_lines = []
                for i, line in enumerate(lines):
                    if i % (skip_lines + 1) == 0:  # Only process lines based on skip_lines
                        count = line.count(find_word)
                        occurrences += count
                        if replace and replace_word:
                            line = line.replace(find_word, replace_word)
                    new_lines.append(line)
                
                if occurrences > 0:
                    if replace and replace_word:
                        new_file_path = os.path.join(output_directory, os.path.relpath(file_path, directory))
                        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                        with open(new_file_path, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                        self.list_box.insert(tk.END, f"{file}: Replaced {occurrences} occurrences")
                    else:
                        self.list_box.insert(tk.END, f"{file}: Found {occurrences} occurrences")

if __name__ == '__main__':
    root = tk.Tk()
    app = FindReplaceApp(root)
    root.mainloop()
