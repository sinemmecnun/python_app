import tkinter as tk
import tkinter.font as tk_font

from src.task_views.account_balance_6 import AccountBalance
from src.task_views.accounts_screen_2 import AccountsScreen
from src.task_views.add_operation_7 import AddOperation
from src.task_views.client_exposition_3 import ClientExposition
from src.task_views.clients_screen_1 import ClientsScreen
from src.task_views.filter_and_sort_5 import SortBySum
from src.task_views.search_by_date_4 import SearchByDate


class MainScreen:
    def __init__(self, root):
        # setting title
        root.title("Касови операции")
        # setting window size
        width = 510
        height = 370

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(align_str)
        root.resizable(width=False, height=False)

        buttons = []
        for idx in range(7):
            button = tk.Button(root)
            button["bg"] = "#f0f0f0"
            ft = tk_font.Font(family='Times', size=10)
            button["font"] = ft
            button["fg"] = "#000000"
            button["justify"] = "center"
            button["text"] = f"{idx + 1} задача"

            buttons.append(button)

        buttons[0].place(x=40, y=40, width=120, height=60)
        buttons[0]["command"] = self.task_1_command

        buttons[1].place(x=200, y=40, width=120, height=60)
        buttons[1]["command"] = self.task_2_command

        buttons[2].place(x=350, y=40, width=120, height=60)
        buttons[2]["command"] = self.task_3_command

        buttons[3].place(x=40, y=140, width=120, height=60)
        buttons[3]["command"] = self.task_4_command

        buttons[4].place(x=200, y=140, width=120, height=60)
        buttons[4]["command"] = self.task_5_command

        buttons[5].place(x=350, y=140, width=120, height=60)
        buttons[5]["command"] = self.task_6_command

        buttons[6].place(x=200, y=240, width=120, height=60)
        buttons[6]["command"] = self.task_7_command

    def task_1_command(self):
        root = tk.Tk()
        ClientsScreen(root)
        root.mainloop()


    def task_2_command(self):
        root = tk.Tk()
        AccountsScreen(root)
        root.mainloop()


    def task_3_command(self):
        root = tk.Tk()
        ClientExposition(root)
        root.mainloop()


    def task_4_command(self):
        root = tk.Tk()
        SearchByDate(root)
        root.mainloop()

    def task_5_command(self):
        root = tk.Tk()
        SortBySum(root)
        root.mainloop()

    def task_6_command(self):
        root = tk.Tk()
        AccountBalance(root)
        root.mainloop()

    def task_7_command(self):
        root = tk.Tk()
        AddOperation(root)
        root.mainloop()