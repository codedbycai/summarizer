import os                                                               # module système

def lire_fichier(path):
    try:
        with open(path, "r", encoding="utf_8") as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier} n'existe pas.")
        return ""

def lire_fichiers(dossier):
    textes = []
    for nom_fichier in os.listdir(dossier):
        chemin = os.path.join(dossier, nom_fichier)                     # chemin complet
        if os.path.isfile(chemin) and nom_fichier.endswith(".txt"):     # verification
            with open(chemin, "r", encoding="utf_8") as fichier:
                textes.append(fichier.read())
    return "\n".join(textes)