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
    graph_dict_no = {c1[0]:[c1[1]], c1[1]:[c1[0]]}  # graph is not oriented
    graph_dict_o = {c1[0]:[c1[1]]}  # graph is oriented

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
        print()
