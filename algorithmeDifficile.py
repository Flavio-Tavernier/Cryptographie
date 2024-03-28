listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'à', 'é', 'è', 'ê', 'ë', 'ù', 'ï', 'î', 'À', 'É', 'È', 'Ê', 'Ë', 'Ù', 'Ï', 'Î', '.', '?', '!', ':', '.', ',', '/', '\\', '$', '§', '£', '%', '=', '+', '-', '*', '\'', '\"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

nbChars = len(listeChars)

def programme() :
    while True :
        print(
        """
        Algorithme de chiffrement affine :

        Pour chiffrer une phrase tappez 1
        Pour déchiffrer une phrase tappez 2
        Pour quitter tappez sur une touche
        """
        )

        choix = input()

        if choix == "1" :
            infosUser = askInfosUser()
            cryptedSentence = crypt(infosUser[0], infosUser[1], infosUser[2], listeChars)
            print("\n\t\tCodé : " + cryptedSentence)
        elif choix == "2" :
            infosUser = askInfosUser()
            clearSentence = decrypt(infosUser[0], infosUser[1], infosUser[2], listeChars)
            print("\n\t\tDécodé : " + clearSentence)
        else :
            break



def askInfosUser() :
    clearSentence = input("Entrez la phrase que vous souhaitez chiffrer : ")
    clefA = int(input("Entrez la clef a : "))
    clefB = int(input("Entrez la clef b : "))

    infosUser = [clefA, clefB, clearSentence]

    return infosUser




def crypt(clefA, clefB, clearSentence, listeChars) :
    cryptedSentence = ""


    for lettre in clearSentence :
        print(lettre)
        if lettre == " " :
            cryptedSentence += " "
        else :
            indexOfLetter = getIndexOfLetter(listeChars, lettre)
            print(indexOfLetter)
            indexAfterAffine = applyAffineFunction(indexOfLetter, clefA, clefB)
            print(indexAfterAffine)
            indexAfterAffineAndModulo = applyModulo(indexAfterAffine)
            print(indexAfterAffineAndModulo)
            cryptedLetter = getCryptedLetter(listeChars, indexAfterAffineAndModulo)
            print(cryptedLetter)
            cryptedSentence += cryptedLetter

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
def decrypt(clefA, clefB, cryptedSentence, listeChars):

    clearSentence = ""

    for lettre in cryptedSentence :
        if lettre == " " :
            clearSentence += " "
        else :
            clearSentence += affineDecrypting(clefA,clefB,lettre, listeChars)

    return clearSentence


def affineDecrypting(clefA,clefB,lettre,listeChars):

    print(lettre)
    indexOfCryptedLetter = getIndexOfLetter(listeChars, lettre)
    print(indexOfCryptedLetter)
    indexOfClearLetter =(inverse(clefA)*(indexOfCryptedLetter-clefB)) % nbChars
    print(indexOfClearLetter)
    return listeChars[indexOfClearLetter]


def inverse(clefA):
        indexOfClearLetter=0
        while (clefA * indexOfClearLetter % nbChars != 1):
                indexOfClearLetter = indexOfClearLetter + 1
        return indexOfClearLetter





































