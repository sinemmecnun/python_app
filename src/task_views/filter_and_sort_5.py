import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox

from src.file_data.file_data import types_dict, operations_full_list_func


class SortBySum:
    def __init__(self, root):
        #setting title
        root.title('Операционен дневник')
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
        table["columns"] = ('acc', 'egn', 'full_name', 'operation', 'amount', 'date')

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

        table.heading('date', text="Дата")
        table.column('date', width=50)

        def search_operations():
            # clears the table
            table.delete(*table.get_children())
            operations_full_list = operations_full_list_func()
            filter_value = operation_type_combobox.get()
            sort_value = sort_type_combobox.get()

            filter_options = {
                "Всички": operations_full_list,
                "Теглене": [x for x in operations_full_list if x[3] == "Теглене"],
                "Вноска": [x for x in operations_full_list if x[3] == "Вноска"]
            }

            filtered_list = filter_options[filter_value]

            if sort_value == 'asc':
                sorted_list = sorted(filtered_list, key=lambda x: x[4])
            else:
                sorted_list = sorted(filtered_list, key=lambda x: -x[4])


            for idx, row in enumerate(sorted_list):
                table.insert("", "end",text = str(idx + 1), values=row)


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
        operation_type_combobox.pack()

        select_sort = tk.Label(root, text="Изберете тип сортиране на сума:")
        select_sort.pack()

        sort_type_combobox = Combobox(root)
        sort_type_combobox['values'] = ('asc', 'desc')
        sort_type_combobox.current(0)
        sort_type_combobox.pack()

        spacer2 = tk.Label(root, text='\n')
        spacer2.pack()

        export_button = tk.Button(root, text="Search", command=search_operations)
        export_button.pack()

        spacer_3 = tk.Label(root, text='')
        spacer_3.pack()