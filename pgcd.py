def pgcd(clefA, nbChars) :

    if clefA < nbChars :
        clefA, nbChars = nbChars, clefA

    if clefA % nbChars == 0 :
        return nbChars

    for i in range(nbChars//2, 0, -1) :
        if clefA % i == 0 and nbChars % i == 0 :
            return i


