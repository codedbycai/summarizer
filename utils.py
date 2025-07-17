
def lire_fichier(path):
    try:
        with open(path, "r", encoding="utf_8") as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier} n'existe pas.")
        return ""