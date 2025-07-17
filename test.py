from utils import lire_fichier
from preprocessing import nettoyer_segmenter

texte_brute = lire_fichier("exemples/article1.txt")
texte_nettoye = nettoyer_segmenter(texte_brute, langue="english")      #'french' ou 'english'

for i,phrase in enumerate(texte_nettoye,1):
    print(f"{i}. {phrase}")
