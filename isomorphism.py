"""5th function"""
import time
from itertools import permutations


def good_vertices_check(vertice_1: str, vertice_2: str, graph_1: dict, graph_2: dict) -> bool:
    if len(graph_1[vertice_1]) != len(graph_2[vertice_2]):
        return False
    vertice_1_deg = {}
    vertice_2_deg = {}
    for vertice in graph_1[vertice_1]:
        deg = len(graph_1[vertice])
        if deg not in vertice_1_deg.keys():
            vertice_1_deg[deg] = 1
        else:
            vertice_1_deg[deg] += 1
    for vertice in graph_2[vertice_2]:
        deg = len(graph_2[vertice])
        if deg not in vertice_2_deg.keys():
            vertice_2_deg[deg] = 1
        else:
            vertice_2_deg[deg] += 1
    if vertice_1_deg == vertice_2_deg:
        return True
    else:
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
    deg_graph_1 = {}
    deg_graph_2 = {}

    for vertice in graph_1.values():
        deg = len(vertice)
        edges_1 += deg
        if deg not in deg_graph_1.keys():
            deg_graph_1[deg] = 1
        else:
            deg_graph_1[deg] += 1

    for vertice in graph_2.values():
        deg = len(vertice)
        edges_2 += deg
        if deg not in deg_graph_2.keys():
            deg_graph_2[deg] = 1
        else:
            deg_graph_2[deg] += 1

    if edges_1 != edges_2 or deg_graph_1 != deg_graph_2:
        return False

    # граф все-таки ізоморфний?
    #!!!спочатку брати вершину з найбільшим степенем!!!
    
    all_variants = tuple(permutations(graph_2.keys()))
    vertices_1 = [vertice for vertice in graph_1.keys()]
    for variant in all_variants:
        for index, vertice_2 in enumerate(variant):
            if good_vertices_check(vertices_1[index], vertice_2, graph_1, graph_2) == False:
                break
            else:
                if index == len(variant) - 1:
                    return True
    return False
    




print(time.time())
print(isomorphism_of_graphs({'4': ['3', '2'], '3': ['1', '4'], '1': ['2', '3'], '2': [
      '1', '4']}, {'1': ['3', '4'], '3': ['1', '2'], '4': ['1', '2'], '2': ['3', '4']}))
print(time.time())
