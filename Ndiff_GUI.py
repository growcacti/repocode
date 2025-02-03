import tkinter as tk
from tkinter import filedialog, messagebox
import difflib

class NDiffGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NDiff GUI")
        
        self.file1 = None
        self.file2 = None
        
        # StringVars for file paths
        self.file1_var = tk.StringVar()
        self.file2_var = tk.StringVar()

        # Labels
        tk.Label(root, text="File 1:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="File 2:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        # Entry widgets
        self.file1_entry = tk.Entry(root, textvariable=self.file1_var, width=50)
        self.file1_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")
        self.file1_var.trace_add("write", lambda *args: self.adjust_entry_width(self.file1_entry, self.file1_var))

        self.file2_entry = tk.Entry(root, textvariable=self.file2_var, width=50)
        self.file2_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")
        self.file2_var.trace_add("write", lambda *args: self.adjust_entry_width(self.file2_entry, self.file2_var))
        
        # Browse buttons
        tk.Button(root, text="Browse", command=self.browse_file1).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(root, text="Browse", command=self.browse_file2).grid(row=1, column=2, padx=10, pady=5)
        
        # Run button
        tk.Button(root, text="Compare", command=self.compare_files).grid(row=2, column=1, pady=10)
        
        # Save button
        tk.Button(root, text="Save Result", command=self.save_result).grid(row=2, column=2, pady=10)
        
        # Text widget for output
        self.output_text = tk.Text(root, wrap="word", height=20, width=80)
        self.output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        
        # Configure grid weights
        root.columnconfigure(1, weight=1)

    def browse_file1(self):
        self.file1 = filedialog.askopenfilename(title="Select File 1")
        self.file1_var.set(self.file1)

    def browse_file2(self):
        self.file2 = filedialog.askopenfilename(title="Select File 2")
        self.file2_var.set(self.file2)

    def adjust_entry_width(self, entry_widget, string_var):
        path_length = len(string_var.get())
        entry_widget.config(width=max(50, path_length))

    def compare_files(self):
        file1_path = self.file1_var.get()
        file2_path = self.file2_var.get()

        if not file1_path or not file2_path:
            messagebox.showerror("Error", "Both file paths must be provided.")
            return

        try:
            with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
                file1_lines = f1.readlines()
                file2_lines = f2.readlines()

            diff = difflib.ndiff(file1_lines, file2_lines)

            self.output_text.delete(1.0, tk.END)
            for line in diff:
                self.output_text.insert(tk.END, line)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_result(self):
        result = self.output_text.get(1.0, tk.END).strip()
        if not result:
            messagebox.showerror("Error", "No result to save.")
            return

        save_path = filedialog.asksaveasfilename(title="Save Result As", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if save_path:
            try:
                with open(save_path, 'w') as file:
                    file.write(result)
                messagebox.showinfo("Success", "Result saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NDiffGUI(root)
    root.mainloop()
