"""Isomorphism check"""


def read_data(path_to_file: str) -> tuple:
    """
    create a dictionary with graph vertices
    Args:
        path_to_file: path to csv file
    Returns:
        graph_dict: tuple of dict with vertices
    """
    file = pd.read_csv(path_to_file)

    first_elem = file.columns[0].split(' ')
    graph_dict_no = {first_elem[0]: [first_elem[1]],
                     first_elem[1]: [first_elem[0]]}  # graph is not oriented
    graph_dict_o = {first_elem[0]: [first_elem[1]]}  # graph is oriented

    for index, row in file.iterrows():
        row = list(row)[0].split(' ')
        vert1 = row[0]
        vert2 = row[1]

        if vert1 not in graph_dict_o.keys():   # for oriented graph
            graph_dict_o[vert1] = [vert2]
        else:
            graph_dict_o[vert1].append(vert2)

        if vert1 not in graph_dict_no.keys():   # for not oriented graph
            graph_dict_no[vert1] = [vert2]
        else:
            graph_dict_no[vert1].append(vert2)
        if vert2 not in graph_dict_no.keys():
            graph_dict_no[vert2] = [vert1]
        else:
            graph_dict_no[vert2].append(vert1)

    return graph_dict_o, graph_dict_no


def ifconnected(graph_dict) -> bool:
    """
    check whether all vertices are interconnected or not
    Args:
        graph_dict: tuple of dict with vertices

    Returns:
        bool
    >>> ifconnected({'1':["2"], '2':["1"], '3':['4']})
    False
    """
    first_vert = list(graph_dict.keys())[0]
    visited, queue = [first_vert], [first_vert]
    while queue:
        vertex = queue.pop(0)
        if vertex in list(graph_dict.keys()):
            for neighbour in graph_dict[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    for element in list(graph_dict.keys()):
        if element not in visited:
            return False
    return True


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

    # adjacent vertices check
    all_variants = tuple(permutations(graph_2.keys()))
    vertices_1 = [vertice for vertice in graph_1.keys()]
    good_variant = 0
    for variant in all_variants:
        if good_variant == 0:
            for index, vertice_2 in enumerate(variant):
                if vertices_check_not_directed(vertices_1[index], vertice_2, graph_1, graph_2) is False:
                    break
                else:
                    if index == len(variant) - 1:
                        good_variant += 1
    if good_variant == 0:
        return False

    # matrix permutations check
    array_1 = adjacent_matrix(graph_1, False)
    array_2 = adjacent_matrix(graph_2, False)
    return matrix_permutations_comparison(array_1, array_2)


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

    # 1: equal number of vertices
    if len(degs_graph_1.keys()) != len(degs_graph_2.keys()):
        return False

    # 2: in-degrees and out-degrees sequence
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

    # matrix permutations check
    array_1 = adjacent_matrix(graph_1, True)
    array_2 = adjacent_matrix(graph_2, True)
    return matrix_permutations_comparison(array_1, array_2)


if __name__ == '__main__':
    import pandas as pd
    from itertools import permutations
    import os.path
    path_file_1 = 'graph1.csv'  # path to our csv file
    path_file_2 = 'graph2.csv'

    #  read information from csv
    if os.path.exists(path_file_1) and os.path.exists(path_file_2):
        graph1 = read_data(path_file_1)
        graph2 = read_data(path_file_2)
        not_oriented_graph_1 = graph1[1]
        oriented_graph_1 = graph1[0]
        not_oriented_graph_2 = graph2[1]
        oriented_graph_2 = graph2[0]

        # check if all verticals are connected
        if not ifconnected(not_oriented_graph_1) or not ifconnected(not_oriented_graph_2):
            print('the graph is not connected')
        else:
            print(
                f'Graphs are isomorphic: {isomorphism_of_not_directed_graphs(not_oriented_graph_1, not_oriented_graph_2)}')
    else:
        print("file doesn't exist")
