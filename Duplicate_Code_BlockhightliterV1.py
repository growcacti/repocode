import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import time
from collections import Counter
import inspect





def scan_files_for_duplicates(directory):
    """ Recursively scan Python files in a directory for duplicate lines of code. """
    duplicate_lines = {}  # Line number -> lines that are duplicate
    files_to_scan = []

    # Recursively find all Python files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                files_to_scan.append(os.path.join(root, file))

    # Read each file and track line frequency
    for file in files_to_scan:
        with open(file, 'r') as f:
            lines = f.readlines()
            line_counter = Counter(lines)
            for line, count in line_counter.items():
                if count > 1:  # If duplicate, store the line
                    if file not in duplicate_lines:
                        duplicate_lines[file] = []
                    duplicate_lines[file].append(line.strip())
    return duplicate_lines

def highlight_duplicates(text_widget, duplicates):
    """ Highlight duplicate lines in the text widget. """
    for file, lines in duplicates.items():
        text_widget.insert(tk.END, f"File: {file}\n")
        for line in lines:
            text_widget.insert(tk.END, line + "\n", "highlight")
        text_widget.insert(tk.END, "\n")

def save_with_timestamp(file_path):
    """ Save a backup file with an epoch timestamp. """
    timestamp = int(time.time())
    file_dir, file_name = os.path.split(file_path)
    new_file_name = f"{timestamp}_{file_name}"
    new_file_path = os.path.join(file_dir, new_file_name)
    
    shutil.copy(file_path, new_file_path)
    return new_file_path

def open_directory():
    """ Open file dialog to select a directory. """
    folder_path = filedialog.askdirectory()
    if folder_path:
        duplicate_lines = scan_files_for_duplicates(folder_path)
        if duplicate_lines:
            messagebox.showinfo("Duplicates Found", "Duplicates detected and highlighted!")
            highlight_duplicates(text_widget, duplicate_lines)
        else:
            messagebox.showinfo("No Duplicates", "No duplicate lines found.")


def save_output():
    """ Save the highlighted output in a new file. """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'w') as f:
                f.write(text_widget.get("1.0", tk.END).strip())
            messagebox.showinfo("Success", f"Output saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")



# Initialize Tkinter window
root = tk.Tk()
root.title("Duplicate Code Finder")

# Set up grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create a Text widget with a scrollbar
text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_widget.grid(row=0, column=0, padx=10, pady=10)

# Tag for highlighting duplicate code
text_widget.tag_configure("highlight", background="yellow", foreground="black")

# Add buttons to open directory and save output
open_button = tk.Button(root, text="Open Directory", command=open_directory)
open_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

save_button = tk.Button(root, text="Save Output", command=save_output)
save_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

root.mainloop()
