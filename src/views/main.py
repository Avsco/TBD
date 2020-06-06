from tkinter import Tk, messagebox
from signIn import printSignIn
from src.modules.signOff.index import signOff
#from signUp import printSignUp


root = Tk()
root.title("Proyecto tbd")

printSignIn(root)
#printSignUp(root)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        signOff()
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()