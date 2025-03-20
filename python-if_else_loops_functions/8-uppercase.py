#!/usr/bin/python3
def uppercase(str):
    result = ""  # Une variable pour accumuler les résultats
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c  
    print("{}".format(result))  
