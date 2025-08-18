from utils import lire_fichier,lire_fichiers
from preprocessing import nettoyer_segmenter
from tfidf import construire_tfidf

texte_brute = lire_fichier("exemples/article1.txt")
list_phrases = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
print(list_phrases)

# texte_brute = lire_fichiers("exemples/corpus")
# texte_nettoye = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
# print(texte_nettoye)

# for i,phrase in enumerate(texte_nettoye,1):
#     print(f"{i}. {phrase}")

#tfidf 
matrice, vocab = construire_tfidf(list_phrases)
print("Vocabulaire:", vocab)
print("\nMatrice TF-IDF:" ,matrice)

