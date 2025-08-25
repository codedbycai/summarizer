from numpy import dot
from numpy.linalg import norm
import networkx as nx

def cosine(u, v):
    return float(dot(u, v) / (norm(u) * norm(v)))

def similarity_matrix(tfidf_matrix, seuil=0.1):
    G = nx.Graph()
    n = len(tfidf_matrix)
    for i in range(n):
        G.add_node(i)
        for j in range(i+1, n):
            s = cosine(tfidf_matrix[i], tfidf_matrix[j])
            if s >= seuil:
                G.add_edge(i, j, weight=s)
    
    return G