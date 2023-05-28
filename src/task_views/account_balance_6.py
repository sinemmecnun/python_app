import tkinter as tk
from tkinter.ttk import Combobox

from src.file_data.file_data import accounts_list, clients_list, calculate_balance, fill_operation_dict, \
    fill_clients_dict


class AccountBalance:
    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title('Справка по сметка')
        #setting window size
        width=700
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(align_str)
        self.root.resizable(width=False, height=False)

        clients_dict = fill_clients_dict()
        def egn_selected(event):
            done_label['text'] = ''

            egn_temp = egn_combobox.get()
            iban_combobox['values'] = [x for x in clients_dict[egn_temp]['accounts']]

        def account_selected(event):
            iban_temp = iban_combobox.get()
            balance_sheet = calculate_balance()
            operations_dict = fill_operation_dict()
            if iban_temp not in balance_sheet.keys():
                return

            egn = [x[0] for x in accounts_list if x[1] == iban_temp][0]
            name = clients_dict[egn]['name']

            transactions_string = f'Клиент: {name}\n' \
                                  f'ЕГН: {egn}\n' \
                                  f'IBAN: {iban_temp}\n' \
                                  f'Разполагаемост: {balance_sheet[iban_temp]:.2f} BGN\n\n' \
                                  f'Движения по сметката:\n'

            for transaction in operations_dict[iban_temp]:
                transactions_string += f"{transaction['date']} | " \
                                       f"{transaction['type']} |{float(transaction['sum']):.2f} BGN\n"

            transactions['text'] = transactions_string

        def export_transactions():
            export_text = transactions['text']
            if export_text == '':
                return

            with open("spravka.txt", 'a', encoding='UTF-8') as spravka:
                spravka.write(export_text)
                spravka.write('---------------------------------------------------------------\n')

            done_label['text'] = 'Done!'

        select_message = tk.Label(root, text="Изберете клиент:")
        select_message.pack()

        egn_combobox = Combobox(root)
        egn_combobox['values'] = [x[0] for x in clients_list]
        egn_combobox.current(0)
        egn_combobox.bind('<<ComboboxSelected>>', egn_selected)
        egn_combobox.pack()

        spacer1 = tk.Label(root, text='\n')
        spacer1.pack()

        select_sort = tk.Label(self.root, text="Изберете сметка:")
        select_sort.pack()

        iban_combobox = Combobox(self.root)
        iban_combobox['values'] = ['Изберете ЕГН']
        iban_combobox.current(0)
        iban_combobox.bind('<<ComboboxSelected>>', account_selected)
        iban_combobox.pack()

        spacer2 = tk.Label(self.root, text='\n')
        spacer2.pack()

        transactions = tk.Label(self.root, text='')
        transactions.pack()

        spacer3 = tk.Label(self.root, text='\n')
        spacer3.pack()

        export_button = tk.Button(self.root, text="Export", command=export_transactions)
        export_button.pack()

        done_label = tk.Label(self.root, text='')
        done_label.pack()