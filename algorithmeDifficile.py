listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def cryptText(listeChars, lettre, a, b) :
    clearSentence = "abcd"
    cryptedSentence = ""


    for lettre in clearSentence :
        indexOfLetter = getIndexOfLetter(listeChars, lettre)
        indexAfterAffine = applyAffineFunction(indexOfLetter, a, b)
        indexAfterAffineAndModulo = applyModulo(indexAfterAffine)
        cryptedLetter = getCryptedLetter(listeChars, indexAfterAffineAndModulo)

        cryptedSentence += cryptedLetter

    print("Non codé : " + clearSentence)
    print("Codé : " + cryptedSentence)



def getIndexOfLetter(listeChars, lettre) :
    return listeChars.index(lettre)


def applyAffineFunction(indexOfLetter, a, b) :
    return a * indexOfLetter + b


def applyModulo(indexAfterAffine) :
    return indexAfterAffine % 26


def getCryptedLetter(listeChars, indexAfterAffineAndModulo) :
    return listeChars[indexAfterAffineAndModulo]











