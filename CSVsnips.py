import csv

fieldnames = ["Name", "Age"]
data = [{"Name": "Alice", "Age": "25"}, {"Name": "Bob", "Age": "30"}]

with open("output.csv", mode="w", newline="", encoding="utf-8-sig") as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()  # writes the headers to the CSV
    csv_dict_writer.writerows(data)  # writes the data to the CSV


#######################


import csv

with open("example.csv", mode="r", newline="", encoding="utf-8-sig") as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)  # Each row is a dictionary


######################3


import csv

data = [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]

with open("output.csv", mode="w", newline="", encoding="utf-8-sig") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)  # writing multiple rows
    #############################
    import csv

fieldnames = ["Name", "Age"]
data = [{"Name": "Alice", "Age": "25"}, {"Name": "Bob", "Age": "30"}]

with open("output.csv", mode="w", newline="", encoding="utf-8-sig") as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()  # writes the headers to the CSV
    csv_dict_writer.writerows(data)  # writes the data to the CSV
