import networkx as nx
from utils import cosine_similarity

def matrix_similarity(tfidf_matrix, seuil=0.1):
    G = nx.Graph()
    n = len(tfidf_matrix)
    for i in range(n):
        G.add_node(i)
        for j in range(i+1, n):
            s = cosine_similarity(tfidf_matrix[i], tfidf_matrix[j])
            if s > seuil:
                G.add_edge(i, j, weight=s)
    
    return G