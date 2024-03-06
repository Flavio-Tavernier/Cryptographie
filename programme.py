# Import des noms du module
from tkinter import *
from tkinter import ttk


# Création d'un objet "fenêtre"
fenetre = Tk()
fenetre.geometry("600x300")


titre = Label(fenetre, text = "Séléctionnez votre méthode de chiffrement")
titre.pack()


reverseAlphabet = ttk.Button(fenetre, text = "Chiffrement alphabet inversé")
reverseAlphabet.place(x = 80 , y = 110)

affine = ttk.Button(fenetre, text = "Chiffrement affine")
affine.place(x = 380 , y = 110)


fenetre.mainloop()





