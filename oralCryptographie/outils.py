import math

def genListe() :
    charFormate = ""
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéèêëùïîÀÉÈÊËÙÏÎ.?!:.,/\$§£%=+-*\'\"1234567890"


    for lettre in char[::-1] :
        charFormate += "'" + lettre + "', "


    print(charFormate)


def pgcd(a, nbChars) :
        if a < nbChars :
            a, nbChars = nbChars, a

        if a % nbChars == 0 :
            return nbChars

        for k in range(nbChars//2, 0, -1) :
            if a % k == 0 and nbChars % k == 0 :
                return k

    


def getListePremier(nbChars) :
    i = 0
    listeNombrePremiersAvecNbChars = []


    for i in range(nbChars) :
        i += 1  
        if (pgcd(i, nbChars) == 1) :
            listeNombrePremiersAvecNbChars.append(i)

    print(listeNombrePremiersAvecNbChars)



def pgcdFacile() :
     
    listePGCD = []

    for i in range (96) :
        i+=1
        if math.gcd(i,96) == 1 :
            listePGCD.append(i)

    print(listePGCD)