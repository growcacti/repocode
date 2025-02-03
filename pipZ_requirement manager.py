import os
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class RequirementsManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Requirements Manager")
        self.root.geometry("600x300")

        # Widgets for Directory Selection
        ttk.Label(root, text="Target Directory:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.dir_entry = ttk.Entry(root, width=50)
        self.dir_entry.grid(row=0, column=1, padx=10, pady=10)
        self.browse_button = ttk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Buttons for Actions
        self.generate_button = ttk.Button(root, text="Generate Requirements and Packages", command=self.generate_requirements)
        self.generate_button.grid(row=1, column=1, pady=10)

        self.install_button = ttk.Button(root, text="Install Packages from Directory", command=self.install_packages)
        self.install_button.grid(row=2, column=1, pady=10)

        # Information Label
        self.info_label = ttk.Label(root, text="This program helps you bundle and install Python dependencies.")
        self.info_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)

    def generate_requirements(self):
        target_dir = self.dir_entry.get()
        if not target_dir:
            messagebox.showerror("Error", "Please select a directory to save the requirements.")
            return

        requirements_path = os.path.join(target_dir, "requirements.txt")
        packages_dir = os.path.join(target_dir, "packages")

        try:
            # Create requirements.txt using pip freeze
            result = subprocess.run(["pip", "freeze"], capture_output=True, text=True, check=True)
            os.makedirs(target_dir, exist_ok=True)
            with open(requirements_path, "w") as f:
                f.write(result.stdout)

            # Download all packages into the packages directory
            os.makedirs(packages_dir, exist_ok=True)
            subprocess.run(["pip", "download", "-r", requirements_path, "-d", packages_dir], check=True)

            messagebox.showinfo("Success", f"Requirements and packages saved to {target_dir}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate requirements and packages.\n{e}")

    def install_packages(self):
        target_dir = self.dir_entry.get()
        if not target_dir:
            messagebox.showerror("Error", "Please select a directory containing the requirements.")
            return

        requirements_path = os.path.join(target_dir, "requirements.txt")
        packages_dir = os.path.join(target_dir, "packages")

        if not os.path.exists(requirements_path):
            messagebox.showerror("Error", "requirements.txt not found in the selected directory.")
            return

        if not os.path.exists(packages_dir):
            messagebox.showerror("Error", "Packages directory not found in the selected directory.")
            return

        try:
            # Install packages using the locally downloaded files
            subprocess.run(["pip", "install", "--no-index", "--find-links", packages_dir, "-r", requirements_path], check=True)
            messagebox.showinfo("Success", "Packages installed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install packages.\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RequirementsManagerApp(root)
    root.mainloop()
