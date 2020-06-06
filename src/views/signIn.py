from tkinter import Frame, Label, Entry, Button
from src.modules.signIn.index import mainSignIn
from src.views.mainFrame import printMainFrame
from src.classes.user import User

def printSignIn(canvas):
    canvas.config(height=210, width=300)

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    labelTitle = Label(frame, text="LOGIN")
    labelTitle.grid(row=0, column=1, pady=10)

    labelUsername = Label(frame, text="Username") 
    labelUsername.grid(row=1, column=0, pady=5)

    entryUsername = Entry(frame)
    entryUsername.grid(row=1, column=1, columnspan=2)

    labelPassword = Label(frame, text="Password") 
    labelPassword.grid(row=2, column=0, pady=5)

    entryPassword = Entry(frame, show="*")
    entryPassword.grid(row=2, column=1, columnspan=2)

    labelMensaje = Label(frame, text="")
    labelMensaje.grid(row=3, column=0, columnspan=2, pady=2)

    buttonsignIn = Button(frame, text="SignIn", command=lambda: signIn(
        entryUsername.get(),
        entryPassword.get(),
        labelMensaje,
        canvas
    ))
    buttonsignIn.grid(row=4, column=1, pady=10)


def signIn(username, password, mensaje, canvas):
    try:
        if username != '' and password != '':
            res = mainSignIn(username, password)
            if res:
                changeMensaje(mensaje, "Logueado exitosamene", "green")
                printMainFrame(canvas, User(res[0], res[1], username))
            else:
                changeMensaje(mensaje, "Ingrese sus datos correctamente", "red")
        else:
            changeMensaje(mensaje, "Rellene todos los campos", "red")
    except Exception as e:
        print(e)
        changeMensaje(mensaje, "Error en la base de datos", "red")

def changeMensaje(mensaje, text, color):
    mensaje['text'] = text
    mensaje['fg'] = color