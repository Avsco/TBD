from tkinter import Label, Button, Entry, ttk

from src.modules.teacher.index import getTeachers
from src.modules.subject.index import getSubjects
from src.modules.exam.index import insertExam

class RegistryOfExams():

    def __init__(self, frame, column):
        self.frame = frame
        self.column = column
        self.created()
        self.mounted()

    def created(self):
        self.labelTitle = Label(self.frame, text='Registry Exams')
        self.labelTitle.grid(column=self.column, row=0, pady=15)

        self.labelSubjects = Label(self.frame, text='Select subject')
        self.labelSubjects.grid(column=self.column, row=1, pady=5)

        self.comboBoxSubjects = ttk.Combobox(self.frame)
        self.comboBoxSubjects.grid(column=self.column, row=2, pady=5)

        self.labelTeacher = Label(self.frame, text='Select teacher')
        self.labelTeacher.grid(column=self.column, row=3, pady=5)

        self.comboBoxTeachers = ttk.Combobox(self.frame)
        self.comboBoxTeachers.grid(column=self.column, row=4, pady=5)

        self.buttonInsertExam = Button(self.frame, text='Ingresar imagen', command=lambda: self.get_image())
        self.buttonInsertExam.grid(column=self.column, row=5, pady=5)

        self.buttonSend = Button(self.frame, text='Send', command=lambda: self.send())
        self.buttonSend.grid(column=self.column, row=6, pady=5)


    def mounted(self):
        self.subjects = getSubjects()
        self.teachers = getTeachers()

        listTeachers = []
        listSubjects = []

        for subject in self.subjects:
            listSubjects.append(subject[1])

        for teacher in self.teachers:
            listTeachers.append(teacher[1])

        self.comboBoxSubjects["values"] = listSubjects
        self.comboBoxTeachers["values"] = listTeachers
 

    def get_image(self):
        pass

    def send(self):
        id_subject = self.subjects[self.comboBoxSubjects.current()][0]
        id_teacher = self.teachers[self.comboBoxTeachers.current()][0]
        insertExam(id_subject, id_teacher, None)

