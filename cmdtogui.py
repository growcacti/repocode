import tkinter as tk
from tkinter import filedialog
import subprocess

class CommandApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a button to open the file dialog
        self.file_button = tk.Button(self, text="Select File", command=self.select_file)
        self.file_button.grid(row=0, column=0, sticky=tk.W+tk.E)

        # Create a button to run the command
        self.run_button = tk.Button(self, text="Run Command", command=self.run_command)
        self.run_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        # Create a checkbutton
        self.check_var = tk.IntVar()
        self.checkbutton = tk.Checkbutton(self, text="Option", variable=self.check_var)
        self.checkbutton.grid(row=1, columnspan=2)

        # Variable to hold the file path
        self.file_path = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select File")

    def run_command(self):
        if not self.file_path:
            print("No file selected!")
            return

        # Construct the command
        command = ["ls", "-l", self.file_path]
        if self.check_var.get():
            command.append("--color")

        # Execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Print the command output (or error)
        if process.returncode == 0:
            print(output.decode('utf-8'))
        else:
            print(error.decode('utf-8'))

if __name__ == "__main__":
    app = CommandApp()
    app.mainloop()
