""""task 7 group 11"""


def create_csv() -> str:
    """
    create trial version of graph
    . not required in project
    """
    lst_name = [[1, 2], [3, 5], [5, 1]]
    fd = pd.DataFrame(lst_name, columns=['FIRST_V', 'SECOND_V'])
    fd.to_csv('graph_trial.csv')
    return 'graph_trial.csv'


def read_data(path_to_file: str) -> dict:
    """
    create a dictionary with graph vertices
    Args:
        path_to_file: path to csv file

    Returns:
        graph_dict: dict of vertices
    """
    if not os.path.exists(path_to_file):
        return print("file doesn't exist")
    file = pd.read_csv(path_to_file, index_col=0)
    graph_dict = {}

    # граф орієнтований
    for index, row in file.iterrows():
        if row['FIRST_V'] not in graph_dict.keys():
            graph_dict[row['FIRST_V']] = row['SECOND_V']
        else:
            graph_dict[row['FIRST_V']].append(row['SECOND_V'])

    return graph_dict


if __name__ == '__main__':
    import pandas as pd
    import os.path

    print(read_data(create_csv()))
