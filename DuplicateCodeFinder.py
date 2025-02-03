import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class DuplicateCodeFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Duplicate Code Finder")
        self.root.geometry("800x600")

        # File Selection
        self.label = tk.Label(root, text="Select Python File:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.file_entry = tk.Entry(root, width=60)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Find Duplicates Button
        self.find_button = tk.Button(root, text="Find Duplicates", command=self.find_duplicates)
        self.find_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Results Section
        self.results_label = tk.Label(root, text="Results:")
        self.results_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.results_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
        self.results_box.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def find_duplicates(self):
        file_path = self.file_entry.get().strip()
        if not file_path or not os.path.isfile(file_path):
            messagebox.showerror("Error", "Please select a valid Python file.")
            return

        with open(file_path, "r") as f:
            lines = f.readlines()

        duplicate_blocks = self.detect_duplicates(lines)

        if duplicate_blocks:
            self.display_results(duplicate_blocks)
        else:
            self.results_box.delete(1.0, tk.END)
            self.results_box.insert(tk.END, "No duplicate code blocks found!")

    def detect_duplicates(self, lines):
        seen_blocks = {}
        duplicates = []
        block_size = 3  # Number of lines to treat as a block

        for i in range(len(lines) - block_size + 1):
            block = tuple(lines[i:i + block_size])
            if block in seen_blocks:
                duplicates.append((seen_blocks[block], i, block))
            else:
                seen_blocks[block] = i

        return duplicates

    def display_results(self, duplicate_blocks):
        self.results_box.delete(1.0, tk.END)
        for start_idx, dup_idx, block in duplicate_blocks:
            self.results_box.insert(
                tk.END,
                f"Duplicate Block:\n"
                f"First Occurrence: Line {start_idx + 1}\n"
                f"Duplicate Occurrence: Line {dup_idx + 1}\n"
                "Block Content:\n" + "".join(block) + "\n\n"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicateCodeFinder(root)
    root.mainloop()
