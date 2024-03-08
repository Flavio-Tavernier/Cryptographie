# Import des noms du module
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import Tk, Label


window = tk.Tk()
f = font.Font(family='Bahnschrift')
style1 = font.Font(size=16)
style2 = font.Font(size=12)



#Accueil
page1 = Frame(window)
page1.grid(row=0, column=0, sticky="nsew")

tittlePage1 = Label(page1, text="Séléctionnez une méthode de chiffrement", font=style1)
tittlePage1.place(x = 300, y = 10)
#tittlePage1.pack()

btnAlphaberCrypt = ttk.Button(page1, text="Chiffrement alphabet inversé", command=lambda: page2.tkraise())
btnAlphaberCrypt.pack()

btnAffineCrypt = ttk.Button(page1, text="Chiffrement affine", command=lambda: page3.tkraise())
btnAffineCrypt.pack()







#Chiffrement alphabet inverse
page2 = Frame(window)
page2.grid(row=0, column=0, sticky="nsew")

tittlePage2 = Label(page2, text="Chiffrement alphabet inversé", font=style1)
tittlePage2.pack(pady=20, side=TOP, anchor=W, fill=X, expand=YES)



#ClearToCrypt
labelEntryClearSentencePage2 = Label(page2, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryClearSentencePage2.pack()

entryClearSentencePage2 = Entry(page2)
entryClearSentencePage2['font'] = f
entryClearSentencePage2.pack(side=TOP, anchor=W, fill=X, expand=YES)


labelEntryCryptedSentencePage2 = Label(page2, text = "Phrase chiffrée :", font=style2)
labelEntryCryptedSentencePage2.pack()

displayCryptedSentencePage2 = Entry(page2)
displayCryptedSentencePage2['font'] = f
displayCryptedSentencePage2.pack(side=TOP, anchor=W, fill=X, expand=YES)


btnToCryptPage2 = Button(page2, text="Chiffrer la phrase", command=lambda: chiffrerPhrase(), font=style2)
btnToCryptPage2.pack(side=TOP, anchor=W, fill=X, expand=YES)




#CryptToClear
labelEntryCryptedSentencePage2 = Label(page2, text = "Entrez la phrase que vous souhaitez déchiffrer", font=style2)
labelEntryCryptedSentencePage2.pack()

entryCryptedSentencePage2 = Entry(page2)
entryCryptedSentencePage2['font'] = f
entryCryptedSentencePage2.pack(side=TOP, anchor=W, fill=X, expand=YES)

btnToDecryptPage2 = Button(page2, text="déchiffrer la phrase", command=lambda: dechiffrerPhrase(), font=style2)
btnToDecryptPage2.pack(side=TOP, anchor=W, fill=X, expand=YES)

labelEntryDecryptedSentencePage2 = Label(page2, text = "Phrase déchiffrée :", font=style2)
labelEntryDecryptedSentencePage2.pack()

displayClearSentencePage2 = Entry(page2)
displayClearSentencePage2['font'] = f
displayClearSentencePage2.pack(side=TOP, anchor=W, fill=X, expand=YES)



btnReturnHomePage2 = Button(page2, text="Retour à l'accueil", command=lambda: page1.tkraise(), font=style2)
btnReturnHomePage2.pack(side=BOTTOM, anchor=W, fill=X, expand=YES)






#Chiffrement affine
page3 = Frame(window)
page3.grid(row=0, column=0, sticky="nsew")

tittlePage3 = Label(page3, text="Chiffrement affine", font=style1)
tittlePage3.pack(pady=20)


#ClearToCrypt
labelEntryClearSentencePage3 = Label(page3, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryClearSentencePage3.pack()

entryClearSentencePage3 = Entry(page3)
entryClearSentencePage3['font'] = f
entryClearSentencePage3.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelEntryClefA = Label(page3, text = "Entrez la clef \"a\"", font=style2)
labelEntryClefA.pack()

entryClefA = Entry(page3)
entryClefA['font'] = f
entryClefA.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelEntryClefB = Label(page3, text = "Entrez la clef \"b\"", font=style2)
labelEntryClefB.pack()

entryClefB = Entry(page3)
entryClefB['font'] = f
entryClefB.pack(side=TOP, anchor=W, fill=X, expand=YES)


btnToCryptPage3 = Button(page3, text="Chiffrer la phrase", command=lambda: crypt(), font=style2)
btnToCryptPage3.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelEntryCryptedSentencePage3 = Label(page3, text = "Phrase chiffrée :", font=style2)
labelEntryCryptedSentencePage3.pack()

displayCryptedSentencePage3 = Entry(page3)
displayCryptedSentencePage3['font'] = f
displayCryptedSentencePage3.pack(side=TOP, anchor=W, fill=X, expand=YES)




#CryptToDecrypt
labelEntryCryptedSentencePage3 = Label(page3, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryCryptedSentencePage3.pack()

entryCryptedSentencePage3 = Entry(page3)
entryCryptedSentencePage3['font'] = f
entryCryptedSentencePage3.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelClefAToDecrypt = Label(page3, text = "Entrez la clef \"a\"", font=style2)
labelClefAToDecrypt.pack()

entryClefAToDecrypt = Entry(page3)
entryClefAToDecrypt['font'] = f
entryClefAToDecrypt.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelClefBToDecrypt = Label(page3, text = "Entrez la clef \"b\"", font=style2)
labelClefBToDecrypt.pack()

entryClefBToDecrypt = Entry(page3)
entryClefBToDecrypt['font'] = f
entryClefBToDecrypt.pack(side=TOP, anchor=W, fill=X, expand=YES)


btnToDecryptPage3 = Button(page3, text="déchiffrer la phrase", command=lambda: decrypt(), font=style2)
btnToDecryptPage3.pack(side=TOP, anchor=W, fill=X, expand=YES)



labelEntryDecryptedSentencePage3 = Label(page3, text = "Phrase déchiffrée :", font=style2)
labelEntryDecryptedSentencePage3.pack()

displayDecryptedSentencePage3 = Entry(page3)
displayDecryptedSentencePage3['font'] = f
displayDecryptedSentencePage3.pack(side=TOP, anchor=W, fill=X, expand=YES)




btnReturnHome = Button(page3, text="Retour à l'accueil", command=lambda: page1.tkraise(), font=style2)
btnReturnHome.pack()




page1.tkraise()
window.geometry("1200x600")
window.resizable(False, False)


window.title("Chiffrator2000")


window.mainloop()












listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'à', 'é', 'è', 'ê', 'ë', 'ù', 'ï', 'î', 'À', 'É', 'È', 'Ê', 'Ë', 'Ù', 'Ï', 'Î', '.', '?', '!', ':', '.', ',', '/', '\\', '$', '§', '£', '%', '=', '+', '-', '*', '\'', '\"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

listeCharsInverses = ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1', '\"', '\'', '*', '-', '+', '=', '%', '£', '§', '$', '\\', '/', ',', '.', ':', '!', '?', '.', 'Î', 'Ï', 'Ù', 'Ë', 'Ê', 'È', 'É', 'À', 'î', 'ï', 'ù', 'ë', 'ê', 'è', 'é', 'à', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']



nbChars = len(listeChars)


def chiffrerPhrase() :
    phrase = entryClearSentencePage2.get()

    print(phrase)

    phraseChiffre = inverserChars(phrase, listeChars, listeCharsInverses)

    print(phraseChiffre)

    displayCryptedSentencePage2.delete(0, "end")
    displayCryptedSentencePage2.insert(0, phraseChiffre)


def dechiffrerPhrase() :
    phraseChiffre = entryCryptedSentencePage2.get()

    phraseDechiffre = retablirChars(phraseChiffre)

    displayClearSentencePage2.delete(0, "end")
    displayClearSentencePage2.insert(0, phraseDechiffre)



def inverserChars(phrase, listeChars, listeCharsInverses) :
    phraseChiffre = ""

    for lettre in phrase :
        if lettre == " " :
            phraseChiffre += " "
        else :
            #Recupere num lettre inverse
            numLettreInverse = listeCharsInverses.index(lettre)

            #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
            lettreInverse = listeChars[numLettreInverse]

            #Concatene la chaine de caracteres
            phraseChiffre +=  lettreInverse


    print("\n\t\tPhrase déchiffrée : " + phrase)
    print("\t\tPhrase chiffrée : " + phraseChiffre)
    return phraseChiffre




def retablirChars(phraseChiffre) :
    phraseDechiffre = ""


    for lettre in phraseChiffre :
        if lettre == " " :
            phraseDechiffre += " "
        else :
            #Recupere num lettre inverse
            numLettreALendroit = listeChars.index(lettre)

            #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
            lettreNormale = listeCharsInverses[numLettreALendroit]

            #Concatene la chaine de caracteres
            phraseDechiffre +=  lettreNormale

    print("\n\t\tPhrase chiffrée : " + phraseChiffre)
    print("\t\tPhrase déchiffrée : " + phraseDechiffre)
    return phraseDechiffre
















def crypt() :
    clefA = int(entryClefA.get())
    clefB = int(entryClefB.get())
    clearSentence = entryClearSentencePage3.get()

    cryptedSentence = ""


    for lettre in clearSentence :
        if lettre == " " :
            cryptedSentence += " "
        else :
            indexOfLetter = getIndexOfLetter(listeChars, lettre)
            indexAfterAffine = applyAffineFunction(indexOfLetter, clefA, clefB)
            indexAfterAffineAndModulo = applyModulo(indexAfterAffine)
            cryptedLetter = getCryptedLetter(listeChars, indexAfterAffineAndModulo)

            cryptedSentence += cryptedLetter

    displayCryptedSentencePage3.delete(0, 'end')
    displayCryptedSentencePage3.insert(0, cryptedSentence)
    return cryptedSentence




def getIndexOfLetter(listeChars, lettre) :
    return listeChars.index(lettre)


def applyAffineFunction(indexOfLetter, clefA, clefB) :
    return clefA * indexOfLetter + clefB


def applyModulo(indexAfterAffine) :
    return indexAfterAffine % nbChars


def getCryptedLetter(listeChars, indexAfterAffineAndModulo) :
    return listeChars[indexAfterAffineAndModulo]





# Dechiffrement
def decrypt():
    clefA = int(entryClefAToDecrypt.get())
    clefB = int(entryClefBToDecrypt.get())
    cryptedSentence = entryCryptedSentencePage3.get()
    decryptedSentence = ""

    for lettre in cryptedSentence :
        if lettre == " " :
            decryptedSentence += " "
        else :
            decryptedSentence += affineDecrypting(clefA,clefB,lettre, listeChars)

    displayDecryptedSentencePage3.delete(0, 'end')
    displayDecryptedSentencePage3.insert(0, decryptedSentence)
    return decryptedSentence


def affineDecrypting(clefA,clefB,lettre,listeChars):

    indexOfCryptedLetter = getIndexOfLetter(listeChars, lettre)

    indexOfClearLetter =(inverse(clefA)*(indexOfCryptedLetter-clefB)) % nbChars

    return listeChars[indexOfClearLetter]


def inverse(clefA):
        indexOfClearLetter=0
        while (clefA * indexOfClearLetter % nbChars != 1):
                indexOfClearLetter = indexOfClearLetter + 1
        return indexOfClearLetter














