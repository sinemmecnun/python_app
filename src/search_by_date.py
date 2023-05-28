import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

from src.file_data import operations_list, types_dict
from src.file_data import clients_list
from src.file_data import accounts_list

class SearchByDate:
    def __init__(self, root):
        #setting title
        root.title("Дневен операционен дневник")
        #setting window size
        width=1000
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)
        table["columns"] = ('acc', 'egn','full_name', 'operation', 'amount')

        table.heading("#0", text="Номер")
        table.column("#0", width=20)

        table.heading("acc", text="Акаунт")
        table.column("acc", width=100)

        table.heading("full_name",text="Име")
        table.column("full_name", width=70)

        table.heading("egn",text="ЕГН")
        table.column("egn", width=50)

        table.heading("operation",text="Oперация")
        table.column("operation", width=50)

        table.heading("amount",text="Сума")
        table.column("amount", width=50)

        def update_label(event):
            selected_date = calendar.get_date()
            label.config(text="Selected Date: " + selected_date)
            table.delete(*table.get_children())

            filtered_list = []
            for operation in operations_list:
                egn = None
                client_name = None
                iban, type, sum, date = operation
                operation_type_string = types_dict[type]

                if date != selected_date:
                    continue

                for account_temp in accounts_list:
                    egn_temp, account = account_temp
                    if account == iban:
                        egn = egn_temp
                        break

                for client in clients_list:
                    egn_temp, name = client

                    if egn_temp == egn:
                        client_name = name
                        break

                filtered_list.append([iban, egn, client_name, operation_type_string, sum])
            for idx, row in enumerate(filtered_list):
                table.insert("", "end",text = str(idx + 1), values=row)


        #in cmd -> pip install tkcalendar
        calendar = Calendar(root, date_pattern='DD.mm.yyyy')
        calendar.pack()
        calendar.bind('<<CalendarSelected>>', update_label)

        label = tk.Label(root, text="Selected Date: ")
        label.pack()





