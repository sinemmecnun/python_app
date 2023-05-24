import tkinter as tk
import tkinter.font as tk_font
from tkinter import ttk

from src.file_data import accounts_list


class AccountsScreen:
    def __init__(self, root):
        #setting title
        root.title("accounts screen")
        #setting window size
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)


        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)
        table["columns"] = ('egn', 'iban')
        table.heading("#0", text="Index")
        table.column("#0", width=50)
        table.heading('egn', text='ЕГН')
        table.heading('iban', text='IBAN')


        # Добавяне на информация в таблицата
        for i, row in enumerate(accounts_list):
            table.insert("", "end", text=str(i+1), values=row)
