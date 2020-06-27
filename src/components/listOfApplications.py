from tkinter import Label, Listbox, END, Button, Entry


class ListOfApplications():
    
    def __init__(self, frame, column):
        self.frame = frame
        self.column = column
        self.created()
        self.mounted()

    def created(self):
        self.labelTittle = Label(self.frame, text='List Of Applications')
        self.labelTittle.grid(column=self.column, row=0, pady=15)

        self.listOfApplications = Listbox(self.frame, width=30)
        self.listOfApplications.grid(column=self.column, row=1)

    def mounted(self):
        pass