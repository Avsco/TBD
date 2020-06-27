from tkinter import Label, ttk, Button, Entry, END
from src.modules.evaluation.index import getSubjects, isOnEvaluation

class TakeAttendeeList():

    def __init__(self, frame, column, id_teacher):
         self.frame = frame
         self.column = column
         self.id_teacher = id_teacher
         self.created()
         self.mounted()

    def created(self):
        self.lableTittle = Label(self.frame, text='list Of students')
        self.lableTittle.grid(column=self.column, row=0, pady=15)

        self.labelSubjects = Label(self.frame, text='Select subject')
        self.labelSubjects.grid(column=self.column, row=1, pady=5)

        self.comboboxSubjects = ttk.Combobox(self.frame)
        self.comboboxSubjects.grid(column=self.column, row=2, pady=5)

        self.EntryStudent = Entry(self.frame)
        self.EntryStudent.grid(column=self.column, row=3, pady=5)

        self.buttonIsOn = Button(self.frame, text='Select Subject', command=lambda: self.send())
        self.buttonIsOn.grid(column=self.column, row=4, pady=5)


    def mounted(self):
        self.subjects = getSubjects(self.id_teacher)
        listSubjects = []
        for subject in self.subjects:
            listSubjects.append(subject[1])
        self.comboboxSubjects["values"] = listSubjects

    def send(self):
        id_subject = self.subjects[self.comboboxSubjects.current()][0]
        isOnEvaluation(id_subject, self.EntryStudent.get())
        self.EntryStudent.delete(0, END)