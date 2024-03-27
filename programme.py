# Import des noms du module
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import Tk, Label






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
    clefA = int(valuesClefACrypt.get())
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
    clefA = int(valuesClefACDecrypt.get())
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




























window = tk.Tk()
f = font.Font(family='Bahnschrift')
style1 = font.Font(size=25)
style2 = font.Font(size=15)
style3 = font.Font(size=12)



#Accueil
page1 = Frame(window)
page1.grid(row=0, column=0, sticky="nsew")

tittlePage1 = Label(page1, text="Séléctionnez une méthode de chiffrement", font=style1)
tittlePage1.place(x = 300, y = 10)
tittlePage1.pack()

btnAlphaberCrypt = ttk.Button(page1, text="Chiffrement alphabet inversé", command=lambda: page2.tkraise())
btnAlphaberCrypt.pack()

btnAffineCrypt = ttk.Button(page1, text="Chiffrement affine", command=lambda: page3.tkraise())
btnAffineCrypt.pack()




#Chiffrement alphabet inverse
page2 = Frame(window)
page2.grid(row=0, column=0, sticky="nsew")

tittlePage2 = Label(page2, text="Chiffrement alphabet inversé", font=style1)
tittlePage2.grid(row=0, column=0, columnspan=3)



#ClearToCrypt
clearToCryptSection = Frame(window)


labelEntryClearSentencePage2 = Label(page2, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryClearSentencePage2.grid(row=1, column=0)

entryClearSentencePage2 = Entry(page2)
entryClearSentencePage2['font'] = f
entryClearSentencePage2.grid(row=2, column=0)

btnToCryptPage2 = ttk.Button(page2, text="Chiffrer la phrase", command=lambda: chiffrerPhrase())
btnToCryptPage2.grid(row=3, column=0)


labelEntryCryptedSentencePage2 = Label(page2, text = "Phrase chiffrée :", font=style2)
labelEntryCryptedSentencePage2.grid(row=4, column=0)

displayCryptedSentencePage2 = Entry(page2)
displayCryptedSentencePage2['font'] = f
displayCryptedSentencePage2.grid(row=5, column=0)



#separation
separationPage2 = Canvas(page2, width=5, bg="grey")
separationPage2.grid(row=1,column=1, rowspan=6);


#CryptToClear
labelEntryCryptedSentencePage2 = Label(page2, text = "Entrez la phrase que vous souhaitez déchiffrer", font=style2)
labelEntryCryptedSentencePage2.grid(row=1,column=2)

entryCryptedSentencePage2 = Entry(page2)
entryCryptedSentencePage2['font'] = f
entryCryptedSentencePage2.grid(row=2,column=2)

btnToDecryptPage2 = ttk.Button(page2, text="déchiffrer la phrase", command=lambda: dechiffrerPhrase())
btnToDecryptPage2.grid(row=3,column=2)

labelEntryDecryptedSentencePage2 = Label(page2, text = "Phrase déchiffrée :", font=style2)
labelEntryDecryptedSentencePage2.grid(row=4,column=2)

displayClearSentencePage2 = Entry(page2)
displayClearSentencePage2['font'] = f
displayClearSentencePage2.grid(row=5,column=2)



btnReturnHomePage2 = ttk.Button(page2, text="Retour à l'accueil", command=lambda: page1.tkraise())
btnReturnHomePage2.grid(row=7, column=0, columnspan=3)












#Chiffrement affine
page3 = Frame(window)
page3.grid(row=0, column=0, sticky="nsew")

tittlePage3 = Label(page3, text="Chiffrement affine", font=style1)
tittlePage3.grid(row=0, column=0, columnspan=4)


#ClearToCrypt
labelEntryClearSentencePage3 = Label(page3, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryClearSentencePage3.grid(row=1, column=0)

entryClearSentencePage3 = Entry(page3)
entryClearSentencePage3['font'] = f
entryClearSentencePage3.grid(row=2, column=0)



labelEntryClefA = Label(page3, text = "Séléctionnez la clef \"a\"", font=style2)
labelEntryClefA.grid(row=3, column=0)



valuesClefACrypt = IntVar()
valuesClefACrypt.set("1")
dropListClefACrypt = OptionMenu(page3, valuesClefACrypt, 1, 17)
dropListClefACrypt.grid(row=4, column=0)



labelEntryClefB = Label(page3, text = "Entrez la clef \"b\"", font=style2)
labelEntryClefB.grid(row=5, column=0)

entryClefB = Entry(page3)
entryClefB['font'] = f
entryClefB.grid(row=6, column=0)


btnToCryptPage3 = ttk.Button(page3, text="Chiffrer la phrase", command=lambda: crypt())
btnToCryptPage3.grid(row=7, column=0)



labelEntryCryptedSentencePage3 = Label(page3, text = "Phrase chiffrée :", font=style2)
labelEntryCryptedSentencePage3.grid(row=8, column=0)

displayCryptedSentencePage3 = Entry(page3)
displayCryptedSentencePage3['font'] = f
displayCryptedSentencePage3.grid(row=9, column=0)



#separation
separationPage2 = Canvas(page3, width=5, bg="grey")
separationPage2.grid(row=1,column=1, rowspan=10);


#CryptToDecrypt
labelEntryCryptedSentencePage3 = Label(page3, text = "Entrez la phrase que vous souhaitez chiffrer", font=style2)
labelEntryCryptedSentencePage3.grid(row=1, column=3)

entryCryptedSentencePage3 = Entry(page3)
entryCryptedSentencePage3['font'] = f
entryCryptedSentencePage3.grid(row=2, column=3)



labelClefAToDecrypt = Label(page3, text = "Séléctionnez la clef \"a\"", font=style2)
labelClefAToDecrypt.grid(row=3, column=3)


valuesClefACDecrypt = IntVar()
valuesClefACDecrypt.set("1")
dropListClefACDecrypt = OptionMenu(page3, valuesClefACDecrypt, 1, 17)
dropListClefACDecrypt.grid(row=4, column=3)


labelClefBToDecrypt = Label(page3, text = "Entrez la clef \"b\"", font=style2)
labelClefBToDecrypt.grid(row=5, column=3)

entryClefBToDecrypt = Entry(page3)
entryClefBToDecrypt['font'] = f
entryClefBToDecrypt.grid(row=6, column=3)


btnToDecryptPage3 = ttk.Button(page3, text="déchiffrer la phrase", command=lambda: decrypt())
btnToDecryptPage3.grid(row=7, column=3)



labelEntryDecryptedSentencePage3 = Label(page3, text = "Phrase déchiffrée :", font=style2)
labelEntryDecryptedSentencePage3.grid(row=8, column=3)

displayDecryptedSentencePage3 = Entry(page3)
displayDecryptedSentencePage3['font'] = f
displayDecryptedSentencePage3.grid(row=9, column=3)




btnReturnHomePage3 = ttk.Button(page3, text="Retour à l'accueil", command=lambda: page1.tkraise())
btnReturnHomePage3.grid(row=11, column=0, columnspan=4)




page1.tkraise()
window.resizable(False, False)


window.title("Chiffrator2000")


window.mainloop()







