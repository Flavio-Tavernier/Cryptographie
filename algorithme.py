import random

dicoAlphabetNormal = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52, 'à':53, 'é':54, 'è':55, 'ê':56, 'ë':57, 'ù':58, 'ï':59, 'î':60, 'À':61, 'É':62, 'È':63, 'Ê':64, 'Ë':65, 'Ù':66, 'Ï':67, 'Î':68, '!':69, ';':70, '/':71, "'":72, '"':73, ':':74, '.':75, '%':76, '*':77, '$':78}

dicoAlphabetInverse = {'a':78, 'b':77, 'c':76, 'd':75, 'e':74, 'f':73, 'g':72, 'h':71, 'i':70, 'j':69, 'k':68, 'l':67, 'm':66, 'n':65, 'o':64, 'p':63, 'q':62, 'r':61, 's':60, 't':59, 'u':58, 'v':57, 'w':56, 'x':55, 'y':54, 'z':53, 'A':52, 'B':51, 'C':50, 'D':49, 'E':48, 'F':47, 'G':46, 'H':45, 'I':44, 'J':43, 'K':42, 'L':41, 'M':40, 'N':39, 'O':38, 'P':37, 'Q':36, 'R':35, 'S':34, 'T':33, 'U':32, 'V':31, 'W':30, 'X':29, 'Y':28, 'Z':27, 'à':26, 'é':25, 'è':24, 'ê':23, 'ë':22, 'ù':21, 'ï':20, 'î':19, 'À':18, 'É':17, 'È':16, 'Ê':15, 'Ë':14, 'Ù':13, 'Ï':12, 'Î':11, '!':10, ';':9, '/':8, "'":7, '"':6, ':':5, '.':4, '%':3, '*':2, '$':1}



def chiffrerPhrase() :
    phrase = "je m'appelle flavio j'ai mangé !./:$*"

    inverserAlphabet(phrase, dicoAlphabetNormal, dicoAlphabetInverse)



def inverserAlphabet(phrase, dicoAlphabetNormal, dicoAlphabetInverse) :
   
    phraseChiffre = ""

    for lettre in phrase :
        if lettre == " " :
            phraseChiffre += ""
        else :
            #Recupere num lettre inverse
            numLettreInverse = dicoAlphabetInverse[lettre]
            #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
            lettreInverse = list(dicoAlphabetNormal)[numLettreInverse - 1]
            #Concatene la chaine de caracteres
            phraseChiffre +=  lettreInverse

    print(phrase)
    print(phraseChiffre)






def genDico() :
    charFormate = ""
    i = 0
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéèêëùïîÀÉÈÊËÙÏÎ!;/'\":.%*$"


    for lettre in char :
        i+=1
        charFormate += "'" + lettre + "':" + str(i) + ", "

    print(charFormate)





def getPhraseAleatoire(dicoAlphabetNormal) :

    phraseAleatoire = ""

    for i in range(12) :
        nombreAleatoire = random.randint(1, 26)
        lettreAleatoire = list(dicoAlphabetNormal)[nombreAleatoire - 1]
        phraseAleatoire += lettreAleatoire







