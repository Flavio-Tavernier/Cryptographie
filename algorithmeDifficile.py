listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
            decrypt(infosUser[0], infosUser[1], infosUser[2], listeChars)
            print("\n\t\tNon codé : " + clearSentence)
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
        indexOfLetter = getIndexOfLetter(listeChars, lettre)
        indexAfterAffine = applyAffineFunction(indexOfLetter, clefA, clefB)
        indexAfterAffineAndModulo = applyModulo(indexAfterAffine)
        cryptedLetter = getCryptedLetter(listeChars, indexAfterAffineAndModulo)

        cryptedSentence += cryptedLetter

    return cryptedSentence




def getIndexOfLetter(listeChars, lettre) :
    return listeChars.index(lettre)


def applyAffineFunction(indexOfLetter, clefA, clefB) :
    return clefA * indexOfLetter + clefB


def applyModulo(indexAfterAffine) :
    return indexAfterAffine % 26


def getCryptedLetter(listeChars, indexAfterAffineAndModulo) :
    return listeChars[indexAfterAffineAndModulo]







# Affichage du mot déchiffré
def decrypt(listeChars):

    cryptedSentence = input("Entrez la phrase que vous souhaitez déchiffrer : ")
    clefA = int(input("Entrez la clef a : "))
    clefB = int(input("Entrez la clef b : "))
    clearSentence = ""

    for lettre in cryptedSentence :
        clearSentence += affineDecrypting(clefA,clefB,lettre, listeChars)

    return clearSentence



# Fonction de déchiffrement
def affineDecrypting(clefA,clefB,lettre,listeChars):

    indexOfCryptedLetter = getIndexOfLetter(listeChars, lettre)

    indexOfClearLetter =(inverse(clefA)*(indexOfCryptedLetter-clefB))%26

    return listeChars[indexOfClearLetter]


def inverse(clefA):
        indexOfClearLetter=0
        while (clefA * indexOfClearLetter % 26 != 1):
                indexOfClearLetter = indexOfClearLetter + 1
        return indexOfClearLetter





































