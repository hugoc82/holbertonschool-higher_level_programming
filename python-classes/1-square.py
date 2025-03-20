#!/usr/bin/python3
"""
Module Square : Ce module définit une classe Square avec un attribut privé 'size'.
"""

class Square:
    """
    Classe représentant un carré.

    Elle contient un attribut privé 'size' pour la taille du côté du carré.
    """

    def __init__(self, size):
        """
        Initialise un objet Square avec un attribut privé 'size'.

        Arguments :
            size (int) : La taille du côté du carré.
        """
        self.__size = size

