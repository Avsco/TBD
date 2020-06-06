from tkinter import Tk, Frame, Label, Listbox, END
from src.modules.ui.index import getUIByID_user, showUi

def printMainFrame(canvas, user):
    canvas.config(height=600, width=800)

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    labelListUI = Label(frame, text="Lista de interfaces")
    labelListUI.grid(row=0, column=0, pady=10)

    listboxUI = Listbox(frame, width=40, height=5)
    listboxUI.grid(row=1, column=0, pady=10)

    for ui in getUIByID_user(user.id):
        user.addUI(ui[0])
    
    for ui in user.UIs:
        listboxUI.insert(END, (ui, showUi(ui)))