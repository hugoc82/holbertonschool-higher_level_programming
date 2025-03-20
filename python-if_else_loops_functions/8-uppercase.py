#!/usr/bin/python3
def uppercase(str):
    result = ""  # Une variable pour accumuler les résultats
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):  # Si c est une lettre minuscule
            result += chr(ord(c) - 32)  # Convertir en majuscule et ajouter à result
        else:
            result += c  # Ajouter le caractère tel quel s'il n'est pas une minuscule
    print("{}".format(result))  # Imprimer la chaîne accumulée avec .format()
