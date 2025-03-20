#!/usr/bin/python3
"""
Module pour définir une classe Square.
La classe Square définit un carré avec un côté spécifique
et permet de manipuler cet objet de manière simple.
"""

class Square:
    """
    Représente un carré avec un côté donné par l'attribut 'size'.

    Attributs:
        size (int): La taille du côté du carré.
    """

    def __init__(self, size):
        """
        Initialise un objet Square avec un attribut 'size'.

        Arguments :
            size (int): La taille du côté du carré.
        """
        self.__size = size
