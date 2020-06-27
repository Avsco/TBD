from tkinter import Label, Listbox, END, SINGLE, ACTIVE, Button, Entry
from src.modules.subject.index import getSubjects
from src.modules.postulation.index import insertPostulation

class RegistryOfAuxiliary():
    def __init__(self, frame, column):
        self.column = column
        self.frame = frame
        self.created()
        self.mounted()

    def created(self):

        self.labelTitle = Label(self.frame, text='Registration of applicants to auxiliary')
        self.labelTitle.grid(row=0, column=self.column, pady=10)

        self.listSubjects = Listbox(self.frame, cursor='mouse', width= 30, height=10, selectmode=SINGLE, selectbackground='#BBA988')
        self.listSubjects.grid(row=1, column=self.column, pady=5)

        self.labelEstudent = Label(self.frame, text="id estudent")
        self.labelEstudent.grid(row=2, column=self.column, pady=5)

        self.entryEstudent = Entry(self.frame)
        self.entryEstudent.grid(row=3, column=self.column, pady=5)

        self.buttonSend = Button(self.frame, text='SEND', command=lambda: self.send())
        self.buttonSend.grid(row=4, column=self.column, pady=5)

        self.labelMenssage = Label(self.frame, text='')
        self.labelMenssage.grid(row=5, column=self.column, pady=3)

    def mounted(self):
        self.showSubjects()

    def showSubjects(self):
        for subject in getSubjects():
            self.listSubjects.insert(END, subject)

    def send(self):
        codSubject = self.listSubjects.get(ACTIVE)[0]
        codStudent = self.entryEstudent.get()
        try:
            msg = insertPostulation(codSubject, codStudent)
            self.changeMenssaje(self.labelMenssage, msg, 'green')
        except Exception as e:
            print(e)

    def changeMenssaje(self, menssaje, text, color):
        menssaje['text'] = text
        menssaje['fg'] = color
