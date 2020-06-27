from tkinter import Label, ttk, Button, Listbox, END
from src.modules.evaluation.index import getStudents, getSubjects

class SeeListOfStudents():

    def __init__(self, frame, column, id_teacher):
         self.frame = frame
         self.column = column
         self.id_teacher = id_teacher
         self.created()
         self.mounted()

    def created(self):
        self.lableTittle = Label(self.frame, text='list Of students in subject')
        self.lableTittle.grid(column=self.column, row=0, pady=15)

        self.labelSubjects = Label(self.frame, text='Select subject')
        self.labelSubjects.grid(column=self.column, row=1, pady=5)

        self.comboboxSubjects = ttk.Combobox(self.frame)
        self.comboboxSubjects.grid(column=self.column, row=2, pady=5)

        self.buttonSelectSubject = Button(self.frame, text='Select Subject', command=lambda: self.send())
        self.buttonSelectSubject.grid(column=self.column, row=3, pady=5)

        self.labelStudents = Label(self.frame, text='Students')
        self.labelStudents.grid(column=self.column, row=4, pady=5)

        self.listboxStudents = Listbox(self.frame, width=30)
        self.listboxStudents.grid(column=self.column, row=5, pady=5)


    def mounted(self):
        self.subjects = getSubjects(self.id_teacher)
        listSubjects = []
        for subject in self.subjects:
            listSubjects.append(subject[1])
        self.comboboxSubjects["values"] = listSubjects

    def send(self):
        id_subject = self.subjects[self.comboboxSubjects.current()][0]
        for student in getStudents(id_subject, self.id_teacher):
            self.listboxStudents.insert(END, student[0])