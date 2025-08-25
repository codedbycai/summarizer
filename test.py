from utils import lire_fichier,lire_fichiers
from preprocessing import nettoyer_segmenter
from tfidf import construire_tfidf
from graph import similarity_matrix
from textrank import textrank
import networkx as nx

texte_brute = lire_fichier("exemples/article1.txt")
list_phrases = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
print(list_phrases)

# texte_brute = lire_fichiers("exemples/corpus")
# texte_nettoye = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
# print(texte_nettoye)

# for i,phrase in enumerate(texte_nettoye,1):
#     print(f"{i}. {phrase}")

#tfidf.py
matrice, vocab = construire_tfidf(list_phrases)
# print("Vocabulaire:", vocab)
# print("\nMatrice TF-IDF:" ,matrice)

#graph.py
G = similarity_matrix(matrice, seuil=0.01)
# print("Nœuds du graphe :", G.nodes())
# print("Arêtes du graphe :", G.edges())
# print("Arêtes du graphe avec poids :", G.edges(data=True))

# conversion graphe -> matrice d'adjacence
A = nx.to_numpy_array(G, weight="weight")

#textrank.py
scores = textrank(A)
print("Scores finaux:", scores)