import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox

from src.file_data import clients_list, clients_dict


class ClientExposition:
    def __init__(self, root):
        #setting title
        root.title("client exposition")
        #setting window size
        width=500
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        def get_accounts(event):
            exposition['text'] = ''
            exposition.pack()

            egn = egn_combobox.get()
            result = [x for x in clients_dict[egn]['accounts']]
            exposition['text'] = '\n'.join(result)

        options = [x for x in clients_dict.keys()]

        egn_combobox = Combobox(root)
        egn_combobox['values'] = options
        egn_combobox.current(0)
        egn_combobox.bind('<<ComboboxSelected>>', get_accounts)
        egn_combobox.pack()

        spacer1 = tk.Label(root, text='')
        spacer1.pack()

        exposition = tk.Label(root, text="")
        exposition.pack()