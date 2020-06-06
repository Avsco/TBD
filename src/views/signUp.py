from tkinter import Canvas, Frame, Label, Entry, Button, S
from src.modules.signUp.index import mainSignUp

def printSignUp(root):
    canvas = Canvas(root, height=260, width=320)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    labelTitle = Label(frame, text="SIGN UP")
    labelTitle.grid(row=0, column=1)

    labelSubtitle = Label(frame, text="Ingrese sus datos")
    labelSubtitle.grid(row=1, column=0, columnspan=2, sticky='S', pady=5)

    labelName = Label(frame, text="Name")
    labelName.grid(row=2, column=0, pady=5, sticky='S')

    entryName = Entry(frame)
    entryName.grid(row=2, column=1, columnspan=2)

    labelUsername = Label(frame, text="Username") 
    labelUsername.grid(row=3, column=0, pady=5, sticky='S')

    entryUsername = Entry(frame)
    entryUsername.grid(row=3, column=1, columnspan=2)

    labelPassword = Label(frame, text="Password") 
    labelPassword.grid(row=4, column=0, pady=5, sticky='S')

    entryPassword = Entry(frame, show="*")
    entryPassword.grid(row=4, column=1, columnspan=2)

    labelMensage = Label(frame, text="")
    labelMensage.grid(row=5, column=0, pady=5, columnspan=2)

    buttonsignIn = Button(frame, text="SignIn", command=lambda: signUp(
        entryName.get(),
        entryUsername.get(),
        entryPassword.get(),
        labelMensage
    ))
    buttonsignIn.grid(row=6, column=1, pady=5)


def signUp(name, username, password, mensage):
   try:
        if name != '' and username != '' and password != '':
            print(name, username, password)
            mainSignUp(name, username, password)
            changeMensaje(mensage, "Registrado correctamente!", "green")
        else:
            changeMensaje(mensage, 'Rellene los campos', 'red')
   except Exception as e:
        print(e)
        changeMensaje(mensage, "Ocurrio un error con la base de datos", "red")

def changeMensaje(mensaje, text, color):
    mensaje['text'] = text
    mensaje['fg'] = color