from tkinter import Tk, Frame
from src.modules.ui.index import getUIByID_user

from src.components.registryOfAuxiliary import RegistryOfAuxiliary
from src.components.listOfApplications import ListOfApplications
from src.components.registryOfExams import RegistryOfExams
from src.components.seeExamNotes import SeeExamNotes
from src.components.seeListOfStudents import SeeListOfStudents
from src.components.takeAttendeeList import TakeAttendeeList

def printMainFrame(canvas, user):
    canvas.config(height=450, width=650)

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    uis = getUIByID_user(user.id)
    for ui in uis:
        if ui[0] == 'RegistryOfAuxiliary': 
            RegistryOfAuxiliary(frame, 0)
        elif ui[0] == 'RegistryOfExams': 
            RegistryOfExams(frame, 1)
        elif ui[0] == 'ListOfApplications': 
            ListOfApplications(frame, 0, user.id)
        elif ui[0] == 'SeeExamNotes': 
            SeeExamNotes(frame, 1, user.id)
        elif ui[0] == 'SeeListOfStudents': 
            SeeListOfStudents(frame, 0, user.id)
        elif ui[0] == 'TakeAttendeeList': 
            TakeAttendeeList(frame, 1, user.id)
        
        



    # RegistryOfAuxiliary(frame, 0)
    # RegistryOfExams(frame, 1)

    # ListOfApplications(frame, 0, user.id)
    # SeeExamNotes(frame, 1, user.id)

    # SeeListOfStudents(frame, 0, user.id)
    # TakeAttendeeList(frame, 1, user.id)