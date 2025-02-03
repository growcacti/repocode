import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import autopep8
import black
import linter
class CodeFormatterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Formatter and Linter")
        
        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid expansion
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Create tabs
        self._create_original_code_tab()
        self._create_formatted_code_tab()
        self._create_linter_output_tab()
    
    def _create_original_code_tab(self):
        """Create the Original Code tab."""
        tab_original = ttk.Frame(self.notebook)
        self.notebook.add(tab_original, text="Original Code")
        
        tab_original.rowconfigure(0, weight=1)
        tab_original.columnconfigure(0, weight=1)
        
        self.text_original = tk.Text(tab_original, wrap="word")
        self.text_original.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        btn_load = tk.Button(tab_original, text="Load Code", command=self.load_file)
        btn_load.grid(row=1, column=0, pady=5)

    def _create_formatted_code_tab(self):
        """Create the Formatted Code tab."""
        tab_formatted = ttk.Frame(self.notebook)
        self.notebook.add(tab_formatted, text="Formatted Code")
        
        tab_formatted.rowconfigure(0, weight=1)
        tab_formatted.columnconfigure(0, weight=1)
        
        self.text_formatted = tk.Text(tab_formatted, wrap="word", state="normal")
        self.text_formatted.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        btn_black = tk.Button(tab_formatted, text="Format with Black", command=self.format_with_black)
        btn_black.grid(row=1, column=0, padx=5, pady=5)
        
        btn_autopep8 = tk.Button(tab_formatted, text="Format with Autopep8", command=self.format_with_autopep8)
        btn_autopep8.grid(row=1, column=1, padx=5, pady=5)

    def _create_linter_output_tab(self):
        """Create the Linter Output tab."""
        tab_linter = ttk.Frame(self.notebook)
        self.notebook.add(tab_linter, text="Linter Output")
        
        tab_linter.rowconfigure(0, weight=1)
        tab_linter.columnconfigure(0, weight=1)
        
        self.text_linter = tk.Text(tab_linter, wrap="word", state="normal")
        self.text_linter.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        btn_lint = tk.Button(tab_linter, text="Run Linter", command=self.run_linter)
        btn_lint.grid(row=1, column=0, pady=5)

    def load_file(self):
        """Load a Python file into the Original Code tab."""
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_original.delete("1.0", tk.END)
                self.text_original.insert("1.0", file.read())

    def format_with_black(self):
        """Format code using Black and display it in the Formatted Code tab."""
        self._update_output(self.text_original, self.text_formatted, self._format_with_black)

    def format_with_autopep8(self):
        """Format code using Autopep8 and display it in the Formatted Code tab."""
        self._update_output(self.text_original, self.text_formatted, self._format_with_autopep8)

    def run_linter(self):
        """Run a linter on the code and display the output in the Linter Output tab."""
        self._update_output(self.text_original, self.text_linter, self._lint_code)

    def _update_output(self, input_text, output_text, processor):
        """Update the output tab with processed results."""
        original_code = input_text.get("1.0", tk.END).strip()
        if not original_code:
            messagebox.showerror("Error", "No code to process!")
            return
        try:
            result = processor(original_code)
            output_text.delete("1.0", tk.END)
            output_text.insert("1.0", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _format_with_black(self, code):
        """Format code using Black."""
        try:
            formatted_code = subprocess.run(
                ["black", "-", "--fast"],
                input=code.encode("utf-8"),
                capture_output=True,
                text=True,
                check=True
            ).stdout
            return formatted_code
        except subprocess.CalledProcessError as e:
            return e.stderr

    def _format_with_autopep8(self, code):
        """Format code using Autopep8."""
        return autopep8.fix_code(code)

    def _lint_code(self, code):
        """Run a linter (pylint) on the code."""
        try:
            process = subprocess.run(
                ["pylint", "-"],
                input=code.encode("utf-8"),
                capture_output=True,
                text=True
            )
            return process.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr


if __name__ == "__main__":
    root = tk.Tk()
    app = CodeFormatterApp(root)
    root.mainloop()
