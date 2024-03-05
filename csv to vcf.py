import csv
import vobject


def convert_csv_to_vcf(csv_file_path, vcf_file_path):
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


# Usage example
convert_csv_to_vcf("contacts.csv", "contacts.vcf")
