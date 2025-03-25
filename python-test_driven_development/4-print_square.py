#!/usr/bin/python3

def print_square(size):
    """
    Affiche un carré de taille 'size' avec le caractère '#'.

    Args:
        size (int): La taille du carré.

    Raises:
        TypeError: Si 'size' n'est pas un entier ou si 'size' est un flottant négatif.
        ValueError: Si 'size' est inférieur à 0.
    """
    # Vérifier si 'size' est un entier
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Vérifier si 'size' est un nombre négatif
    if size < 0:
        raise ValueError("size must be >= 0")

    # Vérifier si 'size' est un flottant négatif
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Afficher le carré
    for _ in range(size):
        print('#' * size)
