listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'à', 'é', 'è', 'ê', 'ë', 'ù', 'ï', 'î', 'À', 'É', 'È', 'Ê', 'Ë', 'Ù', 'Ï', 'Î', '.', '?', '!', ':', '.', ',', '/', '\\', '$', '§', '£', '%', '=', '+', '-', '*', '\'', '\"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

listeCharsInverses = ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1', '\"', '\'', '*', '-', '+', '=', '%', '£', '§', '$', '\\', '/', ',', '.', ':', '!', '?', '.', 'Î', 'Ï', 'Ù', 'Ë', 'Ê', 'È', 'É', 'À', 'î', 'ï', 'ù', 'ë', 'ê', 'è', 'é', 'à', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']



print(listeChars[0+1])


def chiffrerPhrase() :
    phrase = input("Entrez la phrase que vous souhaitez chiffrer : ")

    phraseChiffre = inverserChars(phrase, listeChars, listeCharsInverses)

    return phraseChiffre



def inverserChars(phrase, listeChars, listeCharsInverses) :
    phraseChiffre = ""

    for lettre in phrase :
        if lettre == " " :
            phraseChiffre += " "
        else :
            #Recupere num lettre inverse
            numLettreSuivante = listeChars.index(lettre) + 1

            #Recupere la lettre inverse dans la liste alphabet normal par rapport au num lettre inverse
            lettreSuivante = listeChars[numLettreSuivante]

            #Concatene la chaine de caracteres
            phraseChiffre +=  lettreSuivante


    print("\n\t\tPhrase déchiffrée : " + phrase)
    print("\t\tPhrase chiffrée : " + phraseChiffre)
















