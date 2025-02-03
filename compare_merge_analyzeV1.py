import tkinter as tk
from tkinter import ttk, filedialog
import ast


class CodeComparatorApp:
    def __init__(self, parent):
        self.parent = parent

        # Options
        self.ignore_whitespace = tk.BooleanVar(value=False)
        self.ignore_case = tk.BooleanVar(value=False)
        self.ignore_comments = tk.BooleanVar(value=False)
        self.ignore_blank_lines = tk.BooleanVar(value=False)
        self.file_history = []

        self.create_widgets()

    def create_widgets(self):
        # Text areas for code input
        self.text1 = tk.Text(self.parent,bd=11,bg="light cyan", height=20, width=50, wrap=tk.NONE)
        self.text1.grid(row=0, column=0, padx=5, pady=5)
        self.text2 = tk.Text(self.parent,bd=11,bg="light yellow", height=20, width=50, wrap=tk.NONE)
        self.text2.grid(row=0, column=1, padx=5, pady=5)

        # Options Checkboxes
        options_frame = tk.Frame(self.parent)
        options_frame.grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Checkbutton(options_frame, text="Ignore Comments", variable=self.ignore_comments).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Ignore Blank Lines", variable=self.ignore_blank_lines).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Ignore Whitespace", variable=self.ignore_whitespace).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Ignore Case", variable=self.ignore_case).pack(side=tk.LEFT, padx=5)

        # Buttons
        btn_frame = tk.Frame(self.parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame,bd=6, bg="cornsilk", text="Load Code 1", command=lambda: self.load_file(self.text1)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="cornsilk", text="Load Code 2", command=lambda: self.load_file(self.text2)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="cornsilk", text="Compare Code", command=self.compare_code).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="cornsilk", text="Save Result", command=self.save_result).pack(side=tk.LEFT, padx=5)

        # Results text area
        self.result_text = tk.Text(self.parent, height=20, width=100, wrap=tk.NONE)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.status_label = ttk.Label(self.parent, text="Active Options: No Options Active")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)

        # Update status whenever options are toggled
        for var in [self.ignore_whitespace, self.ignore_case, self.ignore_comments, self.ignore_blank_lines]:
            var.trace("w", lambda *args: self.update_status())


        self.text1.bind("<KeyRelease>", lambda e: self.auto_compare())
        self.text2.bind("<KeyRelease>", lambda e: self.auto_compare())
        self.history_menu = ttk.Menubutton(self.parent, text="File History", direction="below")
        self.history_menu.grid(row=5, column=0, columnspan=2, pady=5)
        self.history_menu["menu"] = tk.Menu(self.history_menu, tearoff=0)

    def preprocess_code(self, code):
        """Apply options to preprocess the code."""
        if self.ignore_whitespace.get():
            code = [line.strip() for line in code.splitlines()]
        if self.ignore_case.get():
            code = [line.lower() for line in code]
            
        if self.ignore_comments.get():
            processed_code = [line for line in processed_code if not line.strip().startswith("#")]

        # Ignore blank lines
        if self.ignore_blank_lines.get():
            processed_code = [line for line in processed_code if line.strip()]

        return "\n".join(processed_code)


    def compare_code(self):
        """Compare the two pieces of code and highlight differences."""
        code1 = self.text1.get("1.0", tk.END).splitlines()
        code2 = self.text2.get("1.0", tk.END).splitlines()

        code1 = self.preprocess_code(code1)
        code2 = self.preprocess_code(code2)

        result = self.find_differences(code1, code2)

        self.result_text.delete("1.0", tk.END)
        for line in result:
            self.result_text.insert(tk.END, line + "\n")

    def find_differences(self, code1, code2):
        """Identify differences between two code blocks."""
        from difflib import unified_diff
        return list(unified_diff(code1, code2, lineterm=""))

    def load_file(self, text_widget):
        """Load a .py file into the specified text widget."""
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, content)

    def save_result(self):
        """Save the comparison result to a file."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.result_text.get("1.0", tk.END))

    def update_status(self):
        """Update the status label with active options."""
        active_options = []
        if self.ignore_whitespace.get():
            active_options.append("Ignore Whitespace")
        if self.ignore_case.get():
            active_options.append("Ignore Case")
        if self.ignore_comments.get():
            active_options.append("Ignore Comments")
        if self.ignore_blank_lines.get():
            active_options.append("Ignore Blank Lines")

        status_text = " | ".join(active_options) if active_options else "No Options Active"
        self.status_label.config(text=f"Active Options: {status_text}")

    def auto_compare(self):
        """Automatically compare or deduplicate code when edited."""
        self.compare_code()
    def load_file(self, text_widget):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, content)

            # Add to file history
            if file_path not in self.file_history:
                self.file_history.append(file_path)
                self.update_file_history_menu()

    def update_file_history_menu(self):
        pass
    def load_recent_file(self, file_path):
        """Load a file from the history."""
        with open(file_path, "r") as file:
            content = file.read()
            self.text1.delete("1.0", tk.END)
            self.text1.insert(tk.END, content)        
class SemanticDeduplicationApp:
    def __init__(self, parent):
        self.parent = parent
        # Options
        self.ignore_whitespace = tk.BooleanVar(value=False)
        self.ignore_case = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        # Text areas for code input
        self.text1 = tk.Text(self.parent, height=20, width=50, wrap=tk.NONE)
        self.text1.grid(row=0, column=0, padx=5, pady=5)
        self.text2 = tk.Text(self.parent, height=20, width=50, wrap=tk.NONE)
        self.text2.grid(row=0, column=1, padx=5, pady=5)

        # Options Checkboxes
        options_frame = ttk.Frame(self.parent)
        options_frame.grid(row=1, column=0, columnspan=2, pady=5)

        ttk.Checkbutton(options_frame, text="Ignore Whitespace", variable=self.ignore_whitespace).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Ignore Case", variable=self.ignore_case).pack(side=tk.LEFT, padx=5)

        # Buttons
        btn_frame = ttk.Frame(self.parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame,bd=6, bg="cornsilk", text="Load Code 1", command=lambda: self.load_file(self.text1)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="bisque", text="Load Code 2", command=lambda: self.load_file(self.text2)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="alice blue", text="Find Duplicates", command=self.find_duplicates).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame,bd=6, bg="lavender", text="Save Merged Code", command=self.save_merged_code).pack(side=tk.LEFT, padx=5)

        # Listbox to show duplicates
        self.duplicates_listbox = tk.Listbox(self.parent, height=15, width=100)
        self.duplicates_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def preprocess_code(self, code):
        """Apply options to preprocess the code."""
        if self.ignore_whitespace.get():
            code = [line.strip() for line in code.splitlines()]
        if self.ignore_case.get():
            code = [line.lower() for line in code]
        return "\n".join(code)

    def load_file(self, text_widget):
        """Load a .py file into the specified text widget."""
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, content)

    def find_duplicates(self):
        """Find and display duplicates in the Listbox."""
        code1 = self.preprocess_code(self.text1.get("1.0", tk.END))
        code2 = self.preprocess_code(self.text2.get("1.0", tk.END))

        funcs1, classes1 = self.extract_definitions(code1)
        funcs2, classes2 = self.extract_definitions(code2)

        duplicates = []

        # Compare functions
        for func1 in funcs1:
            for func2 in funcs2:
                if self.compare_ast_nodes(func1, func2):
                    duplicates.append(f"Duplicate Function: {func1.name}")

        # Compare classes
        for class1 in classes1:
            for class2 in classes2:
                if self.compare_ast_nodes(class1, class2):
                    duplicates.append(f"Duplicate Class: {class1.name}")

        self.duplicates_listbox.delete(0, tk.END)
        for duplicate in duplicates:
            self.duplicates_listbox.insert(tk.END, duplicate)

        if not duplicates:
            self.duplicates_listbox.insert(tk.END, "No duplicates found.")

    def compare_ast_nodes(self, node1, node2):
        """Compare two AST nodes for equivalence."""
        return ast.dump(node1, annotate_fields=False) == ast.dump(node2, annotate_fields=False)

    def extract_definitions(self, code):
        """Extract functions and classes from Python code as AST nodes."""
        tree = ast.parse(code)
        functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        return functions, classes

    def save_merged_code(self):
        """Save the merged code from the second text widget."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text2.get("1.0", tk.END))
# Main Application with Notebook
class MultiToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Tool Suite")

        # Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        self.code_compare_frm = ttk.Frame(self.notebook)
        self.semantic_dup_frm = ttk.Frame(self.notebook)
        self.notebook.add(self.code_compare_frm, text="compare")
        # Add Code Comparator Tab
        self.tab1 = CodeComparatorApp(self.code_compare_frm)
        

        # Add Semantic Deduplication Tab
        self.notebook.add(self.semantic_dup_frm, text="Semantic Deduplication")

        
        self.tab2 = SemanticDeduplicationApp(self.semantic_dup_frm)
        
        
# Run the application
root = tk.Tk()
app = MultiToolApp(root)
root.mainloop()
