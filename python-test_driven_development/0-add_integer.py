#!/usr/bin/python3
"""
Ce module fournit une fonction pour additionner deux entiers.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Paramètres :
    a (int ou float) : Le premier nombre.
    b (int ou float, par défaut 98) : Le deuxième nombre.

    Retourne :
    int : La somme de a et b après conversion en entiers.

    Lève :
    TypeError : Si a ou b n'est ni un entier ni un float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
