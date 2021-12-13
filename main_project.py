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


def bipartite(graph_dict: dict) -> bool:
    """
    determine whether our graph is oriented
    Args:
        graph_dict: dict of vertices

    Returns:
        bool: whether the graph is oriented or not
    """
    first_vert = list(graph_dict.keys())[0]
    visited, queue = [first_vert], [first_vert]
    first_part, second_part = [first_vert],  []
    while queue:
        vertex = queue.pop(0)

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

    answer = input("Do you want graph to be oriented (y/n)? ")
    while answer not in ("y", "n"):
        answer = input("Wrong character! Do you want graph to be oriented (y/n)? ")
    if answer == "y":
        oriented = True
    else:
        oriented = False

    path_to_file = 'graph.csv'  # path to our csv file
    print(bipartite(read_data(path_to_file, oriented)))
