import tkinter as tk
import tkinter.font as tkFont
import csv

def read_csv(csv_file):
    # with open(csv_file, "r", encoding="utf-8") as file:
    #     csvreader = csv.reader(file)
    #     data_list = []
    #     for row in csvreader:
    #         data_list.append(row)
    #     return data_list
    file = open(csv_file, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    return data

class App:
    def __init__(self, root):
        def search_client():
            egn = GLineEdit_327.get()
            for row in range(0, len(clients_list)):
                y = clients_csv[row].split(",") 
                if egn == y[0]:
                    name_label['text'] = y[1]
                    break

        #setting title
        root.title("Kasovi opreracii")
        #setting window size
        width=584
        height=458
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_327=tk.Entry(root)
        GLineEdit_327["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_327["font"] = ft
        GLineEdit_327["fg"] = "#333333"
        GLineEdit_327["justify"] = "center"
        GLineEdit_327["text"] = ""
        GLineEdit_327.place(x=40,y=60,width=161,height=32)

        GLabel_13=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_13["font"] = ft
        GLabel_13["fg"] = "#333333"
        GLabel_13["justify"] = "center"
        GLabel_13["text"] = "EGN"
        GLabel_13.place(x=20,y=30,width=70,height=25)

        GButton_917=tk.Button(root)
        GButton_917["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_917["font"] = ft
        GButton_917["fg"] = "#000000"
        GButton_917["justify"] = "center"
        GButton_917["text"] = "Search"
        GButton_917.place(x=250,y=70,width=70,height=25)
        GButton_917["command"] = search_client

        GListBox_92=tk.Listbox(root)
        GListBox_92["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_92["font"] = ft
        GListBox_92["fg"] = "#333333"
        GListBox_92["justify"] = "center"
        GListBox_92.place(x=40,y=140,width=275,height=137)

        GLabel_868=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_868["font"] = ft
        GLabel_868["fg"] = "#333333"
        GLabel_868["justify"] = "center"
        GLabel_868["text"] = "IBAN"
        GLabel_868.place(x=20,y=110,width=70,height=25)

        GButton_939=tk.Button(root)
        GButton_939["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_939["font"] = ft
        GButton_939["fg"] = "#000000"
        GButton_939["justify"] = "center"
        GButton_939["text"] = "Debit"
        GButton_939.place(x=40,y=310,width=70,height=25)
        GButton_939["command"] = self.GButton_939_command

        GButton_171=tk.Button(root)
        GButton_171["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_171["font"] = ft
        GButton_171["fg"] = "#000000"
        GButton_171["justify"] = "center"
        GButton_171["text"] = "Withdraw"
        GButton_171.place(x=230,y=310,width=70,height=25)
        GButton_171["command"] = self.GButton_171_command

        name_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        name_label["font"] = ft
        name_label["fg"] = "#333333"
        name_label["justify"] = "center"
        name_label["text"] = "Name"
        name_label.place(x=340,y=60,width=216,height=31)

        GLabel_281=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_281["font"] = ft
        GLabel_281["fg"] = "#333333"
        GLabel_281["justify"] = "center"
        GLabel_281["text"] = "Total"
        GLabel_281.place(x=30,y=380,width=70,height=25)

        GButton_977=tk.Button(root)
        GButton_977["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_977["font"] = ft
        GButton_977["fg"] = "#000000"
        GButton_977["justify"] = "center"
        GButton_977["text"] = "Confirm"
        GButton_977.place(x=230,y=380,width=70,height=25)
        GButton_977["command"] = self.GButton_977_command

        GButton_561=tk.Button(root)
        GButton_561["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_561["font"] = ft
        GButton_561["fg"] = "#000000"
        GButton_561["justify"] = "center"
        GButton_561["text"] = "spravka za dvijenie"
        GButton_561.place(x=400,y=130,width=133,height=37)
        GButton_561["command"] = self.GButton_561_command

    def GButton_917_command(self):
        print("command")


    def GButton_939_command(self):
        print("command")


    def GButton_171_command(self):
        print("command")


    def GButton_977_command(self):
        print("command")


    def GButton_561_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

clients_csv = "clients.csv"
acc_csv = "accounts.csv"
types_csv = "operation_types.csv"
operations_csv = "operations.csv"

clients_list = read_csv(clients_csv)
acc_list = read_csv(acc_csv)
types_list = read_csv(types_csv)
operations_list = read_csv(operations_csv)