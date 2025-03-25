#!/usr/bin/python3

def text_indentation(text):
    """
    Affiche le texte en insérant deux nouvelles lignes après chaque '.', '?', et ':'.

    Args:
        text (str): Le texte à traiter.

    Raises:
        TypeError: Si `text` n'est pas une chaîne de caractères.
    """
    # Vérifier si le texte est une chaîne de caractères
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # On va parcourir le texte et traiter les caractères
    i = 0
    while i < len(text):
        # Si le caractère est un '.', '?' ou ':', on imprime et on ajoute deux nouvelles lignes
        if text[i] in ['.', '?', ':']:
            print(text[i], end='')
            print()  # Ajouter une nouvelle ligne
            print()  # Ajouter une deuxième nouvelle ligne
            i += 1  # Passer au caractère suivant
            while i < len(text) and text[i] == ' ':
                i += 1  # Sauter les espaces blancs après le ponctuation
        else:
            print(text[i], end='')
            i += 1
