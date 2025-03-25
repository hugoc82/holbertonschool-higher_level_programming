def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur et retourne une nouvelle matrice.

    Args:
    matrix (list de list de int/float) : Une matrice (liste de listes) à diviser.
    div (int/float) : Un nombre par lequel diviser les éléments de la matrice.

    Returns:
    list : Une nouvelle matrice où chaque élément est divisé par div, arrondi à 2 décimales.

    Raises:
    TypeError : Si la matrice n'est pas une liste de listes d'entiers ou de flottants, 
                si les lignes de la matrice n'ont pas la même taille, 
                ou si div n'est pas un nombre.
    ZeroDivisionError : Si div est égal à zéro.
    """
    # Vérifier si la matrice est une liste de listes
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérifier si chaque ligne a la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérifier si tous les éléments sont des entiers ou des flottants
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérifier si div est un nombre (entier ou flottant)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérifier si div est égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Diviser chaque élément de la matrice par div et arrondir à 2 décimales
    return [[round(element / div, 2) for element in row] for row in matrix]
