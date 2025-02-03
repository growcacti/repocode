import os
import importlib
import functools
from tkinter import *
from tkinter import messagebox

class ImportToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Import Tool")
        
        # Input for module name
        Label(root, text="Module Name:").grid(row=0, column=0, sticky=W)
        self.module_entry = Entry(root, width=30)
        self.module_entry.grid(row=0, column=1, padx=5, pady=5)

        # Check existence button and result
        Button(root, text="Check Existence", command=self.check_existence).grid(row=1, column=0, sticky=W, pady=5)
        self.exists_result = Label(root, text="", fg="blue")
        self.exists_result.grid(row=1, column=1, sticky=W)

        # Import module button and result
        Button(root, text="Import Module", command=self.import_module).grid(row=2, column=0, sticky=W, pady=5)
        self.import_result = Label(root, text="", fg="blue")
        self.import_result.grid(row=2, column=1, sticky=W)

        # Address to Path Conversion
        Label(root, text="Convert Module Address to Path:").grid(row=3, column=0, sticky=W)
        self.address_entry = Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        Button(root, text="Convert", command=self.convert_address).grid(row=4, column=0, sticky=W)
        self.convert_result = Label(root, text="", fg="blue")
        self.convert_result.grid(row=4, column=1, sticky=W)

    def normal_import(self, module_name):
        '''Import a module using the provided module name.'''
        try:
            if '.' in module_name:
                package_name, submodule_name = module_name.rsplit('.', 1)
                package = __import__(module_name)
                return functools.reduce(getattr, [package] + module_name.split('.')[1:])
            else:
                return __import__(module_name)
        except ModuleNotFoundError:
            return None

    def check_existence(self):
        '''Check if a module exists and display result in GUI.'''
        module_name = self.module_entry.get()
        if self.exists(module_name):
            self.exists_result.config(text="Module exists.")
        else:
            self.exists_result.config(text="Module does not exist.")

    def import_module(self):
        '''Attempt to import a module and display result in GUI.'''
        module_name = self.module_entry.get()
        imported_module = self.normal_import(module_name)
        if imported_module:
            self.import_result.config(text="Module imported successfully.")
        else:
            self.import_result.config(text="Module not found.")

    def exists(self, module_name, package_name=None):
        '''Return whether a module by the name `module_name` exists.'''
        try:
            if '.' in module_name:
                messagebox.showerror("Error", "Currently only supports top-level modules.")
                return False
            return bool(importlib.util.find_spec(module_name, package_name))
        except ModuleNotFoundError:
            return False

    def convert_address(self):
        '''Convert a module address to a path-separated address and display result in GUI.'''
        module_address = self.address_entry.get()
        if module_address:
            path = self._module_address_to_partial_path(module_address)
            self.convert_result.config(text=path)
        else:
            messagebox.showerror("Error", "Please enter a module address.")

    def _module_address_to_partial_path(self, module_address):
        '''Convert a dot-separated address to a path-separated address.'''
        return os.path.sep.join(module_address.split('.'))

# Main Program
root = Tk()
app = ImportToolGUI(root)
root.mainloop()
