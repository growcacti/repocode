import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Menu


class TkGuiGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("TK GUI Generator with Live Preview & Variable Binding")
        self.top = None  # Preview Window
        self.create_toplevel()

        # Track current grid position
        self.current_row = 0
        self.current_column = 0
        self.max_columns = 3

        # Default boilerplate code
        self.prefix_boilerplate = """# Auto-generated Script\nimport tkinter as tk\nfrom tkinter import ttk\n\nroot = tk.Tk()\n"""
        self.suffix_boilerplate = """\nroot.mainloop()\n"""

        # Tkinter variable options
        self.variable_types = {
            "StringVar": "tk.StringVar()",
            "IntVar": "tk.IntVar()",
            "DoubleVar": "tk.DoubleVar()",
            "BooleanVar": "tk.BooleanVar()",
        }

        self.setup_ui()

    def create_toplevel(self):
        """Create or recreate the Preview Window."""
        if self.top is None or not self.top.winfo_exists():
            self.top = tk.Toplevel(self.root)
            self.top.title("Widget Preview")
            self.top.protocol("WM_DELETE_WINDOW", self.on_toplevel_close)

            self.preview_frame = tk.LabelFrame(self.top, text="Live Widget Preview")
            self.preview_frame.pack(padx=10, pady=10, fill="both", expand=True)

            self.preview_area = tk.Frame(self.preview_frame)
            self.preview_area.pack(fill="both", expand=True)

    def on_toplevel_close(self):
        """Handle the Preview Window close event."""
        self.top.destroy()
        self.top = None

    def setup_ui(self):
        """Set up the main UI layout."""
        self.create_toplevel()

        selection_frame = tk.LabelFrame(self.root, text="Widget Properties")
        selection_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Widget type selection
        tk.Label(selection_frame, text="Widget Type:").grid(row=0, column=0, sticky="w")
        self.widget_type_combo = ttk.Combobox(
            selection_frame, values=["Entry", "Button", "ComboBox", "CheckButton", "Scale", "Label", "Spinbox"]
        )
        self.widget_type_combo.grid(row=0, column=1, sticky="ew")
        self.widget_type_combo.set("Entry")

        # Text Entry
        tk.Label(selection_frame, text="Text:").grid(row=1, column=0, sticky="w")
        self.text_entry = tk.Entry(selection_frame)
        self.text_entry.grid(row=1, column=1, sticky="ew")

        # Width & Height
        tk.Label(selection_frame, text="Width:").grid(row=2, column=0, sticky="w")
        self.width_spin = ttk.Spinbox(selection_frame, from_=5, to=500, width=5)
        self.width_spin.grid(row=2, column=1)
        self.width_spin.insert(0, "10")

        tk.Label(selection_frame, text="Height:").grid(row=3, column=0, sticky="w")
        self.height_spin = ttk.Spinbox(selection_frame, from_=1, to=50, width=5)
        self.height_spin.grid(row=3, column=1)
        self.height_spin.insert(0, "5")

        # Background & Foreground Colors
        tk.Label(selection_frame, text="Background:").grid(row=4, column=0, sticky="w")
        self.bg_var = tk.StringVar(value="white")
        ttk.Combobox(selection_frame, textvariable=self.bg_var, values=["white", "gray", "blue", "red"]).grid(row=4, column=1)

        tk.Label(selection_frame, text="Foreground:").grid(row=5, column=0, sticky="w")
        self.fg_var = tk.StringVar(value="black")
        ttk.Combobox(selection_frame, textvariable=self.fg_var, values=["black", "white", "green", "purple"]).grid(row=5, column=1)

        # Relief & Border
        tk.Label(selection_frame, text="Relief:").grid(row=6, column=0, sticky="w")
        self.relief_combo = ttk.Combobox(selection_frame, values=["flat", "raised", "sunken", "groove", "ridge"])
        self.relief_combo.grid(row=6, column=1)
        self.relief_combo.set("flat")

        tk.Label(selection_frame, text="Border Width:").grid(row=7, column=0, sticky="w")
        self.border_spin = ttk.Spinbox(selection_frame, from_=1, to=10, width=5)
        self.border_spin.grid(row=7, column=1)
        self.border_spin.insert(0, "2")

        # Variable Binding
        self.use_variable = tk.BooleanVar(value=False)
        self.variable_type = tk.StringVar(value="StringVar")

        tk.Checkbutton(selection_frame, text="Use Tkinter Variable", variable=self.use_variable).grid(row=8, column=0, sticky="w")
        ttk.Combobox(selection_frame, textvariable=self.variable_type, values=list(self.variable_types.keys())).grid(row=8, column=1, sticky="ew")

        # Buttons
        tk.Button(selection_frame, text="Add Widget", command=self.generate_code).grid(row=9, column=0, columnspan=2, pady=5)
        tk.Button(selection_frame, text="Clear Preview", command=self.clear_preview).grid(row=10, column=0, columnspan=2, pady=5)

        # Code Display Areacky="nsew")
        self.preview_frame = tk.LabelFrame(self.top, text="Widget Preview")
        self.preview_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Use a frame as a container for preview widgets
        code_frame = tk.Frame(self.root)
        code_frame.grid(row=2, column=4, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.canvas= tk.Canvas(code_frame, width=50,height=44)
        self.canvas.grid(row=2,column=6)

        self.code_text = ScrolledText(self.canvas, height=30, width=50)
        self.code_text.grid(row=8,column=2, padx=10, pady=10)








    def generate_code(self):
        """Generate widget and display its code."""
        self.create_toplevel()
        widget_type = self.widget_type_combo.get()
        text = self.text_entry.get()
        width = int(self.width_spin.get())
        height = int(self.height_spin.get())
        bg = self.bg_var.get()
        fg = self.fg_var.get()
        relief = self.relief_combo.get()
        bd = int(self.border_spin.get())
        use_var = self.use_variable.get()
        var_type = self.variable_type.get()

        widget, code, var_code = None, "", ""

        # Handle variable binding
        if use_var:
            var_name = f"var_{self.current_row}_{self.current_column}"
            var_code = f"{var_name} = {self.variable_types[var_type]}\n"
        else:
            var_name = ""

        # Generate widget code
        if widget_type == "Entry":
            code = f'tk.Entry(root, width={width}, bg="{bg}", fg="{fg}", bd={bd}, relief="{relief}", textvariable={var_name}).grid(row={self.current_row}, column={self.current_column})'
            widget = tk.Entry(self.preview_area, width=width, bg=bg, fg=fg, bd=bd, relief=relief, textvariable=tk.StringVar() if use_var else None)
        elif widget_type == "CheckButton":
            code = f'tk.Checkbutton(root, text="{text}", variable={var_name}).grid(row={self.current_row}, column={self.current_column})'
            widget = tk.Checkbutton(self.preview_area, text=text, variable=tk.BooleanVar() if use_var else None)
        elif widget_type == "Label":
            code = f'tk.Label(root, text="{text}", bg="{bg}", fg="{fg}", font=("Arial", 12)).grid(row={self.current_row}, column={self.current_column})'
            widget = tk.Label(self.preview_area, text=text, bg=bg, fg=fg, font=("Arial", 12))
        
        widget.grid(row=self.current_row, column=self.current_column, padx=5, pady=5)
        self.code_text.insert(tk.END, (var_code if use_var else "") + code + "\n")

        # Update position
        self.current_column += 1
        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1

    def clear_preview(self):
        """Clear preview area."""
        for widget in self.preview_area.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TkGuiGenerator(root)
    root.mainloop()
