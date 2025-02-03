import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime

class FileDirectoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File and Directory Manager")

        self.current_directory = os.getcwd()  # Get the current working directory

        # Create the GUI components
        tk.Label(root, text="Enter filenames (comma-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter directory names (comma-separated):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.dir_entry = tk.Entry(root, width=50)
        self.dir_entry.grid(row=1, column=1, padx=10, pady=5)

        self.create_button = tk.Button(root, text="Create Files/Directories", command=self.create_files_directories)
        self.create_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.feedback_text = tk.Text(root, height=10, width=60)
        self.feedback_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.read_file_button = tk.Button(root, text="Read CSV and Remove Duplicates", command=self.read_file_and_remove_duplicates)
        self.read_file_button.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Current Directory:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.directory_label = tk.Label(root, text=self.current_directory, anchor="w")
        self.directory_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.change_dir_button = tk.Button(root, text="Change Directory", command=self.change_directory)
        self.change_dir_button.grid(row=6, column=0, columnspan=2, pady=10)

    def create_files_directories(self):
        self.feedback_text.delete('1.0', tk.END)
        filenames = self.file_entry.get().split(',')
        dirnames = self.dir_entry.get().split(',')

        for name in filenames:
            if name.strip():  # Ensure the name is not empty
                try:
                    with open(os.path.join(self.current_directory, name.strip()), 'w') as f:
                        pass  # Just create the file if it doesn't exist
                    self.feedback_text.insert(tk.END, f"File created: {name.strip()}\n")
                except Exception as e:
                    self.feedback_text.insert(tk.END, f"Failed to create file {name.strip()}: {e}\n")

        for name in dirnames:
            if name.strip():  # Ensure the name is not empty
                try:
                    os.makedirs(os.path.join(self.current_directory, name.strip()), exist_ok=True)
                    self.feedback_text.insert(tk.END, f"Directory created: {name.strip()}\n")
                except Exception as e:
                    self.feedback_text.insert(tk.END, f"Failed to create directory {name.strip()}: {e}\n")

    def read_file_and_remove_duplicates(self):
        filepath = filedialog.askopenfilename(filetypes=[("Comma Separated Values", "*.csv"), ("All Files", "*.*")])
        if not filepath:
            return

        custom_string = ''

        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()

            cleaned_lines = [line.strip() for line in lines if line.strip()]
            unique_lines = list(set(cleaned_lines))

            # Generating a unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"{custom_string}_{timestamp}.csv"

            # Create a list with formatted items
            formatted_items = [f"{custom_string}_{timestamp}_{item}" for item in unique_lines]

            with open(os.path.join(self.current_directory, output_filename), 'w') as file:
                for item in formatted_items:
                    file.write(f"{item}\n")

            self.feedback_text.insert(tk.END, f"Unique entries written to {output_filename}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file and remove duplicates: {e}")

    def change_directory(self):
        new_directory = filedialog.askdirectory()
        if new_directory:
            self.current_directory = new_directory
            self.directory_label.config(text=self.current_directory)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDirectoryApp(root)
    root.mainloop()
