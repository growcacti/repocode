import os
import importlib
import contextlib
import io

def generate_help_from_requirements(requirements_file, output_directory):
    """
    Generate .txt files containing help documentation for modules listed in a requirements file.

    Args:
        requirements_file (str): Path to the requirements.txt file.
        output_directory (str): Directory to save the .txt files.
    """
    if not os.path.exists(requirements_file):
        print(f"Requirements file '{requirements_file}' not found.")
        return

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read module names from the requirements file
    with open(requirements_file, "r") as file:
        modules = [line.split("==")[0].strip() for line in file if line.strip()]

    for module_name in modules:
        try:
            # Import the module
            module = importlib.import_module(module_name)

            # Capture the help text
            with contextlib.redirect_stdout(io.StringIO()) as f:
                help(module)
            help_text = f.getvalue()

            # Write to a .txt file
            file_path = os.path.join(output_directory, f"{module_name}_help.txt")
            with open(file_path, "w") as output_file:
                output_file.write(help_text)
            print(f"Help file created for: {module_name}")

        except Exception as e:
            print(f"Failed to generate help for {module_name}: {e}")

# Path to requirements.txt
requirements_file = "requirements.txt"

# Directory to store the help files
output_directory = "Module_Help"

# Generate help files
generate_help_from_requirements(requirements_file, output_directory)
