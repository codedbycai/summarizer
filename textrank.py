# textrank.py
import numpy as np


def textrank(adj_matrix, damping=0.85, max_iter=100, tol=1e-6):
    """
    Algorithme TextRank (PageRank) pour attribuer un score d’importance à chaque phrase.

    Cet algorithme donne un score d’importance à chaque phrase d’un texte
    en fonction des similarités avec les autres phrases.
    Plus une phrase est connectée (et connectée à des phrases déjà importantes),
    plus son score augmente.

    Args:
        adj_matrix (list of list of float | np.ndarray):
            Matrice d’adjacence pondérée représentant le graphe de similarité.
        damping (float, optionnel): facteur d’amortissement (probabilité de suivre un lien), par défaut 0.85.
        max_iter (int, optionnel): nombre maximal d’itérations, par défaut 100.
        tol (float, optionnel): tolérance de convergence (différence entre deux vecteurs de scores), par défaut 1e-6.

    Returns:
        tuple:
            - int: nombre d’itérations effectuées.
            - list of float: scores normalisés (0–1) pour chaque phrase.
    """
    n = len(adj_matrix)

    if n == 0:
        return 0, []

    # convertir en numpy array
    A = np.array(adj_matrix, dtype=float)

    # cas sans arêtes
    if np.all(A == 0):
        return 1, [1.0 / n] * n

    # normalisation : axis=1 (lignes), keepdims=True (keep dimension)
    row_sums = A.sum(axis=1, keepdims=True)

    M = np.zeros_like(A)
    for i in range(n):  # pour chaque phrase (ligne)
        if row_sums[i] != 0:  # eviter les divisions par zero
            M[i] = A[i] / row_sums[i]

    # initialisation : score uniforme 1/n
    scores = np.ones(n) / n

    # Ancienne version
    # for iter in range(max_iter):
    #     new_scores = np.zeros(n)

    #     for i in range(n):
    #         # random page is 1 - d
    #         new_scores[i] = (1 - damping) / n

    #         # contribution des voisins (redistribution des scores)
    #         for j in range(n):
    #             new_scores[i] += damping * M[j, i] * scores[j]

    # Version NumPy
    for iter in range(max_iter):
        new_scores = (1 - damping) / n + damping * M.T.dot(scores)

        # Vérifier convergence (écart entre anciens et nouveaux scores)
        diff = np.sum(np.abs(new_scores - scores))
        if diff < tol:
            # normalise
            return iter + 1, (new_scores / new_scores.max()).tolist()

        scores = new_scores

    # si on sort de la boucle = pas de convergence
    print(
        f"[ATTENTION] PageRank n’a pas convergé après {max_iter} itérations.\n"
        f"                Essayez un damping factor plus bas ou acceptez ce résultat."
    )

    return max_iter, (new_scores / new_scores.max()).tolist()
