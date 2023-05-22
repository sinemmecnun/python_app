import tkinter as tk
import tkinter.font as tk_font

from src.file_data import accounts_list


class AccountsScreen:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        accounts_listbox=tk.Listbox(root)
        accounts_listbox["borderwidth"] = "1px"
        ft = tk_font.Font(family='Times', size=10)
        accounts_listbox["font"] = ft
        accounts_listbox["fg"] = "#333333"
        accounts_listbox["justify"] = "center"
        accounts_listbox.place(x=40,y=60,width=415,height=286)

        accounts_label=tk.Label(root)
        ft = tk_font.Font(family='Times', size=12)
        accounts_label["font"] = ft
        accounts_label["fg"] = "#333333"
        accounts_label["justify"] = "center"
        accounts_label["text"] = "Сметки"
        accounts_label.place(x=30,y=20,width=150,height=33)

        for idx in range(len(accounts_list)):
            _, iban = accounts_list[idx]
            accounts_listbox.insert(idx + 1, iban)