import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox

from src.file_data import operations_list, types_dict
from src.file_data import clients_list
from src.file_data import accounts_list

class SortBySum:
    def __init__(self, root):
        #setting title
        root.title('filter by type and sort by sum')
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
        table["columns"] = ('acc', 'full_name', 'egn', 'operation', 'amount')

        table.heading("#0", text="Index")
        table.column("#0", width=20)

        table.heading("acc", text="Акаунт")
        table.column("acc", width=100)

        table.heading("full_name",text="Име")
        table.column("full_name", width=70)

        table.heading("egn",text="Егн")
        table.column("egn", width=50)

        table.heading("operation",text="Oперация")
        table.column("operation", width=50)

        table.heading("amount",text="Сума")
        table.column("amount", width=50)

        def filter_by_type(event):
            print(operation_type_combobox.get())

        def select_sort_command(event):
            print(sort_type_combobox.get())

        spacer1 = tk.Label(root, text='\n')
        spacer1.pack()

        options = ['Всички']
        for operation_id, operation_type in types_dict.items():
            options.append(operation_type)

        select_message = tk.Label(root, text="Изберете операция:")
        select_message.pack()

        operation_type_combobox = Combobox(root)
        operation_type_combobox['values'] = options
        operation_type_combobox.current(0)
        operation_type_combobox.bind('<<ComboboxSelected>>', filter_by_type)
        operation_type_combobox.pack()

        select_sort = tk.Label(root, text="Изберете тип сортиране:")
        select_sort.pack()

        sort_type_combobox = Combobox(root)
        sort_type_combobox['values'] = ('asc', 'desc')
        sort_type_combobox.current(0)
        sort_type_combobox.bind('<<ComboboxSelected>>', select_sort_command)
        sort_type_combobox.pack()

