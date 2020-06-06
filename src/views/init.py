from tkinter import Tk, messagebox, Frame, Canvas, Button
from src.modules.signOff.index import signOff
from src.views.signIn import printSignIn
from src.views.signUp import printSignUp


def init():
    root = Tk()
    root.title("Proyecto tbd")


    canvas = Canvas(root, height=150, width=200)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    buttonsignIn = Button(frame, text="INGRESAR", command=lambda: printSignIn(canvas))
    buttonsignIn.grid(row=0, column=0, pady=10, padx = 20)

    buttonsignIn = Button(frame, text="REGISTRARSE", command=lambda: printSignUp(canvas))
    buttonsignIn.grid(row=1, column=0, pady=10, padx = 20)


    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            signOff()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

