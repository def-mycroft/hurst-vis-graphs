"""Automated tests for visibility graph using pytest"""
from . import build_visibility_graph as sc


def test_create_edges():
    """Applies unit test"""
    # expected set of edges based on the input
    edges_expected = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (6, 7), (7, 8), (8, 9), (8, 10), (8, 11), (8, 12), (9, 10), (9, 11), (10, 11), (11, 12), (12, 13), (12, 14), (12, 15), (12, 16), (13, 14), (13, 15), (14, 15), (15, 16), (16, 17), (16, 18), (16, 19), (17, 18), (17, 19), (18, 19)]

    # x and y args for example from the Lacasca paper 
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    y = [0.87, 0.49, 0.36, 0.83, 0.87, 0.49, 0.36, 0.83, 0.87, 0.49, 0.36, 0.83, 0.87, 0.49, 0.36, 0.83, 0.87, 0.49, 0.36, 0.83]

    msg = 'Calculated edges should match test case'
    f = lambda l: list(sorted(l))
    assert f(sc.create_edges(x,y)) == f(edges_expected), msg
