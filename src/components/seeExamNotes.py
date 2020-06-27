from tkinter import Button, Label, Listbox, ttk, END
from src.modules.postulation.index import getSubjectsByPostulant
from src.modules.evaluation.index import getEvaluations

class SeeExamNotes():

    def __init__(self, frame, column, id_user):
         self.frame = frame
         self.column = column
         self.id_user = id_user
         self.created()
         self.mounted()

    def created(self):
        self.labelTittle = Label(self.frame, text='Ver notas de postulaciones')
        self.labelTittle.grid(column=self.column, row=0, pady=15)

        self.labelPostulations = Label(self.frame, text='elige la asignatura que quieres ver la nota')
        self.labelPostulations.grid(column=self.column, row=1, pady=5)

        self.comboBoxSubjects = ttk.Combobox(self.frame)
        self.comboBoxSubjects.grid(column=self.column, row=2, pady=5)

        self.buttonSelecSubject = Button(self.frame, text='Select Subject', command= lambda: self.showExams())
        self.buttonSelecSubject.grid(column=self.column, row=3, pady=5)

        self.labelExams = Label(self.frame, text='Exams')
        self.labelExams.grid(column=self.column, row=4, pady=5)

        self.listboxExams = Listbox(self.frame, width=30)
        self.listboxExams.grid(column=self.column, row=5, pady=5)

    def mounted(self):
        self.subjectPostulations = getSubjectsByPostulant(self.id_user)
        listSubjectPostulation = []
        for subject in self.subjectPostulations:
            listSubjectPostulation.append(subject[1])
        self.comboBoxSubjects["values"] = listSubjectPostulation

    def showExams(self):
        self.listboxExams.delete(0, END)
        id_subject = self.subjectPostulations[self.comboBoxSubjects.current()][0]
        evaluations = getEvaluations(id_subject, self.id_user)
        print(evaluations)
        for evaluation in evaluations:
            self.listboxExams.insert(END, evaluation)

