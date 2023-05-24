import csv

clients_csv = "./data/clients.csv"
acc_csv = "./data/accounts.csv"
types_csv = "./data/operation_types.csv"
operations_csv = "./data/operations.csv"

def read_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
        del data_list[0]
        return data_list


clients_list = read_csv(clients_csv)
# egn, name

accounts_list = read_csv(acc_csv)
# egn, iban

types_list = read_csv(types_csv)
types_dict = {}
# id, type

operations_list = read_csv(operations_csv)
# iban, type, sum, date

# IMPORTANT
clients_dict = {}
operations_dict = {}

for type in types_list:
    id, operation_type = type
    if id not in types_dict:
        types_dict[id] = ''
    types_dict[id] = operation_type

for client in clients_list:
    egn, name = client
    if egn not in clients_dict.keys():
        clients_dict[egn] = {}
        clients_dict[egn]['accounts'] = []
    clients_dict[egn]['name'] = name

for account in accounts_list:
    egn, iban = account
    clients_dict[egn]['accounts'].append(iban)
#
# for operation in operations_list:
#     id, iban, type, sum, date = operation
#     if iban not in operations_dict:
#         operations_dict[iban] = {}
#     operations_dict[iban][id] = {}
#     # operations_dict[iban][id]['type'] = types_dict[type]
#     operations_dict[iban][id]['sum'] = sum
#     operations_dict[iban][id]['date'] = date
