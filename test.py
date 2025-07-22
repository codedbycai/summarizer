from utils import lire_fichier,lire_fichiers
from preprocessing import nettoyer_segmenter

texte_brute = lire_fichier("exemples/article1.txt")
texte_nettoye = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
print(texte_nettoye)

# texte_brute = lire_fichiers("exemples/corpus")
# texte_nettoye = nettoyer_segmenter(texte_brute, langue="french")      #'french' ou 'english'
# print(texte_nettoye)

# for i,phrase in enumerate(texte_nettoye,1):
#     print(f"{i}. {phrase}")
