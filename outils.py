def genDico() :
    charFormate = ""
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéèêëùïîÀÉÈÊËÙÏÎ.?!:.,/\$§£%=+-*\'\"1234567890"


    for lettre in char[::-1] :
        charFormate += "'" + lettre + "', "


    print(charFormate)