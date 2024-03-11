import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.font as font



gui = Tk()

styleLabel = ttk.Style()
styleLabel.configure("font.TLabel", font='Helvetica 18 bold')

styleBtn = ttk.Style()
styleBtn.configure("font.TButton", font='Helvetica 14 bold')



# ---------- Accueil ----------
homePage = Frame(gui)
homePage.grid(row=0, column=0, sticky="nsew")


title = Label(homePage, text="Séléctionnez votre méthode de chiffrement", style="font.TLabel")
title.grid(row=0, column=0, columnspan=2)


btnSelectAlphabet = Button(homePage, text ="Chiffrement alphabet inversé", command=lambda: alphabetPage.tkraise(), style="font.TButton")
btnSelectAlphabet.grid(row=1, column=0)


btnSelectAffine = ttk.Button(homePage, text="Chiffrement affine", style="font.TButton")
btnSelectAffine.grid(row=1, column=1)


# ----------  ----------






# ---------- Page Alphabet inverse ----------
alphabetPage = Frame(gui)
alphabetPage.grid(row=0, column=0, sticky="nsew")


titlePage2 = Label(alphabetPage, text="Séléctionnez votre méthode de chiffrement", style="font.TLabel")
titlePage2.place(x=250, y=50, anchor="center")
titlePage2.grid(row=0, column=0)








homePage.tkraise()
gui.title("Chiffrator2000")
gui.geometry('500x200')
#gui.resizable(height = False, width = False)

gui.mainloop()


