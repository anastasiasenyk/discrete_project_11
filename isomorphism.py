"""5th function"""
import time
from itertools import permutations


def adjacent_matrix(graph: dict, directed: bool) -> list:
    """
    Creates adjacent matrix of the graph.
    Args:
        graph: dict of vertices
        directed: True is graph is directed, False if not
    Returns:
        list: list of lists, where lists are rows formed by 0 and 1
    """
    if directed:
        empty_vertices = []
        for edges in graph.values():
            for vert in edges:
                if vert not in graph.keys():
                    empty_vertices.append(vert)
        for vert in empty_vertices:
            graph[vert] = []

    array = []
    for vert_1 in graph.keys():
        row = []
        for vert_2 in graph.keys():
            if vert_2 in graph[vert_1]:
                row.append(1)
            else:
                row.append(0)
        array.append(tuple(row))

    return array


def matrix_permutations_comparison(array_1: list, array_2: list) -> bool:
    """
    Finds matrix permutations and checks whether they are similar to another matrix.
    Args:
        array_1: adjacent matrix of first graph
        array_2: adjacent matrix of second graph
    Returns:
        bool: True if the same matrix was found, False if not
    """
    rows_permutations = list(permutations(array_1))
    for rows_variant in rows_permutations:
        columns_permutations = list(permutations(list(zip(*rows_variant))))
        for columns_variant in columns_permutations:
            if columns_variant == array_2:
                return True
    return False


def vertices_check_not_directed(vertice_1: str, vertice_2: str, graph_1: dict, graph_2: dict) -> bool:
    """
    Check whether two vertices have same degree and
    are connected with vertices which have same degrees.
    Args:
        vertice_1: name of first vertice
        vertice_2: name of second vertice to check with
        graph_1: dict of vertices of first graph
        graph_2: dict of vertices of second graph
    Returns:
        bool: True if vertices and their adjacent vertices have the same degree,\
              False if don't
    """
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
    Checks whether not directed graphs are isomorphic.
    Args:
        graph_1: dict of vertices of first graph
        graph_2: dict of vertices of second graph
    Returns:
        bool: True if they are isomorphic, False if they don't.
    """
    # invariant_1: equal number of vertices
    if len(graph_1.keys()) != len(graph_2.keys()):
        return False

    # invariant_2 and 3: equal number of edges and same degree sequence
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

    # # adjacent vertices check
    # all_variants = tuple(permutations(graph_2.keys()))
    # vertices_1 = [vertice for vertice in graph_1.keys()]
    # for variant in all_variants:
    #     for index, vertice_2 in enumerate(variant):
    #         if vertices_check_not_directed(vertices_1[index], vertice_2, graph_1, graph_2) is False:
    #             break
    #         else:
    #             if index == len(variant) - 1:
    #                 return True
    # return False

    # matrix permutations check
    array_1 = adjacent_matrix(graph_1, False)
    array_2 = adjacent_matrix(graph_2, False)
    return matrix_permutations_comparison(array_1, array_2)


def vertices_check_directed(connected_vert_1: list, connected_vert_2: list,
                            deg_graph_1: dict, deg_graph_2: dict) -> bool:
    """
    Check whether two vertices are connected with vertices which have same
    in-degrees and out-degrees.
    Args:
        connected_vert_1: list of adjacent vertices of first vertice
        connected_vert_2: list of adjacent vertices of second vertice
        deg_graph_1: dict, where keys are vertices of first graph and 
            values are lists, where first element is out-degree, second - in-degree
        deg_graph_2: dict, where keys are vertices of second graph and 
            values are lists, where first element is out-degree, second - in-degree
    Returns:
        bool: True if adjacent vertices of two given vertices have same
            in-degrees and out-degrees, False if don't
    """
    deg_connected_1 = {}
    deg_connected_2 = {}

    for vert in connected_vert_1:
        if tuple(deg_graph_1[vert]) not in deg_connected_1.keys():
            deg_connected_1[tuple(deg_graph_1[vert])] = 1
        else:
            deg_connected_1[tuple(deg_graph_1[vert])] += 1

    for vert in connected_vert_2:
        if tuple(deg_graph_2[vert]) not in deg_connected_2.keys():
            deg_connected_2[tuple(deg_graph_2[vert])] = 1
        else:
            deg_connected_2[tuple(deg_graph_2[vert])] += 1

    if deg_connected_1 == deg_connected_2:
        return True
    else:
        return False


def isomorphism_of_directed_graphs(graph_1: dict, graph_2: dict,) -> bool:
    """
    Checks whether directed graphs are isomorphic.
    Args:
        graph_1: dict of vertices of first graph
        graph_2: dict of vertices of second graph
    Returns:
        bool: True if they are isomorphic, False if they don't.
    """
    # invariant_1 and 2: equal number of vertices, in-degrees and out-degrees sequence
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

    # equal number of vertices
    if len(degs_graph_1.keys()) != len(degs_graph_2.keys()):
        return False

    # in-degrees and out-degrees sequence
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

    # adjacent vertices check
    # all_variants = tuple(permutations(degs_graph_2.keys()))
    # vertices_1 = [vertice for vertice in degs_graph_1]
    
    # for variant in all_variants:
    #     for index, vertice_2 in enumerate(variant):
    #         vertice_1 = vertices_1[index]
    #         if degs_graph_1[vertice_1] != degs_graph_2[vertice_2]:
    #             break
    #         if not vertices_check_directed(vert_connected_1[vertice_1],
    #                                        vert_connected_2[vertice_2], degs_graph_1, degs_graph_2):
    #             break
    #         if index == len(variant) - 1:
    #             return True
    # return False

    # matrix permutations check
    array_1 = adjacent_matrix(graph_1, True)
    array_2 = adjacent_matrix(graph_2, True)
    return matrix_permutations_comparison(array_1, array_2)


start = time.time()
# print(isomorphism_of_directed_graphs({'a': ['c', 'd'], 'c': [
#       'b'], 'd': ['b']}, {'a': ['b'], 'b': ['d'], 'c': ['a', 'd']}, {'a': ['c', 'd'], 'c': ['a', 'b'], 'd': ['a', 'b'], 'b': ['c', 'd']}, {'a': ['b', 'c'], 'c': ['a', 'd'], 'd': ['c', 'b'], 'b': ['a', 'd']}))
# print(isomorphism_of_not_directed_graphs({'1': ['2', '5', '4'], '2': ['1', '5', '3'], '3': [
#       '2', '6', '4'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['5', '3', '4']}, {'a': ['b','f','d'],'b': ['a','e','c'],'c': ['b','f','d'],'d': ['a','c','e'],'e': ['b','f','d'],'f': ['e','c','a']}))
print(isomorphism_of_not_directed_graphs({'4': ['3', '6', '2', '1'], '3': ['4', '7', '6', '1', '5', '2'], '7': ['3', '2', '6'], '2': ['7', '1', '4', '5', '6', '3'], '6': ['4', '5', '3', '7', '2'], '5': ['6', '3', '2', '1'], '1': [
      '2', '3', '4', '5']}, {'2': ['3', '4', '5', '1', '3', '4', '6'], '3': ['2', '5', '1', '2', '4', '6'], '6': ['1', '4', '3', '2'], '1': ['6', '2', '3', '5', '4'], '4': ['2', '6', '5', '3', '2', '1'], '5': ['2', '4', '3', '1']}))
finish = time.time()
print(finish-start)
