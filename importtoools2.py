import os
import ast
import shutil
import time
from tkinter import Tk, Button, Label, filedialog, ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt

class DependencyOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Script Dependency Organizer")
        self.root.geometry("800x600")

        self.folder_path = None
        self.dependencies = {}
        self.error_files = []  # To store files with errors
        self.starting_scripts = []  # To store scripts with `if __name__ == '__main__'`

        # GUI Layout
        Label(root, text="Select Folder to Scan:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Button(root, text="Browse", command=self.browse_folder).grid(row=0, column=1, padx=10, pady=10)

        Button(root, text="Start Scan", command=self.start_scan).grid(row=1, column=0, padx=10, pady=10)
        Button(root, text="Organize Files", command=self.organize_files).grid(row=1, column=1, padx=10, pady=10)
        Button(root, text="View Import Graph", command=self.view_graph).grid(row=1, column=2, padx=10, pady=10)

        Label(root, text="Connected File Groups:", font=("Arial", 12)).grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.tree = ttk.Treeview(root, columns=("Group"), show="headings", height=10)
        self.tree.heading("Group", text="Connected File Groups")
        self.tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        Label(root, text="Skipped Files (Errors):", font=("Arial", 12)).grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        self.error_list = ttk.Treeview(root, columns=("Errors"), show="headings", height=5)
        self.error_list.heading("Errors", text="Files with Errors")
        self.error_list.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def browse_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder")
        if self.folder_path:
            messagebox.showinfo("Folder Selected", f"Selected Folder: {self.folder_path}")

    def start_scan(self):
        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        self.dependencies, self.starting_scripts = self.scan_dependencies(self.folder_path)
        self.display_results()

        if not self.dependencies:
            messagebox.showwarning("Warning", "No valid Python files with imports found.")

    def scan_dependencies(self, folder):
        dependencies = {}
        starting_scripts = []
        self.error_files = []  # Clear previous errors

        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    try:
                        # Compile the file to check for syntax errors before parsing
                        with open(filepath, "r") as f:
                            content = f.read()
                            compile(content, filepath, "exec")
                        
                        # Parse with AST
                        file_deps, has_main = self.get_imports(filepath, folder)
                        if has_main:
                            starting_scripts.append(filepath)
                        if file_deps:
                            dependencies[filepath] = file_deps
                    except (SyntaxError, IndentationError) as e:
                        self.error_files.append((filepath, str(e)))
        return dependencies, starting_scripts

    def get_imports(self, filepath, base_dir):
        """
        Extracts and resolves imports for a given Python file.
        """
        imports = set()
        has_main = False
        with open(filepath, "r") as file:
            try:
                tree = ast.parse(file.read(), filename=filepath)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imports.add(self.resolve_import(alias.name, base_dir))
                    elif isinstance(node, ast.ImportFrom) and node.module:
                        imports.add(self.resolve_import(node.module, base_dir))
                    elif isinstance(node, ast.If):
                        if getattr(node.test, 'left', None) and isinstance(node.test.left, ast.Name):
                            if node.test.left.id == "__name__" and isinstance(node.test.comparators[0], ast.Str):
                                if node.test.comparators[0].s == "__main__":
                                    has_main = True
            except Exception as e:
                print(f"Skipping file due to unexpected error: {filepath}\nError: {e}")
        return imports, has_main

    def resolve_import(self, module_name, base_dir):
        """
        Resolves the file path for a given module name starting from base_dir.
        """
        module_path = module_name.replace(".", os.sep) + ".py"
        for root, _, files in os.walk(base_dir):
            if module_path in files:
                return os.path.join(root, module_path)
        return module_name

    def organize_files(self):
        if not self.dependencies:
            messagebox.showerror("Error", "No dependencies to organize. Please scan first.")
            return

        graph = self.build_dependency_graph(self.dependencies)
        groups = list(nx.connected_components(graph.to_undirected()))

        for idx, group in enumerate(groups):
            folder_name = f"group_{idx + 1}_{int(time.time())}"
            dest_folder = os.path.join(self.folder_path, folder_name)
            os.makedirs(dest_folder, exist_ok=True)
            for filepath in group:
                shutil.copy(filepath, dest_folder)

        messagebox.showinfo("Success", "Files organized into groups.")
        self.display_results()

    def build_dependency_graph(self, dependencies):
        graph = nx.DiGraph()
        for file, imports in dependencies.items():
            graph.add_node(file)
            for imp in imports:
                for other_file in dependencies:
                    if other_file != file and os.path.basename(other_file).startswith(imp):
                        graph.add_edge(file, other_file)
        return graph

    def display_results(self):
        self.tree.delete(*self.tree.get_children())
        self.error_list.delete(*self.error_list.get_children())

        if self.dependencies:
            graph = self.build_dependency_graph(self.dependencies)
            groups = list(nx.connected_components(graph.to_undirected()))
            for idx, group in enumerate(groups):
                self.tree.insert("", "end", values=(f"Group {idx + 1}: {', '.join(group)}"))

        for file, error in self.error_files:
            self.error_list.insert("", "end", values=(f"{file} - {error}"))

        print("Starting Scripts:", self.starting_scripts)

    def view_graph(self):
        if not self.dependencies:
            messagebox.showerror("Error", "No dependencies to visualize. Please scan first.")
            return

        graph = self.build_dependency_graph(self.dependencies)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_color="lightblue", font_weight="bold")
        plt.show()


if __name__ == "__main__":
    root = Tk()
    app = DependencyOrganizer(root)
    root.mainloop()
