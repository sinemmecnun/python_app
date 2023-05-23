import tkinter as tk
from tkcalendar import DateEntry
import tkinter.font as tk_font
from tkinter import ttk
from tkcalendar import Calendar

from src.file_data import operations_list
from src.file_data import clients_list
from src.file_data import accounts_list

class SearchByDate:
    def __init__(self, root):
        #setting title
        root.title("by date")
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
        table["columns"] = ('acc', 'full_name', 'egn', 'code_operation', 'amount')

        table.heading("#0", text="Index")
        table.column("#0", width=50)

        table.heading("acc",text="Акаунт")
        table.column("acc", width=50)

        table.heading("full_name",text="Име")
        table.column("full_name", width=50)

        table.heading("egn",text="Егн")
        table.column("egn", width=50)

        table.heading("code_operation",text="Код операция")
        table.column("code_operation", width=50)

        table.heading("amount",text="Сума")
        table.column("amount", width=50)
    
        def updateLabel(event):
            label.config(text="Selected Date: " + calendar.get_date())

        #in cmd -> pip install tkcalendar
        calendar = Calendar(root, date_pattern='DD/mm/yyyy')
        calendar.pack()
        calendar.bind('<<CalendarSelected>>', updateLabel)
        
        label = tk.Label(root, text="Selected Date: ")
        label.pack()


        #таблицата

        curr_dict = {}
        for operation in operations_list[1:]:
            if operation[4] == calendar.get_date():
                operation_account = operation[1]
                operation_code = operation[2]
                operation_amount = float(operation[3])

                for account in accounts_list[1:]:
                    if account[1] == operation_account:
                        acc_egn = account[0]
                
                for client in clients_list[1:]:
                    if client[0] == acc_egn:
                        client_name = client[1]

                if operation_account not in curr_dict:
                    curr_dict[operation_account] = {
                        'Име': client_name,
                        'Егн': acc_egn,
                        'Код операция': operation_code,
                        'Сума': operation_amount
                    }

        for operation_account in curr_dict:
            table.insert('', 'end', text="1", values=(curr_dict['Акаунт'], curr_dict['Име'],
                                                      curr_dict['Егн'], curr_dict['Код операция'],
                                                      curr_dict['Сума']))

        # for x in curr_dict:
        #     table.insert('', 'end', text="1",
        #                  values=(championList['Weight Class'], championList['Name']))

