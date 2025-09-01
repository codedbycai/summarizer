import networkx as nx
import numpy as np


def matrix_similarity(tfidf_matrix, seuil=0.1):
    # Convertir en matrice numpy
    tfidf_array = np.array(tfidf_matrix, dtype=float)

    # Normaliser les lignes (chaque phrase en vecteur unitaire)
    phrase_norms = np.linalg.norm(tfidf_array, axis=1, keepdims=True)

    # Eviter diviser par zéro avec NumPy Boolean Indexing
    phrase_norms[phrase_norms == 0] = 1e-9
    normalized_tfidf = tfidf_array / phrase_norms

    # Calculer la matrice de similarité (produit scalaire de tous les couples de phrases)
    similarity_matrix = np.dot(normalized_tfidf, normalized_tfidf.T)

    # Appliquer un seuil : ignorer les similarités trop faibles
    similarity_matrix[similarity_matrix < seuil] = 0.0

    # Construction du graphe
    graph = nx.from_numpy_array(similarity_matrix)

    nb_nodes = graph.number_of_nodes()
    nb_edges = graph.number_of_edges()

    return similarity_matrix, nb_nodes, nb_edges
