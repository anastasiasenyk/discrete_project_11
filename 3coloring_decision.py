def color_check(color: int, coloring: dict, neighbours: list):
    for neighbour in neighbours:
        if coloring[neighbour] == color:
            return False
    return True


def coloring_rec(coloring: dict, vert_index: int, vertices: list, graph: dict) -> bool:
    if vert_index == len(vertices):
        return True
    for color in range(1, 4):
        if color_check(color, coloring, graph[vertices[vert_index]]):
            coloring[vertices[vert_index]] = color
            if coloring_rec(coloring, vert_index + 1, vertices, graph):
                return True
            coloring[vertices[vert_index]] = 0
    return False


def coloring_decision(graph: dict) -> bool:
    """
    Checks whether it is possible to color graph by 3 colors.
    """
    coloring_dict = {}
    for vert in graph.keys():
        coloring_dict[vert] = 0
    vertices = list(graph.keys())
    coloring_rec(coloring_dict, 0, vertices, graph)
    return coloring_dict

print(coloring_decision({'1': ['2', '5', '4'], '2': ['1', '5', '3'], '3': [
      '2', '6', '4'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['5', '3', '4']}))
