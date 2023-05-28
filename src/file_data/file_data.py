import csv

# sets the paths to the data
clients_csv = "./data/clients.csv"
acc_csv = "./data/accounts.csv"
types_csv = "./data/operation_types.csv"
operations_csv = "./data/operations.csv"

def read_csv(csv_file):
    # reads data from files
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
        del data_list[0]
        return data_list


# gets lists from each file
clients_list = read_csv(clients_csv)
# egn, name

accounts_list = read_csv(acc_csv)
# egn, iban

types_list = read_csv(types_csv)
# id, type

operations_list = read_csv(operations_csv)
# iban, type, sum, date

def fill_types_dict(types_list_temp):
    temp_dict = {}
    # {id: tip}
    for type in types_list_temp:
        id, operation_type = type
        if id not in temp_dict:
            temp_dict[id] = ''
        temp_dict[id] = operation_type

    return temp_dict

def fill_clients_dict():
    clients_dict = {}
    # {egn: {name: "", accounts: [..., ...]}}
    for client in clients_list:
        egn, name = client
        if egn not in clients_dict.keys():
            clients_dict[egn] = {}
            clients_dict[egn]['accounts'] = []
        clients_dict[egn]['name'] = name

    for account in accounts_list:
        egn, iban = account
        clients_dict[egn]['accounts'].append(iban)

    return clients_dict


def fill_operation_dict():
    operations_dict = {}
    # {iban: [{type: "", sum: ..., date: ""}, {}]}
    for operation in operations_list:
        if not operation:
            continue
        iban, type, sum, date = operation
        if iban not in operations_dict:
            operations_dict[iban] = []

        temp_dict = {
            'type': types_dict[type],
            'sum': sum,
            'date': date}

        operations_dict[iban].append(temp_dict)

    return operations_dict


types_dict = fill_types_dict(types_list)

def calculate_balance():
    operations_dict = fill_operation_dict()
    balance_sheet = {}
    # {iban: balance}
    for iban, operations in operations_dict.items():
        current_balance = 0
        for operation in operations:
            type = operation['type']

            sum = float(operation['sum'])
            multiplier = 1 if type == "Вноска" else -1

            current_balance += sum * multiplier
        balance_sheet[iban] = current_balance

    return balance_sheet

def operations_full_list_func():
    operations_full_list = []
    for operation in operations_list:
        if not operation:
            continue
        iban, type, sum, date = operation
        operation_type_string = types_dict[type]

        egn = [x[0] for x in accounts_list if x[1] == iban][0]
        client_name = [x[1] for x in clients_list if x[0] == egn][0]

        temp_operation_list = [iban, egn, client_name, operation_type_string, sum, date]
        operations_full_list.append(temp_operation_list)

    return operations_full_list

clients_dict = fill_clients_dict()
