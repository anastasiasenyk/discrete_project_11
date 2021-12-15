"""5th function"""
import time


def good_vertices(vertice_1: str, vertice_2: str, graph_1: dict, graph_2: dict) -> bool:
    if len(graph_1[vertice_1]) != len(graph_2[vertice_2]):
        return False


def isomorphism_of_graphs(graph_1: dict, graph_2: dict) -> bool:
    """
    Checks whether graphs are isomorphic.
    Returns True if they are, False if they don't.
    """
    # інваріант_1: кількість вершин
    if len(graph_1.keys()) != len(graph_2.keys()):
        return False

    # інваріант_2 і 3: кількість ребер і кількість вершин конкретного степеня
    edges_1 = 0
    edges_2 = 0
    deg_dict_1 = {} 
    deg_dict_2 = {}

    for vertice in graph_1.values():
        deg = len(vertice)
        edges_1 += deg
        if deg not in deg_dict_1.keys():
            deg_dict_1[deg] = 1
        else:
            deg_dict_1[deg] += 1

    for vertice in graph_2.values():
        deg = len(vertice)
        edges_2 += deg
        if deg not in deg_dict_2.keys():
            deg_dict_2[deg] = 1
        else:
            deg_dict_2[deg] += 1

    if edges_1 != edges_2 or deg_dict_1 != deg_dict_2:
        return False


print(isomorphism_of_graphs({'4': ['3', '2'], '3': ['1', '4'], '1': ['2', '3'], '2': [
      '1', '4']}, {'1': ['3', '4'], '3': ['1', '2'], '4': ['1', '2'], '2': ['3', '4']}))
