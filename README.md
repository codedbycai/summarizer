## Application de Résumé Automatique de Textes (Extractive Summarization)


## 1. Présentation du projet

Ce projet implémente une **application de résumé automatique extractif**.  
Le but est de partir d’un document (article, rapport, etc.) et d’obtenir un résumé qui garde seulement les **phrases essentielles**.

Pour cela, on suit plusieurs étapes :

* On **nettoie** le texte et on le **découpe en phrases**.

* On **représente** chaque phrase avec un calcul appelé **TF-IDF** (met en avant les mots importants).

* On **relie les phrases** entre elles grâce à un **graphe** basé sur leur similarité.

* On utilise l’algorithme **TextRank** (adaptation de PageRank) pour donner un **score d’importance** à chaque phrase.

* Enfin, on **choisit les meilleures phrases** et on les remet dans l’ordre d’origine pour former le résumé.

C’est donc une méthode extractive : on ne réécrit pas le texte, on extrait les phrases les plus utiles.

---

## 2. Installation

a. **Cloner le dépôt et créer un environnement virtuel**
```bash
git clone https://github.com/codedbycai/summarizer.git
cd project-summarizer
python3 -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
```

b. **Télécharger les ressources NLTK**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```
---

## 3. Usage

 a. **Exemples de commandes CLI**

```bash
python summarizer.py \
    --input exemples/article1.txt \
    --ratio 0.2 \
    --mode french \
    --output exemples/article1_summary.txt
```

```bash
python summarizer.py \
    --input exemples/corpus \
    --ratio 0.5 \
    --mode english
```

```bash
python summarizer.py --input exemples/corpus --ratio 0.5 --mode french 
```
b. **Description des arguments**
* **--input** : un ou plusieurs fichiers `.txt` ou dossiers contenant des `.txt`
* **--ratio** : pourcentage de phrases à garder (entre `0.05` et `0.5`)
* **--mode** : langue du texte (`french` ou `english`)
* **--output** : chemin du fichier de sortie (sinon affiche dans la console)

---

## 4. Architecture du code

a. **Dépendance (modules)**
```
project-summarizer/
├── preprocessing.py   # nettoyage et segmentation
├── tfidf.py           # calcul TF, IDF, matrice TF-IDF
├── graph.py           # graphe de similarité
├── textrank.py        # scoring TextRank
├── summarizer.py      # interface CLI (pipeline complet)
├── utils.py           # fonctions utilitaires (lecture fichiers, timing, similarité)
├── requirements.txt   # dépendances Python
├── exemples/          # exemples d’entrée/sortie
└── tests/             # tests unitaires (pytest)
```
b. **Schéma simplifié**
```
  Texte brut        (.txt)
      ↓
preprocessing.py    (nettoyage,segmentation,tokenisation)
      ↓
   tfidf.py         (calcul TF, IDF, matrice TF-IDF)
      ↓
   graph.py         (graphe de similarité)
      ↓
  textrank.py       (scores  des phrases PageRank)
      ↓
 summarizer.py      (sélection des phrases → résumé final)
```
---

## 5. Exemple concret

```bash
python summarizer.py \
    --input exemples/article1.txt \
    --ratio 0.2 \
    --mode french \
    --output exemples/article1_summary.txt

    ...
    à terminer
    ...
```

---

## 6. Test unitaires
* **Ligne de commande** :
```bash
pytest --maxfail=1 --disable-warnings -q
```
**Explication des tests fournis et de l’ajout possible de nouveaux tests.
(à faire)**

---

## 7. Historique Git

**Le projet a été développé en suivant un workflow basé sur plusieurs branches** :

* **main** : branche stable contenant les versions validées.
* **feature/...** : une branche par fonctionnalité.
    * `feature/preprocessing`
     * `feature/tfidf`
     * `feature/graph`
     * `feature/textrank`
     * `feature/cli`

**Messages de commit** :
* **[PREP]** : Prétraitement (nettoyage, segmentation, tokenisation)
* **[TFIDF]** : Calcul TF, IDF et matrice TF-IDF  
* **[GRAPH]** : Construction graphe de similarité
* **[TR]** : Implémentation TextRank
* **[CLI]** : Ajout interface ligne de commande
* **[UTILS]** : Fonctions utilitaires (mesure du temps, lecture fichiers, etc.) 
* **[DOC]** : Rédaction du README.

**Pour consulter tout l’historique des commits et suivre l’avancement du projet** :
* En ligne de commande :

```bash
git log --oneline --decorate --graph
```

* Ou directement sur GitHub :

```
https://github.com/codedbycai/summarizer/commits/
```