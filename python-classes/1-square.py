#!/usr/bin/python3
"""
Module pour définir une classe Square.
"""

class Square:
    """
    Représente un carré avec un côté donné par l'attribut 'size'.
    """

    def __init__(self, size):
        """
        Initialise un objet Square avec un attribut 'size'.

        Arguments :
            size (int): La taille du côté du carré.
        """
        self.__size = size
