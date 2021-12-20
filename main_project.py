"""task 7 group 11"""
from typing import Optional


def read_data(path_to_file: str) -> Optional[tuple]:
    """
    create a dictionary with graph vertices
    Args:
        path_to_file: path to csv file
    Returns:
        graph_dict: tuple of dict with vertices
    """
    if not os.path.exists(path_to_file):
        return print("file doesn't exist")
    file = pd.read_csv(path_to_file)
    c1 = file.columns[0].split(' ')
    graph_dict_no = {c1[0]: [c1[1]], c1[1]: [c1[0]]}  # graph is not oriented
    graph_dict_o = {c1[0]: [c1[1]]}  # graph is oriented

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


def bipartite(graph_dict: dict) -> bool:
    """
    determine whether our graph is bipartite
    (only for not oriented graphs)
    Args:
        graph_dict: dict of vertices

    Returns:
        bool: whether the graph is bipartite or not
    >>> bipartite({'1': ['6'], '2': ['3'], \
    '3': ['6', '1'], '4': ['5'], '7': ['4'], '5': ['2', '3']})
    True
    >>> bipartite({'1': ['2'], '2': ['3'], '3': ['1']})
    False
    """
    first_vert = list(graph_dict.keys())[0]
    visited, queue = [first_vert], [first_vert]
    first_part, second_part = [first_vert],  []
    while queue:
        vertex = queue.pop(0)
        if vertex in list(graph_dict.keys()):
            for neighbour in graph_dict[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

                if vertex in first_part:
                    if neighbour in first_part:
                        return False
                    else:
                        second_part.append(neighbour)
                else:
                    if neighbour in second_part:
                        return False
                    else:
                        first_part.append(neighbour)
    return True


def is_euler_possible_not_directed(graph_dict: dict) -> bool:
    """
    Checks whether a not directed graph has Eulerian circuit or not
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Returns:
        bool: True if the graph_dict has Eulerian circuit False if not
    >>> is_euler_possible_not_directed({'1': ['2', '3', '4'], '2': ['1', '3'],\
     '3': ['1', '2'], '4': ['1', '5'], '5': ['4']})
    False
    >>> is_euler_possible_not_directed({'1': ['2', '3'], '2': ['1', '3'], '3': ['1', '2']})
    True
    """
    multiplicity = []

    for _, item in graph_dict.items():
        multiplicity.append(len(item))

    for i in range(len(multiplicity)):
        if multiplicity[i] % 2 == 1:
            return False
    return True


def euler_circuit_not_directed(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit in not directed graph
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Retuns:
        list: list of vertices whiсh form Euler circuit
        str: message that graph_dict is not connected
    >>> euler_circuit_not_directed({'1': ['4', '2'], \
    '2': ['1', '3', '6', '5'], \
    '3': ['2','4'], \
    '4': ['1', '3'], \
    '5': ['2', '6'], \
    '6': ['2', '5']})
    ['1', '2', '5', '6', '2', '3', '4', '1']
    """
    if is_euler_possible_not_directed(graph_dict) is False:
        return "Graph has no Eulerial circuit"

    else:
        stack = [list(graph_dict.keys())[0]]
        circuit = []
        while stack:
            curr_vertex = stack[-1]
            if len(graph_dict[curr_vertex]) == 0:
                circuit.append(curr_vertex)
                stack.pop(-1)
            else:
                random_edge = graph_dict[curr_vertex][0]
                graph_dict[curr_vertex].remove(random_edge)
                graph_dict[random_edge].remove(curr_vertex)
                stack.append(random_edge)

        for key in graph_dict:
            if key not in circuit:
                return "Graph is not connected"
    return circuit


def is_euler_possible_directed(graph_dict: dict) -> bool:
    """
    Checks whether a directed graph has Eulerian circuit or not
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Returns:
        bool: True if the graph_dict has Eulerian circuit False if not
    >>> is_euler_possible_directed({'1': ['2'], '2': ['3'], '3': ['1']})
    True
    >>> is_euler_possible_directed({'1': ['2'], '2': ['3'], '3': ['1', '2']})
    False
    """

    for key in graph_dict:
        enter = list(value for value in graph_dict.values()).count([key])
        exit = len(graph_dict[key])

        if enter != exit:
            return False
    return True


def euler_circuit_directed(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit in a directed graph
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Return:
        list: list of vertices whiсh form Euler circuit
        str: message that graph_dict is not connected
    >>> euler_circuit_not_directed({'1': ['4', '2'],\
    '2': ['1', '3', '6', '5'], \
    '3': ['2','4'], \
    '4': ['1', '3'], \
    '5': ['2', '6'], \
    '6': ['2', '5']})
    ['1', '2', '5', '6', '2', '3', '4', '1']
    """
    if is_euler_possible_directed(graph_dict) is False:
        return "Graph has no Eulerial circuit"

    else:
        stack = [list(graph_dict.keys())[0]]
        circuit = []
        while stack:
            curr_vertex = stack[-1]
            if len(graph_dict[curr_vertex]) == 0:
                circuit.append(curr_vertex)
                stack.pop(-1)
            else:
                random_edge = graph_dict[curr_vertex][0]
                graph_dict[curr_vertex].remove(random_edge)
                stack.append(random_edge)

        for key in graph_dict:
            if key not in circuit:
                return "Graph is not connected"
    return circuit


def pre_hamilton(graph: dict, var_bool: bool):
    """function to find create list of visited and path
    Args:
        graph: dictionary where keys are vertices
        var_bool: bool whether graph are oriented
    Returns:
        list: list of vertices which form Hamilton circuit
        str: message that cycle doesn't exist"""
    length = len(list(graph.keys()))
    visited = [list(graph.keys())[0]]
    path = [list(graph.keys())[0]]
    if not var_bool:
        path = hamiltonian_cycle(graph, visited, path, 0, length)
        if isinstance(path, list):
            return path
    else:
        path = hamiltonian_cycle(graph, visited, path, 0, length)
        if isinstance(path, list):
            return path
    return "doesn't exist"


def hamiltonian_cycle(graph: dict, visited: list, path: list, v: int, length: int):
    """
    recursive function
    using backtracking
    Args:
        graph: dictionary where keys are vertices
        visited: list of visited vertexes
        path: cycle
        v: index of element
        length: numbers of element
    Returns:
        list: list of vertices which form Hamilton circuit
    """
    if len(path) == length:
        if path[-1] in graph.keys() and path[0] in graph[path[-1]]:
            path.append(path[0])
            return path
        else:
            return False
    item = list(graph.keys())[v]
    for element in graph[item]:
        if element not in visited:
            visited.append(element)
            path.append(element)
            path_bool = hamiltonian_cycle(graph, visited, path, v + 1, length)
            if isinstance(path_bool, list):
                return path_bool
            visited.pop(-1)
            path.pop(-1)
    return False


if __name__ == '__main__':
    import pandas as pd
    import os.path
    path_file = 'graph.csv'  # path to our csv file
    # path_file = 'hamiltonian_20_151_try1.csv'

    #  read information from csv
    graphs = read_data(path_file)
    if isinstance(graphs, tuple):
        not_oriented_graph = graphs[1]
        oriented_graph = graphs[0]

        if not ifconnected(not_oriented_graph):  # check if all verticals are connected
            print('the graph is not connected')
        else:
            #  our functions
            print(f'Graph is bipartite - {bipartite(not_oriented_graph)}')
            #  euler
            print(f'Euler cycle for directed graph - {euler_circuit_directed(read_data(path_file)[0])}')
            print(f'Euler cycle for not directed graph - {euler_circuit_not_directed(read_data(path_file)[1])}')
            #  hamilton
            print(f"Hamiltonian Cycle for not connected graph: {pre_hamilton(not_oriented_graph, False)}")
            print(f"Hamiltonian Cycle for connected graph: {pre_hamilton(oriented_graph, True)}")
