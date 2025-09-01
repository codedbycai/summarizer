import os  # module système
import time

from numpy import dot
from numpy.linalg import norm


def cosine_similarity(u, v):
    """Calcule la similarité cosinus entre deux vecteurs."""
    norm_u = norm(u)
    norm_v = norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0  # pas de similarité si l’un des vecteurs est nul
    return float(dot(u, v) / (norm_u * norm_v))


def lire_fichier(path):
    """Lit le contenu d'un fichier .txt et le retourne, ou une chaîne vide si introuvable."""
    try:
        with open(path, "r", encoding="utf_8") as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier} n'existe pas.")
        return ""


def lire_fichiers(dossier):
    """Lit tous les fichiers .txt d’un dossier et concatène leur contenu."""
    textes = []
    nb_fichiers = 0
    for nom_fichier in os.listdir(dossier):
        chemin = os.path.join(dossier, nom_fichier)  # chemin complet
        if os.path.isfile(chemin) and nom_fichier.endswith(".txt"):  # verification
            nb_fichiers += 1
            with open(chemin, "r", encoding="utf_8") as fichier:
                textes.append(fichier.read())
    return "\n".join(textes), nb_fichiers


def mesurer_temps(func, *args, **kwargs):
    """
    Lance une fonction et mesure son temps.

    Args:
        func: la fonction à appeler.
        *args: les valeurs données à la fonction.
        **kwargs: les paramètres nommés passés à la fonction.

    Returns:
        tuple[Any, float]: (résultat de la fonction, durée en secondes).
    """
    start = time.time()
    result = func(*args, **kwargs)  # kwargs (ex: tol=1e-6 pour TextRank)
    end = time.time()
    duree = end - start

    return result, duree
