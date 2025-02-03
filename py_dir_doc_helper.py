import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.scrolledtext as st
import os


class PyDDViewer:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
        self.load_files_from_directory()

    def create_widgets(self):
        # Listbox for files in the Module_Help folder
        self.lb = tk.Listbox(self.root, bd=15, bg="light cyan", height=45, width=35)
        self.lb.grid(row=0, column=0, rowspan=4, sticky="nsw")
        self.lb.bind("<<ListboxSelect>>", self.display_selected_file)

        # Text widget to display the file contents
        self.textwidget = st.ScrolledText(
            self.root, bd=12, bg="alice blue", wrap="word", height=45, width=160
        )
        self.textwidget.grid(row=0, column=1, rowspan=4, sticky="nsw")

        # Button to clear text widget
        self.clr_button = tk.Button(self.root, bd=5, bg="orange", text="Clear", command=self.clear)
        self.clr_button.grid(row=4, column=0)

        # Button to save file
        self.save_btn = tk.Button(self.root, bd=5, bg="azure", text="Save to File", command=self.save_file)
        self.save_btn.grid(row=4, column=1)

    def load_files_from_directory(self):
        """Load all text files from the Module_Help directory into the Listbox."""
        directory = "Module_Help"
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the directory if it doesn't exist

        # Clear the Listbox
        self.lb.delete(0, tk.END)

        # Add text files to the Listbox
        for file in os.listdir(directory):
            if file.endswith(".txt"):  # Only list .txt files
                self.lb.insert(tk.END, file)

    def display_selected_file(self, event):
        """Display the contents of the selected file in the Text widget."""
        selection = self.lb.curselection()
        if not selection:
            return

        file_name = self.lb.get(selection[0])
        directory = "Module_Help"
        file_path = os.path.join(directory, file_name)

        try:
            with open(file_path, "r") as file:
                content = file.read()
                self.textwidget.delete(1.0, tk.END)
                self.textwidget.insert(tk.END, content)
        except Exception as e:
            self.textwidget.delete(1.0, tk.END)
            self.textwidget.insert(tk.END, f"Error reading file: {e}")

    def clear(self):
        """Clear the text widget."""
        self.textwidget.delete(1.0, tk.END)

    def save_file(self):
        """Save the content of the text widget to a file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Scripts", "*.py"),
                ("All Files", "*.*")
            ],
        )
        if filepath:
            with open(filepath, "w") as output_file:
                text = self.textwidget.get(1.0, tk.END)
                output_file.write(text)


    def load_files_from_directory(self):
        """Load all text files from the Module_Help directory into the Listbox."""
        directory = "Module_Help"
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the directory if it doesn't exist

        # Clear the Listbox
        self.lb.delete(0, tk.END)

        # Add text files to the Listbox
        for file in os.listdir(directory):
            if file.endswith(".txt"):  # Only list .txt files
                self.lb.insert(tk.END, file)

    def display_selected_file(self, event):
        """Display the contents of the selected file in the Text widget."""
        selection = self.lb.curselection()
        if not selection:
            return

        file_name = self.lb.get(selection[0])
        directory = "Module_Help"
        file_path = os.path.join(directory, file_name)

        try:
            with open(file_path, "r") as file:
                content = file.read()
                self.textwidget.delete(1.0, tk.END)
                self.textwidget.insert(tk.END, content)
        except Exception as e:
            self.textwidget.delete(1.0, tk.END)
            self.textwidget.insert(tk.END, f"Error reading file: {e}")

    def clear(self):
        """Clear the text widget."""
        self.textwidget.delete(1.0, tk.END)

    def save_file(self):
        """Save the content of the text widget to a file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Scripts", "*.py"),
                ("All Files", "*.*")
            ],
        )
        if filepath:
            with open(filepath, "w") as output_file:
                text = self.textwidget.get(1.0, tk.END)
                output_file.write(text)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Documentation Viewer")
    app = PyDDViewer(root)
    root.mainloop()
