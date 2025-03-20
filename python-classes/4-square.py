#!/usr/bin/python3
"""
Module contenant la classe Square, qui représente un carré.
"""


class Square:
    """
    Représente un carré avec un côté donné par l'attribut privé '__size'.
    """

    def __init__(self, size=0):
        """
        Initialise un objet Square avec un attribut 'size'.

        Arguments :
            size (int): La taille du côté du carré. Doit être un entier >= 0.

        Lève des exceptions si le type ou la valeur de 'size' n'est pas valide.
        """
        self.size = size

    @property
    def size(self):
        """
        Permet de récupérer la taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré. Lève une exception si la valeur est invalide.

        Arguments :
            value (int): La taille du côté du carré.
        
        Lève :
            TypeError : Si la valeur n'est pas un entier.
            ValueError : Si la valeur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Retourne :
            int: L'aire du carré, calculée comme le carré de la taille du côté.
        """
        return self.__size ** 2

