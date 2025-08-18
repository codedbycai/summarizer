import math
import pytest

from tfidf import (
    construire_vocabulaire,
    calculer_tf,
    calculer_idf,
    construire_matrice_tfidf,
    construire_tfidf,
)

def test_phrase_vide():
    assert construire_vocabulaire([]) == []

def test_vocabulaire_simple():
    phrases = [["python", "projet"], ["test", "unitaire"]]
    vocab = construire_vocabulaire(phrases)
    # Vérifie que tous les mots uniques sont là
    assert set(vocab) == {"python", "projet", "test", "unitaire"}

def test_tf_simple():
    phrases = [["python", "python", "projet"]]
    vocab = construire_vocabulaire(phrases)
    tf_list = calculer_tf(phrases, vocab)

    # "python" apparaît 2 fois sur 3 → TF = 2/3
    assert abs(tf_list[0]["python"] - (2/3)) < 1e-9
    # "projet" apparaît 1 fois sur 3 → TF = 1/3
    assert abs(tf_list[0]["projet"] - (1/3)) < 1e-9

def test_idf_presence():
    phrases = [["a"], ["a", "b"]]
    vocab = construire_vocabulaire(phrases)
    idf = calculer_idf(phrases, vocab)
    assert idf["a"] <= idf["b"]  # "a" est plus fréquent que "b"

def test_matrice_tfidf():
    phrases = [
        ["python", "code", "projet"],
        ["python", "test", "unitaire"]
    ]
    vocab = construire_vocabulaire(phrases)
    tf_list = calculer_tf(phrases, vocab)
    idf = calculer_idf(phrases, vocab)
    
    matrice = construire_matrice_tfidf(tf_list, idf, vocab)
    assert len(matrice) == 2
    assert len(matrice[0]) == len(vocab)



