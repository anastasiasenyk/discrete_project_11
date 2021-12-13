""""task 7 group 11"""


def read_data(path_to_file: str, oriented: bool) -> dict:
    """
    create a dictionary with graph vertices
    Args:
        path_to_file: path to csv file
        oriented: bool

    Returns:
        graph_dict: dict of vertices
    """
    if not os.path.exists(path_to_file):
        return print("file doesn't exist")
    file = pd.read_csv(path_to_file, index_col=0)
    graph_dict = {}

    for index, row in file.iterrows():
        vert1 = str(index)
        vert2 = str(row['vertex2'])
        if oriented:  # graph is oriented
            if vert1 not in graph_dict.keys():
                graph_dict[vert1] = [vert2]
            else:
                graph_dict[vert1].append(vert2)
        else:  # graph is not oriented
            if vert1 not in graph_dict.keys():
                graph_dict[vert1] = [vert2]
            else:
                graph_dict[vert1].append(vert2)
            if vert2 not in graph_dict.keys():
                graph_dict[vert2] = [vert1]
            else:
                graph_dict[vert2].append(vert1)
    return graph_dict


if __name__ == '__main__':
    import pandas as pd
    import os.path

    answer = input("Do you want graph to be oriented (y/n)? ")
    while answer not in ("y", "n"):
        answer = input("Wrong character! Do you want graph to be oriented (y/n)? ")
    if answer == "y":
        oriented = True
    else:
        oriented = False

    path_to_file = 'graph.csv'  # path to our csv file
    print(read_data(path_to_file, oriented))
