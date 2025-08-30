import argparse
import os
import math

from utils import lire_fichier,lire_fichiers,mesurer_temps
from preprocessing import nettoyer_segmenter
from tfidf import construire_tfidf
from graph import matrix_similarity
from textrank import textrank


def charger_sources(inputs):
    textes = []
    nb_fichiers = 0
    print("Fichier :")
    for chemin in inputs:
        if os.path.isdir(chemin):
            contenu, n = lire_fichiers(chemin)
            for nom_fichier in os.listdir(chemin):
                if nom_fichier.endswith(".txt"):
                    print("-",nom_fichier)
            textes.append(contenu)
            nb_fichiers += n
        elif os.path.isfile(chemin):
            textes.append(lire_fichier(chemin))
            print("-",chemin)
            nb_fichiers += 1
        else:
            print(f"[ERREUR] Chemin invalide '{chemin}'")
    return "\n".join(textes), nb_fichiers

def selection_phrases(phrases, scores, ratio):
    n = len(phrases)
    top = math.ceil(ratio * n)  # nombre de phrases à garder  ⌈ P × N ⌉

    # associer phrase index + score
    phrases_scores = []
    for i in range(n):
        phrase_texte = phrases[i]  # reconstruire en texte
        phrases_scores.append((i, scores[i], phrase_texte))
         
    # trier score décroissant
    phrases_scores.sort(key=lambda x: x[1], reverse=True)

    # garder les meilleures
    top_phrases = phrases_scores[:top]

    # remettre dans l’ordre du texte original (index croissant)
    top_phrases.sort(key=lambda x: x[0])

    # for i, phrase in enumerate(top_phrases, start=1):
    #     print(f"{i}. {phrase}")
    # Retourner seulement le texte des phrases
    return [p[2] for p in top_phrases]
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",nargs="+",required=True)
    parser.add_argument("--ratio",type=float,required=True)
    parser.add_argument("--mode",choices=["french","english"],required=True)
    parser.add_argument("--output",type=str,default=None)
    args = parser.parse_args()

    texte_brut,nb_fichiers = charger_sources(args.input)

    if nb_fichiers == 0:
        print(">> Aucun fichier valide trouvé.")
        return
    
    if not (0.05 <= args.ratio <= 0.5):
        print("[ATTENTION] Le ratio doit être compris entre 0.05 et 0.5")
        return
    
    phrases_original, phrases_token = nettoyer_segmenter(texte_brut, langue=args.mode)
    # print(phrases_original)

    (matrice, vocab),duree_tfidf = mesurer_temps(construire_tfidf,phrases_token)
    (G, nb_nodes, nb_edges), duree_graph = mesurer_temps(matrix_similarity,matrice, 0.1)
    
    (iter, scores), duree_textrank = mesurer_temps(textrank,G)
    if iter >= 100:  # max_iter défini dans textrank
        return
    
    resume = selection_phrases(phrases_original,scores,args.ratio)

    # Affichage
    print(f"Lecture de {nb_fichiers} fichiers…")
    print(f"Nombre total de phrases : {len(phrases_original)} ; termes uniques : {len(vocab)}.\n")
    print(f"Construction de la matrice TF-IDF ({len(phrases_original)} × {len(vocab)})… temps écoulé : {duree_tfidf:.3f} s.")
    print(f"Construction du graphe de similarité… {nb_nodes} nœuds, {nb_edges} arêtes… temps écoulé : {duree_graph:.3f} s.")
    print(f"TextRank – itération 1 à 100 (convergence après {iter} itérations, damping=0.85)… temps écoulé : {duree_textrank:.3f} s.")
    print(f"Temps d’exécution total : {duree_tfidf + duree_graph + duree_textrank:.3f} s.\n")
    print(f"Sélection des {len(resume)} phrases pour le résumé (ratio={args.ratio}).")

    # Emplacement du fichier de sortie ou, si --output omis, afficher le résumé dans la console.
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(resume))
        print(f"Résumé enregistré dans {args.output}")
    else:
        print("\nRésumé généré :\n")
        print("\n".join(resume))

if __name__ == "__main__":
    main()

"""
    python summarizer.py --input exemples/article1.txt exemples/corpus/texte1.txt \
                     --ratio 0.2 \
                     --mode french \
                     --output résumé.txt
    python summarizer.py --input exemples/article1.txt \
                     --ratio 0.2 \
                     --mode french \
                     --output résumé.txt
"""