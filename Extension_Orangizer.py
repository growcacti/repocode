
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

class ExtensionOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x750")
        self.directory = tk.StringVar()
        self.ignore_extensions = tk.StringVar()
        self.extension_counts = defaultdict(int)
        self.recursive = tk.BooleanVar(value=False)
        self.timestamp = None  # To store the shared timestamp
        self.create_widgets()

    def create_widgets(self):
        # Directory selection
        tk.Label(self.root, text="Select Directory:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, bd=11, bg="light cyan", textvariable=self.directory, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, bd=5, bg="orange", text="Browse Directory", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.root, bd=3, bg="skyblue", text="Load from File", command=self.load_from_file).grid(row=0, column=3, padx=10, pady=10)

        # Ignore Extensions
        tk.Label(self.root, text="Ignore Extensions (comma-separated):").grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, bd=8, bg="thistle", textvariable=self.ignore_extensions, width=50).grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        # Recursive option
        tk.Checkbutton(self.root, text="Include Subdirectories", variable=self.recursive).grid(row=2, column=0, columnspan=3, sticky="w", padx=10)

        # Buttons
        tk.Button(self.root, bd=7, bg="MistyRose2", text="Count Extensions", command=self.count_extensions).grid(row=3, column=0, columnspan=4, pady=10)
        tk.Button(self.root, bd=8, bg="RosyBrown1", text="Make Folders", command=self.make_folders).grid(row=4, column=0, columnspan=4, pady=10)
        tk.Button(self.root, bd=9, bg="plum3", text="Copy Files", command=self.copy_files).grid(row=5, column=0, columnspan=4, pady=10)

        # Results area
        self.result_text = tk.Text(self.root, bd=12, bg="alice blue", width=80, height=15)
        self.result_text.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory.set(directory)

    def load_from_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            directory = os.path.dirname(file_path)
            self.directory.set(directory)

    def count_extensions(self):
        self.extension_counts.clear()
        directory = self.directory.get()
        ignore_list = [ext.strip().lower() for ext in self.ignore_extensions.get().split(",")]

        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Please select a valid directory.")
            return

        for root_dir, _, files in os.walk(directory) if self.recursive.get() else [(directory, None, os.listdir(directory))]:
            for file in files:
                _, ext = os.path.splitext(file)
                ext = ext.lower()
                if ext and ext not in ignore_list:
                    self.extension_counts[ext] += 1

        self.display_results()

    def display_results(self):
        self.result_text.delete(1.0, tk.END)
        if not self.extension_counts:
            self.result_text.insert(tk.END, "No files found with extensions.\n")
        else:
            for ext, count in self.extension_counts.items():
                self.result_text.insert(tk.END, f"{ext}: {count}\n")

    def make_folders(self):
        directory = self.directory.get()
        if not directory or not self.extension_counts:
            messagebox.showerror("Error", "Please count extensions first.")
            return

        self.timestamp = int(time.time())  # Generate a single timestamp for this session
        for ext in self.extension_counts:
            folder_name = f"{ext[1:]}_{self.timestamp}"  # Use the same timestamp
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

        messagebox.showinfo("Success", "Folders created successfully.")

    def copy_files(self):
        directory = self.directory.get()
        if not directory or not self.extension_counts or not self.timestamp:
            messagebox.showerror("Error", "Please count extensions and create folders first.")
            return

        for root_dir, _, files in os.walk(directory) if self.recursive.get() else [(directory, None, os.listdir(directory))]:
            for file in files:
                _, ext = os.path.splitext(file)
                ext = ext.lower()
                if ext in self.extension_counts:
                    folder_name = f"{ext[1:]}_{self.timestamp}"  # Use the same timestamp
                    folder_path = os.path.join(directory, folder_name)
                    shutil.copy2(os.path.join(root_dir, file), os.path.join(folder_path, file))

        messagebox.showinfo("Success", "Files copied successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExtensionOrganizer(root)
    root.mainloop()
