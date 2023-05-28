import tkinter as tk
from tkinter import ttk

from src.file_data.file_data import clients_list


class ClientsScreen:
    def __init__(self, root):
        #setting title
        root.title("Клиенти")
        #setting window size
        width=500
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)
        table["columns"] = ('egn', 'name')
        table.heading("#0", text="Номер")
        table.column("#0", width=50)
        table.heading('egn', text='ЕГН')
        table.heading('name', text='Име')

        # Добавяне на информация в таблицата
        for i, row in enumerate(clients_list):
            table.insert("", "end", text=str(i+1), values=row)
