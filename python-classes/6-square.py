#!/usr/bin/python3
"""
Module contenant la classe Square, qui représente un carré avec une position.
"""


class Square:
    """
    Représente un carré avec un côté donné par l'attribut privé '__size'
    et une position donnée par l'attribut privé '__position'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un objet Square avec un attribut 'size' et 'position'.

        Arguments :
            size (int): La taille du côté du carré. Doit être un entier >= 0.
            position (tuple): La position du carré, un tuple de deux entiers.
                              Doit être une paire d'entiers positifs (x, y).
        Lève des exceptions si le type ou la valeur de 'size' ou 'position' n'est pas valide.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Permet d'obtenir la taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Arguments :
            value (int): La nouvelle taille du carré. Doit être un entier >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Permet d'obtenir la position du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Arguments :
            value (tuple): La nouvelle position du carré. Doit être une paire d'entiers positifs (x, y).
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retour :
            int : L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère '#' dans la sortie standard,
        en respectant la position spécifiée.

        Si la taille est égale à 0, affiche une ligne vide.
        La position doit être respectée par des espaces avant le carré.
        """
        if self.__size == 0:
            print()
        else:
            # Imprimer les lignes vides avant le carré selon position[1]
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                # Imprimer les espaces avant le carré selon position[0]
                print(' ' * self.__position[0] + '#' * self.__size)

