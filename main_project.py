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
    file = pd.read_csv(path_to_file, index_col=0)
    graph_dict_no = {}  # graph is not oriented
    graph_dict_o = {}  # graph is oriented

    for index, row in file.iterrows():
        vert1 = str(index)
        vert2 = str(row['vertex2'])

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


if __name__ == '__main__':
    import pandas as pd
    import os.path
    path_file = 'graph.csv'  # path to our csv file

    #  read information from csv
    graphs = read_data(path_file)
    not_oriented_graph = graphs[1]
    oriented_graph = graphs[0]

    if not ifconnected(not_oriented_graph):  # check if all verticals are connected
        print('the graph is not connected')
    else:
        #  our functions
        print(f'Graph is bipartite - {bipartite(not_oriented_graph)}')
