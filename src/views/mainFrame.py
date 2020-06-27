from tkinter import Tk, Frame
from src.modules.ui.index import getUIByID_user, showUi

from src.components.registryOfAuxiliary import RegistryOfAuxiliary
from src.components.listOfApplications import ListOfApplications
mainUser = None

def printMainFrame(canvas, user):
    canvas.config(height=450, width=325)

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # RegistryOfAuxiliary(frame, 0)
    ListOfApplications(frame, 0)