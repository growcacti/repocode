import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

class DuplicateCodeRemover:
    def __init__(self, root):
        self.root = root
        self.root.title("Duplicate Code Remover")
        
        self.label = tk.Label(root, text="Select a Python file or directory:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.browse_file_button = tk.Button(root, text="Browse File", command=self.browse_file)
        self.browse_file_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.browse_dir_button = tk.Button(root, text="Browse Directory", command=self.browse_directory)
        self.browse_dir_button.grid(row=0, column=3, padx=10, pady=10)
        
        self.recursive_var = tk.BooleanVar()
        self.recursive_checkbutton = tk.Checkbutton(root, text="Recursive", variable=self.recursive_var)
        self.recursive_checkbutton.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        
        self.scan_button = tk.Button(root, text="Scan and Remove Duplicates", command=self.scan_and_remove_duplicates)
        self.scan_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        
        self.summary_text = tk.Text(root, height=15, width=80)
        self.summary_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Output", command=self.save_output)
        self.save_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)        

    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)
    
    def browse_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)
    
    def read_file_with_multiple_encodings(self, file_path):
        encodings = ['utf-8', 'iso-8859-1', 'cp1252']
        for enc in encodings:
            try:
                with open(file_path, 'r', encoding=enc) as file:
                    return file.readlines()
            except UnicodeDecodeError:
                continue
        # If all encodings fail, read with 'ignore' errors
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.readlines()
    
    def scan_and_remove_duplicates(self):
        path = self.path_entry.get()
        if not path:
            messagebox.showerror("Error", "Please select a file or directory.")
            return
        
        if os.path.isfile(path):
            files = [path]
        elif os.path.isdir(path):
            if self.recursive_var.get():
                files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames if f.endswith('.py')]
            else:
                files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.py')]
        else:
            messagebox.showerror("Error", "Invalid file or directory.")
            return
        
        # Create a unique folder for cleaned files
        epoch_time = int(time.time())
        cleaned_folder = os.path.join(os.getcwd(), f"cleaned_duplicates_{epoch_time}")
        os.makedirs(cleaned_folder, exist_ok=True)
        
        summary = ""
        for file in files:
            try:
                lines = self.read_file_with_multiple_encodings(file)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file {file}: {e}")
                continue
            
            unique_lines = []
            duplicates = defaultdict(int)
            for line in lines:
                if line not in unique_lines:
                    unique_lines.append(line)
                else:
                    duplicates[line] += 1
            
            cleaned_file_path = os.path.join(cleaned_folder, f"cleaned_{os.path.basename(file)}")
            with open(cleaned_file_path, 'w', encoding='utf-8') as f:
                f.writelines(unique_lines)
            
            summary += f"File: {file}\n"
            summary += f"Total lines: {len(lines)}\n"
            summary += f"Duplicate lines removed: {sum(duplicates.values())}\n"
            summary += f"Cleaned file saved to: {cleaned_file_path}\n\n"
        
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)
        messagebox.showinfo("Summary", "Duplicate code removal complete. Check the summary for details.")
    def save_output(self):
        output_text = self.summary_text.get(1.0, tk.END).strip()
        if not output_text:
            messagebox.showwarning("Warning", "There is no output to save.")
            return
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(output_text)
                messagebox.showinfo("Success", f"Output saved to {save_path}.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save output: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicateCodeRemover(root)
    root.mainloop()
