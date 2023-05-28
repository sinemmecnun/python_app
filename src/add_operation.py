import csv
import tkinter as tk
from datetime import date
from tkinter import END
from tkinter.ttk import Combobox

from src.file_data import clients_list, clients_dict, types_list, operations_list


class AddOperation:
    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title('Добави вносна бележка/нареждане разписка')
        #setting window size
        width=700
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(align_str)
        self.root.resizable(width=False, height=False)

        def egn_selected(event):
            egn_temp = egn_combobox.get()
            iban_combobox['values'] = [x for x in clients_dict[egn_temp]['accounts']]

        def add_operation():
            iban_temp = iban_combobox.get()
            operation_type = operation_type_combobox.get()
            operation_type_string = [x[0] for x in types_list if x[1] == operation_type][0]
            operation_sum = sum_textbox.get('1.0', END)
            operation_sum.strip('\n')
            try:
                operation_sum = f"{float(operation_sum):.2f}"
            except ValueError:
                operation_text['text'] = 'Невалидна сума'


            today = date.today()
            current_date = today.strftime("%d.%m.%Y")

            new_operation = [iban_temp, operation_type_string, operation_sum, current_date]
            operations_list.append(new_operation)

            with open('./data/operations.csv', 'a', encoding='UTF-8') as operations_csv:
                writer = csv.writer(operations_csv, delimiter=',')
                writer.writerow(new_operation)
            operation_text['text'] = "\n"+ " | ".join(new_operation)


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
        iban_combobox.pack()

        spacer2 = tk.Label(self.root, text='\n')
        spacer2.pack()

        select_operation = tk.Label(self.root, text="Изберете тип операция:")
        select_operation.pack()

        operation_type_combobox = Combobox(self.root)
        operation_type_combobox['values'] = [x[1] for x in types_list]
        operation_type_combobox.current(0)
        operation_type_combobox.pack()

        spacer3 = tk.Label(self.root, text='\n')
        spacer3.pack()

        write_sum = tk.Label(self.root, text="Въведете сума:")
        write_sum.pack()

        sum_textbox = tk.Text(root, height=1, width=20)
        sum_textbox.pack()

        spacer4 = tk.Label(self.root, text='\n')
        spacer4.pack()

        add_button = tk.Button(self.root, text='Осчетоводи', command=add_operation)
        add_button.pack()

        operation_text = tk.Label(self.root, text="")
        operation_text.pack()