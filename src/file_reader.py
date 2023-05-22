import csv


def read_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
        del data_list[0]
        return data_list