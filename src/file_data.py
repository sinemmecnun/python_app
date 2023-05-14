import csv

with open("../data/operation_types.csv", "r", encoding='UTF-8') as operation_types:
    reader = csv.reader(operation_types)
    operation_types_data = {}

    for row in reader:
        operation_id, operation_type = row
        if not operation_id.isnumeric():
            continue

        operation_types_data[operation_id] = operation_type


with open("../data/clients.csv", "r", encoding='UTF-8') as clients:
    reader = csv.reader(clients)
    clients_data = {}

    for row in reader:
        egn, names = row
        if not egn.isnumeric():
           continue
        clients_data[egn] = names


with open("../data/accounts.csv", 'r') as accounts:
    pass

with open("../data/operations.csv", 'r') as operations:
    pass
