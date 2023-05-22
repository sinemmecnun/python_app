import tkinter as tk
import tkinter.font as tkFont
import csv

def read_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list = []
        for row in csvreader:
            data_list.append(row)
        return data_list

class App:
    def __init__(self, root):
        #setting title
        root.title("касови операции")
        #setting window size
        width=510
        height=256
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_831=tk.Button(root)
        GButton_831["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_831["font"] = ft
        GButton_831["fg"] = "#000000"
        GButton_831["justify"] = "center"
        GButton_831["text"] = "1 задача"
        GButton_831.place(x=40,y=40,width=120,height=60)
        GButton_831["command"] = self.GButton_831_command

        GButton_73=tk.Button(root)
        GButton_73["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#000000"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "2 задача"
        GButton_73.place(x=200,y=40,width=120,height=60)
        GButton_73["command"] = self.GButton_73_command

        GButton_494=tk.Button(root)
        GButton_494["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_494["font"] = ft
        GButton_494["fg"] = "#000000"
        GButton_494["justify"] = "center"
        GButton_494["text"] = "3 задача"
        GButton_494.place(x=350,y=40,width=120,height=60)
        GButton_494["command"] = self.GButton_494_command

        GButton_367=tk.Button(root)
        GButton_367["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_367["font"] = ft
        GButton_367["fg"] = "#000000"
        GButton_367["justify"] = "center"
        GButton_367["text"] = "4 задача"
        GButton_367.place(x=40,y=140,width=120,height=60)
        GButton_367["command"] = self.GButton_367_command

        GButton_237=tk.Button(root)
        GButton_237["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_237["font"] = ft
        GButton_237["fg"] = "#000000"
        GButton_237["justify"] = "center"
        GButton_237["text"] = "5 задача"
        GButton_237.place(x=200,y=140,width=120,height=60)
        GButton_237["command"] = self.GButton_237_command

        GButton_803=tk.Button(root)
        GButton_803["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_803["font"] = ft
        GButton_803["fg"] = "#000000"
        GButton_803["justify"] = "center"
        GButton_803["text"] = "6 задача"
        GButton_803.place(x=350,y=140,width=120,height=60)
        GButton_803["command"] = self.GButton_803_command

    def GButton_831_command(self):
        print("command")


    def GButton_73_command(self):
        print("command")


    def GButton_494_command(self):
        print("command")


    def GButton_367_command(self):
        print("command")


    def GButton_237_command(self):
        print("command")


    def GButton_803_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

clients_csv = "D:/data/clients.csv"
acc_csv = "D:/data/accounts.csv"
types_csv = "D:/data/operation_types.csv"
operations_csv = "D:/data/operations.csv"

clients_list = read_csv(clients_csv)
acc_list = read_csv(acc_csv)
types_list = read_csv(types_csv)
operations_list = read_csv(operations_csv)