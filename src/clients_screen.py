import tkinter as tk
import tkinter.font as tk_font
from tkinter import ttk

from src.file_data import clients_list


class ClientsScreen:
    def __init__(self, root):
        #setting title
        root.title("clients screen")
        #setting window size
        width=500
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        # clients_listbox=tk.Listbox(root)
        # clients_listbox["borderwidth"] = "1px"
        # ft = tk_font.Font(family='Times', size=10)
        # clients_listbox["font"] = ft
        # clients_listbox["fg"] = "#333333"
        # clients_listbox["justify"] = "center"
        # clients_listbox.place(x=40,y=60,width=415,height=286)

        # clients_label=tk.Label(root)
        # ft = tk_font.Font(family='Times', size=12)
        # clients_label["font"] = ft
        # clients_label["fg"] = "#333333"
        # clients_label["justify"] = "center"
        # clients_label["text"] = "Клиенти"
        # clients_label.place(x=30,y=20,width=150,height=33)

        # for idx in range(len(clients_list)):
        #     egn, name = clients_list[idx]
        #     clients_listbox.insert(idx + 1, f"{egn}, {name}")

        table = ttk.Treeview(root)
        table.pack(fill=tk.BOTH, expand=True)
        table["columns"] = clients_list[0]
        table.heading("#0", text="Index")
        table.column("#0", width=50)
        for col in clients_list[0]:
            table.heading(col, text=col)
            table.column(col, width=100)
# Добавяне на информация в таблицата
        for i, row in enumerate(clients_list[1:]):
            table.insert("", "end", text=i+1, values=row)
