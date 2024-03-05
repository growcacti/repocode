import csv
import vobject
from tkinter import Tk, filedialog


def convert_csv_to_vcf():
    # Select CSV input file
    Tk().withdraw()
    csv_file_path = filedialog.askopenfilename(
        title="Select CSV File", filetypes=[("CSV Files", "*.csv")]
    )
    if not csv_file_path:
        return  # User cancelled the file selection

    # Select VCF output file
    vcf_file_path = filedialog.asksaveasfilename(
        title="Save VCF File",
        defaultextension=".vcf",
        filetypes=[("VCF Files", "*.vcf")],
    )
    if not vcf_file_path:
        return  # User cancelled the file selection

    with open(csv_file_path, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        with open(vcf_file_path, "w") as vcf_file:
            for row in reader:
                vcard = vobject.vCard()
                vcard.add("n").value = vobject.vcard.Name(
                    family=row["Last Name"], given=row["First Name"]
                )
                vcard.add("tel").value = row["Phone"]
                vcard.add("email").value = row["Email"]

                # Additional fields can be added based on your CSV columns

                vcf_file.write(vcard.serialize())


# Run the GUI
Tk().withdraw()
convert_csv_to_vcf()
