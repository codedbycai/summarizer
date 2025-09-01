import numpy as np
from textrank import textrank


def test_textrank():
    A = np.array([[0, 1], [1, 0]])  # 2 phrases reliées
    iterations, scores = textrank(A)
    assert len(scores) == 2


def test_textrank_empty():
    # graphe vide
    iterations, scores = textrank([])
    assert iterations == 0
    assert scores == []
