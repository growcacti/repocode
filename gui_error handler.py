import tkinter as tk
from tkinter import filedialog, ttk
import subprocess

class ScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("External Script Runner")
        self.root.geometry("600x400")

        # File selection
        self.file_label = ttk.Label(root, text="Script File:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.file_path_entry = ttk.Entry(root, width=50)
        self.file_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.browse_button = ttk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Run button
        self.run_button = ttk.Button(root, text="Run Script", command=self.run_script)
        self.run_button.grid(row=1, column=1, padx=10, pady=10)

        # Output text box
        self.output_label = ttk.Label(root, text="Output:")
        self.output_label.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

        self.output_text = tk.Text(root, wrap="word", height=15, width=70)
        self.output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.scrollbar.grid(row=3, column=3, sticky="ns", padx=5, pady=5)
        self.output_text.configure(yscrollcommand=self.scrollbar.set)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def run_script(self):
        script_path = self.file_path_entry.get()
        if not script_path:
            self.output_text.insert(tk.END, "Please select a script to run.\n")
            return

        try:
            # Run the script
            result = subprocess.run(
                ["python3", script_path],
                capture_output=True,
                text=True,
                check=True
            )
            # Display output
            self.output_text.insert(tk.END, "Output:\n" + result.stdout + "\n")
        except subprocess.CalledProcessError as e:
            # Display errors
            self.output_text.insert(tk.END, "Error:\n" + e.stderr + "\n")
        except FileNotFoundError as e:
            # Handle invalid script paths
            self.output_text.insert(tk.END, f"FileNotFoundError: {str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
