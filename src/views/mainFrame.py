from tkinter import Tk, Frame, Canvas
from src.modules.ui.index import getUIByID_user

from src.components.registryOfAuxiliary import RegistryOfAuxiliary
from src.components.listOfApplications import ListOfApplications
from src.components.registryOfExams import RegistryOfExams
from src.components.seeExamNotes import SeeExamNotes
from src.components.seeListOfStudents import SeeListOfStudents
from src.components.takeAttendeeList import TakeAttendeeList

def printMainFrame(canvas, user):

    canvas.config(height=500, width=690)

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


    frame1 = Frame(frame)
    frame1.config(bd=1, relief="solid")
    frame1.grid(column=0, row=0, padx= 20, ipadx=10, ipady=10)
    frame1.tkraise()

    frame2 = Frame(frame)
    frame2.config(bd=1, relief="solid")
    frame2.grid(column=1, row=0, padx=20, ipadx=10, ipady=10)
    frame2.tkraise()


    uis = getUIByID_user(user.id)
    for ui in uis:
        if ui[0] == 'RegistryOfAuxiliary': 
            RegistryOfAuxiliary(frame1, 0)
        elif ui[0] == 'RegistryOfExams': 
            RegistryOfExams(frame2, 0)
        elif ui[0] == 'ListOfApplications': 
            ListOfApplications(frame1, 0, user.id)
        elif ui[0] == 'SeeExamNotes': 
            SeeExamNotes(frame2, 1, user.id)
        elif ui[0] == 'SeeListOfStudents': 
            SeeListOfStudents(frame1, 0, user.id)
        elif ui[0] == 'TakeAttendeeList': 
            TakeAttendeeList(frame2, 1, user.id)
        
        



    # RegistryOfAuxiliary(frame, 0)
    # RegistryOfExams(frame, 1)

    # ListOfApplications(frame, 0, user.id)
    # SeeExamNotes(frame, 1, user.id)

    # SeeListOfStudents(frame, 0, user.id)
    # TakeAttendeeList(frame, 1, user.id)