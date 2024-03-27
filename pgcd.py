def pgcd(nbChars) :

    i = 0 
    listPgcd = []

    while i < nbChars :
        i += 1

        print(i)

        if i < nbChars :
            i, nbChars = nbChars, i

        if i % nbChars == 0 :
            print(i)
            listPgcd.append(i) 

        for k in range(nbChars//2, 0, -1) :
            if k % k == 0 and nbChars % k == 0 :
                listPgcd.append("test")

    print(listPgcd)
        

