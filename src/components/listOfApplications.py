from tkinter import Label, Listbox, END, Button, Entry
from src.modules.postulation.index import getPostulation
from src.modules.subject.index import getSubjectsById

class ListOfApplications():
    
    def __init__(self, frame, column, user_id):
        self.user_id = user_id
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
        for postulation in getPostulation(self.user_id):
            nameSubject = getSubjectsById(postulation[0])
            self.listOfApplications.insert(END, (nameSubject, postulation[2]))
        