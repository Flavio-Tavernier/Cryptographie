listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

listeCharsInverses = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']





def chiffrerPhrase() :

    phraseNonChiffre = "test"

    phraseChiffre = ""

    for lettre in phraseNonChiffre :
        #Recupere num lettre inverse
        numLettreInverse = listeCharsInverses.index(lettre)

        #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
        lettreInverse = listeChars[numLettreInverse]

        #Concatene la chaine de caracteres
        phraseChiffre +=  lettreInverse

        print(lettre)
        print(numLettreInverse)
        print(lettreInverse)
        print("\n")


    print(phraseNonChiffre)
    print(phraseChiffre)



def deChiffrerPhrase() :

    phraseChiffre = "gvhg"

    phraseNonChiffre = ""

    for lettre in phraseChiffre :
        #Recupere num lettre inverse
        numLettre = listeChars.index(lettre)

        #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
        lettreNonchiffre = listeCharsInverses[numLettre]

        #Concatene la chaine de caracteres
        phraseNonChiffre +=  lettreNonchiffre

        print(lettre)
        print(numLettre)
        print(lettreNonchiffre)
        print("\n")


    print(phraseChiffre)
    print(phraseNonChiffre)


















