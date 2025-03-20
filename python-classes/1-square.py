#!/usr/bin/python3
"""
Module Square : Ce module définit une classe Square avec un attribut privé size.
"""

class Square:
    """Classe définissant un carré avec un attribut privé size."""
    
    def __init__(self, size):
        """
        Initialise un objet Square avec un attribut privé size.

        Args:
        size (int): La taille du côté du carré
        """
        self.__size = size
