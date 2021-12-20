def color_check(color: str, coloring: dict, neighbours: list) -> bool:
    """
    Checks whether adjacent vertices are colored in the same color or not.
    Args:
        color: color in which we try to color the vertice
        coloring: dict where keys are vertices of the graph, values - color of that vertice
        neighbours: list of adjacent vertices
    Returns:
        bool: True if the vertice can be colored in that color, False if not
    >>> color_check('red', {'1': 'blue', '2': 0}, ['1'])
    True
    >>> color_check('red', {'1': 'red', '2': 0}, ['1'])
    False
    """
    for neighbour in neighbours:
        if coloring[neighbour] == color:
            return False
    return True


def coloring_rec(coloring: dict, vertices: list, vert_index: int, graph: dict) -> bool:
    """
    Recursive function, which colors vertices of the graph.
    Args:
        coloring: dict where keys are vertices of the graph, values - color of that vertice
        vertices: list of vertices
        vert_index: index of vertice in a list vertices
        graph: dict of vertices
    Returns:
        bool: True if graph can be colored in three colors, False if not 
    >>> coloring_rec({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}, ['1', '2', '3', '4', '5', '6'], 0,{'1': ['2', '5', '4'], '2': ['1', '5', '3'], '3': \
    ['2', '6', '4'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['5', '3', '4']})
    True

    >>> coloring_rec({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}, ['1', '2', '3', '4', '5', '6'], 0,{'1': ['2', '3','5', '4','6'], '2': ['1', '5', '3'], '3': \
    ['2', '6', '4','1'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['1','5', '3', '4']})
    False
    """
    if vert_index == len(vertices):
        return True
    for color in ['red', 'blue', 'green']:
        if color_check(color, coloring, graph[vertices[vert_index]]):
            coloring[vertices[vert_index]] = color
            if coloring_rec(coloring, vertices, vert_index + 1,  graph):
                return True
            coloring[vertices[vert_index]] = 0
    return False


def coloring_decision(graph: dict):
    """
    Function which tries to color graph in three colors.
    Args:
        graph: dict of vertices
    Returns:
        list: list of tuples (vertice, color)
        str: message that coloring isn't possible
    >>> coloring_decision({'1': ['2', '5', '4'], '2': ['1', '5', '3'], '3': \
    ['2', '6', '4'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['5', '3', '4']})
    [('1', 'red'), ('2', 'blue'), ('3', 'red'), ('4', 'green'), ('5', 'green'), ('6', 'blue')]

    >>> coloring_decision({'1': ['2', '3','5', '4','6'], '2': ['1', '5', '3'], '3': \
    ['2', '6', '4','1'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['1','5', '3', '4']})
    "This graph can't be colored by three colors"
    """
    coloring_dict = {}
    for vert in graph.keys():
        coloring_dict[vert] = 0
    vertices = list(graph.keys())

    if not coloring_rec(coloring_dict,  vertices, 0, graph):
        return "This graph can't be colored by three colors"

    result = []
    for vert, color in coloring_dict.items():
        result.append((vert, color))
    return result
