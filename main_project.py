""""task 7 group 11"""


def read_data(path_to_file: str) -> tuple:
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


if __name__ == '__main__':
    import pandas as pd
    import os.path
    path_to_file = 'graph.csv'  # path to our csv file

    #  read information from csv
    graphs = read_data(path_to_file)
    not_oriented_graph = graphs[0]
    oriented_graph = graphs[1]

    #  our functions
    print()
