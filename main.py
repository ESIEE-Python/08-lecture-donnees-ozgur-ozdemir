"""
08-lecture-donnees-ozgur-ozdemir
"""
import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        # Récupérer chaque ligne et la convertir en liste d'entiers
        l = [list(map(int, line.strip().split(';'))) for line in f.readlines()]
    return l

def get_list_k(data, k):
    """ retourne la k eme liste de donnée"""
    return data[k] if 0 <= k < len(data) else None

def get_first(l):
    """ retourne le premier élément de la liste"""
    return l[0] if l else None

def get_last(l):
    """ retourne le dernier élément de la liste"""
    return l[-1] if l else None

def get_max(l):
    """ retourne le max de la liste """
    return max(l) if l else None

def get_min(l):
    """retourne le min de la liste """
    return min(l) if l else None

def get_sum(l):
    """ retourne la somme des elements"""
    return sum(l) if l else 0

#### Fonction principale

def main():
    """ fonction principale"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(f"Ligne {i}: {l}")

    k = 0  # Exemple d'indice à tester
    print(f"Liste à l'indice {k}: {get_list_k(data, k)}")

    # Exemple d'utilisation des autres fonctions sur la première liste
    first_list = get_list_k(data, k)
    if first_list:
        print(f"Premier élément: {get_first(first_list)}")
        print(f"Dernier élément: {get_last(first_list)}")
        print(f"Maximum: {get_max(first_list)}")
        print(f"Minimum: {get_min(first_list)}")
        print(f"Somme: {get_sum(first_list)}")

if __name__ == "__main__":
    main()
