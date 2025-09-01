from graph import matrix_similarity


def test_graph():
    # 2 phrases identiques = similarité max
    tfidf = [[1, 0], [1, 0]]
    sim_matrix, nodes, edges = matrix_similarity(tfidf, seuil=0.1)

    assert nodes == 2
    assert edges >= 1  # au moins 1 arete car les phrases sont identiques
