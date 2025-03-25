#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Affiche le nom complet sous la forme : "My name is <first name> <last name>".

    Args:
        first_name (str): Le prénom.
        last_name (str): Le nom de famille (facultatif).

    Raises:
        TypeError: Si first_name ou last_name ne sont pas des chaînes de caractères.
    """
    # Vérifier que first_name est une chaîne de caractères
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Vérifier que last_name est une chaîne de caractères
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
