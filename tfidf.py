import math
from collections import Counter


def construire_vocabulaire(phrases):
    """
    Construit le vocabulaire (liste des mots uniques) à partir des phrases.

    Args:
        phrases (list of list of str): liste de phrases, où chaque phrase est une liste de mots.

    Returns:
        list: vocabulaire trié contenant tous les mots uniques.
    """
    # On veut trouver tous les mots différents
    vocabulaire = set()  # un set = ensemble sans doublons
    for phrase in phrases:  # on parcourt chaque phrase
        for mot in phrase:  # on parcourt chaque mot de la phrase
            vocabulaire.add(mot)  # on ajoute le mot au set

    # Transformer en liste ordornné
    return sorted(list(vocabulaire))


def calculer_tf(phrases, vocabulaire):
    """
    Calcule la fréquence des mots (TF) pour chaque phrase.

    Args:
        phrases (list of list of str): liste de phrases tokenisées.
        vocabulaire (list): liste de tous les mots uniques.

    Returns:
        list of dict: pour chaque phrase, un dictionnaire {mot: fréquence}.
                        Exemple : {"mot1": 0.2, "mot2": 0.5, ...}
    """
    tf_list = []  # va contenir un dictionnaire par phrase

    for phrase in phrases:
        tf_phrase = {}
        nb_mots = len(phrase)

        if nb_mots == 0:
            # si la phrase est vide, tout mettre à 0
            for mot in vocabulaire:
                tf_phrase[mot] = 0
            tf_list.append(tf_phrase)
            continue

        compteur = Counter(phrase)  # dictionnaire
        for mot in vocabulaire:
            tf_phrase[mot] = compteur[mot] / nb_mots
        tf_list.append(tf_phrase)

    return tf_list


def calculer_idf(phrases, vocabulaire):
    """
    Calcule l'IDF(Inverse Document Frequency) pour chaque mot du vocabulaire.
    L’IDF mesure à quel point un mot est spécifique ou rare dans le corpus.
    Mot rare = IDF élevé (plus informatif)

    Args:
        phrases (list of list of str): liste de phrases tokenisées.
        vocabulaire (list): liste de tous les mots uniques.

    Returns:
        dict: {mot: valeur IDF}.
    """
    N = len(phrases)  # nb total de phrases
    idf = {}

    for mot in vocabulaire:
        # combien de phrases contiennent ce mot
        nb_phrases_contenant = sum(1 for phrase in phrases if mot in phrase)
        idf[mot] = math.log((1 + N) / (1 + nb_phrases_contenant)) + 1

    return idf


def construire_matrice_tfidf(tf_list, idf, vocabulaire):
    """
    Construit la matrice TF-IDF complète (phrases x vocabulaire).

    Args:
        tf_list (list of dict): liste des fréquences TF par phrase.
        idf (dict): valeurs IDF par mot.
        vocabulaire (list): liste des mots uniques.

    Returns:
        list of list of float: matrice TF-IDF.
    """
    matrice_tfidf = []

    for tf_phrase in tf_list:  # pour chaque phrase
        vecteur = []
        for mot in vocabulaire:  # pour chaque mot du vocabulaire
            valeur = tf_phrase[mot] * idf[mot]  # TF * IDF
            vecteur.append(valeur)
        matrice_tfidf.append(vecteur)

    return matrice_tfidf


def construire_tfidf(phrases):
    """
    Construit le vocabulaire, calcule TF, IDF et renvoie la matrice TF-IDF.

    Args:
        phrases (list of list of str): liste des phrases tokenisées.

    Returns:
        tuple: (matrice TF-IDF, vocabulaire).
    """
    vocabulaire = construire_vocabulaire(phrases)
    tf_list = calculer_tf(phrases, vocabulaire)
    idf = calculer_idf(phrases, vocabulaire)
    matrice = construire_matrice_tfidf(tf_list, idf, vocabulaire)

    return matrice, vocabulaire
