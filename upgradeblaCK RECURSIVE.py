import os
import subprocess


def reformat_code(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                result = subprocess.run(f"python -m black {filepath}", shell=True)
                if result.returncode == 0:
                    print(f"Successfully formatted: {filepath}")
                else:
                    print(f"Error occurred while formatting: {filepath}")


# Usage
reformat_code("/media/jh/Python_Backup/*.py")
