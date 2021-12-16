"""5th function"""
import time
from itertools import permutations


def vertices_check_not_directed(vertice_1: str, vertice_2: str, graph_1: dict, graph_2: dict) -> bool:
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


def isomorphism_of_not_directed_graphs(graph_1: dict, graph_2: dict) -> bool:
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

    # графи все-таки ізоморфні?
    #!!!спочатку брати вершину з найбільшим степенем!!!

    all_variants = tuple(permutations(graph_2.keys()))
    vertices_1 = [vertice for vertice in graph_1.keys()]
    for variant in all_variants:
        for index, vertice_2 in enumerate(variant):
            if vertices_check_not_directed(vertices_1[index], vertice_2, graph_1, graph_2) is False:
                break
            else:
                if index == len(variant) - 1:
                    return True
    return False


def isomorphism_of_directed_graphs(graph_1: dict, graph_2: dict) -> bool:
    """
    Checks whether graphs are isomorphic.
    Returns True if they are, False if they don't.
    """
    # інваріанти: кількість вершин, степені входу і виходу
    degs_graph_1 = {}
    degs_graph_2 = {}

    for vertice, edges in graph_1.items():
        if vertice not in degs_graph_1.keys():
            degs_graph_1[vertice] = [0, 0]
        degs_graph_1[vertice][0] = len(edges)
        for edge in edges:
            if edge not in degs_graph_1.keys():
                degs_graph_1[edge] = [0, 0]
            degs_graph_1[edge][1] += 1

    for vertice, edges in graph_2.items():
        if vertice not in degs_graph_2.keys():
            degs_graph_2[vertice] = [0, 0]
        degs_graph_2[vertice][0] = len(edges)
        for edge in edges:
            if edge not in degs_graph_2.keys():
                degs_graph_2[edge] = [0, 0]
            degs_graph_2[edge][1] += 1

    # кількість вершин
    if len(degs_graph_1.keys()) != len(degs_graph_2.keys()):
        return False

    # степені входу, виходу
    degs_check = {}
    for degs in degs_graph_1.values():
        if tuple(degs) not in degs_check.keys():
            degs_check[tuple(degs)] = 1
        else:
            degs_check[tuple(degs)] += 1

    for degs in degs_graph_2.values():
        if tuple(degs) not in degs_check.keys():
            return False
        else:
            degs_check[tuple(degs)] -= 1

    for vertices_number in degs_check.values():
        if vertices_number != 0:
            return False

    # графи все-таки ізоморфні?
    #!!!спочатку брати вершину з найбільшим степенем!!!
    all_variants = tuple(permutations(degs_graph_2.keys()))
    vertices_1 = [vertice for vertice in degs_graph_1.keys()]
    for variant in all_variants:
        for index, vertice_2 in enumerate(variant):
            if degs_graph_1[vertices_1[index]] != degs_graph_2[vertice_2]:
                break
            else:
                if index == len(variant) - 1:
                    return True
    return False


start = time.time()
print(isomorphism_of_directed_graphs({'1': ['3', '4'], '2': [
      '3'], '4': ['2']}, {'1': ['3', '4'], '2': ['3'], '4': ['2']}))
# print(isomorphism_of_not_directed_graphs({'a': ['b'], 'b': ['a', 'c'], 'c': ['b', 'd', 'g'], 'g': ['c'], 'd': ['e', 'c'], 'e': ['d', 'f', 'h'], 'h': [
#       'e'], 'f': ['e']}, {'a': ['b'], 'b': ['a', 'c', 'g'], 'c': ['b', 'd'], 'g': ['b'], 'd': ['e', 'c'], 'e': ['d', 'f', 'h'], 'h': ['e'], 'f': ['e']}))
finish = time.time()
print(finish-start)
