import tkinter as tk
from tkinter import ttk
import importlib

def load_module():
    """Loads the selected module and displays its dir() output."""
    module_name = module_combobox.get()
    try:
        module = importlib.import_module(module_name)
        globals()[module_name] = module
        dir_output = dir(module)
        dir_text.delete("1.0", tk.END)
        dir_text.insert(tk.END, "\n".join(dir_output))
    except Exception as e:
        dir_text.delete("1.0", tk.END)
        dir_text.insert(tk.END, f"Error: {e}")

def display_help(event):
    """Displays help() of the selected item from dir() output."""
    selected_item = dir_text.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
    module_name = module_combobox.get()
    try:
        if module_name in globals():
            module = globals()[module_name]
            help_output = help(getattr(module, selected_item, None))
            help_text.delete("1.0", tk.END)
            help_text.insert(tk.END, help_output)
    except Exception as e:
        help_text.delete("1.0", tk.END)
        help_text.insert(tk.END, f"Error: {e}")

# Create main window
root = tk.Tk()
root.title("Dir and Help Explorer")

# Module selection combobox
module_label = tk.Label(root, text="Select Module:")
module_label.grid(row=0, column=0, sticky="w")

module_combobox = ttk.Combobox(root, values=[
    "os", "sys", "math", "json", "re", "datetime", "tkinter", "random"
])
module_combobox.grid(row=0, column=1, sticky="ew")
module_combobox.set("os")

# Button to load the module and display dir()
load_button = tk.Button(root, text="Load Module", command=load_module)
load_button.grid(row=0, column=2, sticky="ew")

# Dir output section
dir_label = tk.Label(root, text="Dir Output:")
dir_label.grid(row=1, column=0, columnspan=2, sticky="w")

dir_text = tk.Text(root, height=15, width=40)
dir_text.grid(row=2, column=0, columnspan=2, sticky="nsew")
dir_text.bind("<<Selection>>", display_help)

# Help output section
help_label = tk.Label(root, text="Help Output:")
help_label.grid(row=1, column=2, sticky="w")

help_text = tk.Text(root, height=15, width=40)
help_text.grid(row=2, column=2, sticky="nsew")

# Configure grid
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start main loop
root.mainloop()
