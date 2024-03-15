# Example dictionary
files_dict = {
    'file1': 1,
    'file2': 2,
    'file3': 3,
}

# Increment each value in the dictionary
increment_value = 1  # This is the value by which you want to increment the dictionary values
for key in files_dict:
    files_dict[key] += increment_value

print(files_dict)
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    filepath = filedialog.askopenfilename()
    if filepath:
        path_label.config(text=filepath)

# Create the main window
root = tk.Tk()
root.title("File Path Finder")

# Create a button to open the file dialog
open_file_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_file_button.grid(row=0, column=0, padx=10, pady=10)

# Create a label to display the selected file path
path_label = tk.Label(root, text="No file selected")
path_label.grid(row=1, column=0, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
import os

def get_files_in_directory_to_dict(directory_path):
    files_dict = {}
    # List all files in the given directory
    for filename in os.listdir(directory_path):
        # Check if the current item is a file
        if os.path.isfile(os.path.join(directory_path, filename)):
            files_dict[filename] = os.path.join(directory_path, filename)
    return files_dict

# Specify the directory path here
directory_path = '/path/to/your/directory'
files_dict = get_files_in_directory_to_dict(directory_path)
print(files_dict)
