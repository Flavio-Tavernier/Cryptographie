def dechiffreMsgArmee() :

    listeChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'à', 'é', 'è', 'ê', 'ë', 'ù', 'ï', 'î', 'À', 'É', 'È', 'Ê', 'Ë', 'Ù', 'Ï', 'Î', '.', '?', '!', ':', '.', ',', '/', '\\', '*', '\'', '\"', "’", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    msgArmee = "Ibp Xojbbp coxkzxfpbp p’bkqoxfkbkq xr zljyxq zvybo"

    msgDechiffre = ""


    for lettre in msgArmee :
        if lettre == " " :
            msgDechiffre += " "
        else :
            indexLettreDechiffree = listeChars.index(lettre) + 3

            msgDechiffre += listeChars[indexLettreDechiffree]

    print(msgDechiffre)