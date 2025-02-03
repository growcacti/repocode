import os
import importlib
import contextlib
import io

def generate_module_help(directory, modules):
    """
    Generate .txt files containing help documentation for the specified modules.

    Args:
        directory (str): Directory to save the .txt files.
        modules (list): List of module names to generate help for.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    for module_name in modules:
        try:
            # Import the module
            module = importlib.import_module(module_name)

            # Capture the help text
            with contextlib.redirect_stdout(io.StringIO()) as f:
                help(module)
            help_text = f.getvalue()

            # Write to a .txt file
            file_path = os.path.join(directory, f"{module_name}_help.txt")
            with open(file_path, "w") as file:
                file.write(help_text)
            print(f"Help file created for: {module_name}")

        except Exception as e:
            print(f"Failed to generate help for {module_name}: {e}")


# List of modules to generate help files for
modules_to_document = [
    "os",
    "sys",
    "json",
    "tkinter",
    "math",
    "datetime",
    "random",
]

# Directory to store the help files
output_directory = "Module_Help"

# Generate the help files
generate_module_help(output_directory, modules_to_document)
