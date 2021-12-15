import random
def is_euler_possible(graph_dict: dict) -> str:
    """
    Returns True if graph_dict can have an Eulerian circuit
    returns "only path" if graph_dict has only Eulerian path
    returns "nothing" if graph has no path and no circuit
    Args:
        graph_dict: dictionary where keys are vertices 
        and keys are lists of connected vertices
    Returns:
        str: whether the graph_dict has Eulerial circuit or Euler path or nothing
    >>> is_euler_possible({1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]})
    'only path'
    """
    multiplicity = []
    for _, item in graph_dict.items():
        multiplicity.append(len(item))
    num_of_odd = 0
    for i in range(len(multiplicity)):
        if multiplicity[i] % 2 == 1:
            num_of_odd += 1
    if num_of_odd > 2 or num_of_odd == 1:
        return "nothing"
    elif num_of_odd == 2:
        return "only path"
    else:
        return True


def euler_circuit(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit
    Args:
        graph_dict: dictionary where keys are vertices 
        and keys are lists of connected vertices
    Retuns:
        list: list of vertices whiсh form Euler circuit
    >>> euler_circuit({1: [4, 2], 2: [1, 3, 6, 5], 3: [2,4], 4: [1, 3], 5: [2, 6], 6: [2, 5]})
    [1, 4, 3, 2, 6, 5, 2, 1]
    """
    if is_euler_possible(graph_dict) == "nothing":
        return "Graph has no Eulerial circuit or Eulerial path"
    elif is_euler_possible(graph_dict) == "only path":
        return "Graph has only Eulerian path"
    else:
        stack = [list(graph_dict.keys())[0]]
        circuit = []
        while stack != []:
            curr_vertex = stack[-1]
            if len(graph_dict[curr_vertex]) == 0:
                circuit.append(curr_vertex)
                stack.pop(-1)
            else:
                random_edge = random.choice(graph_dict[curr_vertex])
                graph_dict[curr_vertex].remove(random_edge)
                graph_dict[random_edge].remove(curr_vertex)
                stack.append(random_edge)
        return circuit


if __name__ == "__main__":
    g = {"1": ["5", ], "2": ["5", "1"], "3": ["4", "5"], "4": ["5", "3"], "5": ["2", "4", "1", "3"]}
    print(euler_circuit(g))
    import doctest
    doctest.testmod()