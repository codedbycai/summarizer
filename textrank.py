# textrank.py
import numpy as np

def textrank(adj_matrix, damping=0.85, max_iter=100, tol=1e-6):
    
    n = len(adj_matrix)
    
    if n == 0:
        return []

    # convertir en numpy array
    A = np.array(adj_matrix, dtype=float)

    # cas sans arêtes
    if np.all(A == 0):
        return [1.0 / n] * n
    
    # normalisation : axis=1 (lignes), keepdims=True (keep dimension)
    row_sums = A.sum(axis=1, keepdims=True)

    M = np.zeros_like(A)
    for i in range(n):  # pour chaque phrase (ligne)
        if row_sums[i] != 0:  # eviter les divisions par zero
            M[i] = A[i] / row_sums[i]

    # initialisation : score uniforme 1/n
    scores = np.ones(n) / n


    for iter in range(max_iter):
        new_scores = np.zeros(n)
        
        for i in range(n):
            # random page is 1 - d
            new_scores[i] = (1 - damping) / n
            
            # contribution des voisins (redistribution des scores)
            for j in range(n):
                new_scores[i] += damping * M[j, i] * scores[j]
        
        # Vérifier convergence (écart entre anciens et nouveaux scores)
        diff = np.sum(np.abs(new_scores - scores))
        if diff < tol:
            
            break

        scores = new_scores

    # Normalisation entre 0 et 1
    max_score = max(scores)
    if max_score > 0:
        scores = scores / max_score

    return iter,scores.tolist()
