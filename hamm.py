""""task 7 group 11"""
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
    graph_dict_no = {c1[0]:[c1[1]], c1[1]:[c1[0]]}  # graph is not oriented
    graph_dict_o = {c1[0]:[c1[1]]}  # graph is oriented

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


def hamiltonianCycle(graph, visited, path, v, lenght):
    if len(path) == lenght:
        if path[-1] in graph.keys() and path[0] in graph[path[-1]]:
            path.append(path[0])
            return path
        else:
            return False
    lst = list(graph.keys())
    item = lst[v]
    for element in graph[item]:
        if element not in visited:
            visited.append(element)
            path.append(element)
            path_bool = hamiltonianCycle(graph, visited, path, v+1, lenght)
            if isinstance(path_bool, list):
                return path_bool
            visited.pop(-1)
            path.pop(-1)
    return False




if __name__ == '__main__':
    import pandas as pd
    import os.path
    # hamiltonian_20_151_try1.csv y y
    # hamiltonian_20_81_try2.csv y n
    # hamiltonian_10_38_try1.csv y n
    # hamiltonian_10_14_try2.csv n n
    path_file = 'hamiltonian_20_151_try1.csv'   # path to our csv file


    #  read information from csv
    graphs = read_data(path_file)
    not_oriented_graph = graphs[1]
    oriented_graph = graphs[0]


    if ifconnected(not_oriented_graph):
        lenght = len(list(not_oriented_graph.keys()))
        visited = [list(not_oriented_graph.keys())[0]]
        path = [list(not_oriented_graph.keys())[0]]

        print("Hamiltonian Cycle for not connected graph: ")
        path = hamiltonianCycle(not_oriented_graph, visited, path, 0, lenght)
        if isinstance(path, list):
            print(path)
        else:
            print('No NO NOOOOOOOO')


        lenght = len(list(oriented_graph.keys()))
        visited = [list(oriented_graph.keys())[0]]
        path = [list(oriented_graph.keys())[0]]

        print("Hamiltonian Cycle for connected graph: ")
        path = hamiltonianCycle(oriented_graph, visited, path, 0, lenght)
        if isinstance(path, list):
            print(path)
        else:
            print('No NO NOOOOOOOO')