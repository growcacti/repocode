import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def reformat_code_with_tkinter():
    # Setup the root Tkinter window
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing

    # Show an "Open" dialog box and return the path to the selected directory
    directory = filedialog.askdirectory()  # users can select the directory here

    if directory:  # Proceed only if the user selected a directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    result = subprocess.run(["python", "-m", "black", filepath], capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"Successfully formatted: {filepath}")
                        print(result.stdout)
                    else:
                        print(f"Error occurred while formatting: {filepath}")
                        print(result.stderr)

# Usage
reformat_code_with_tkinter()
