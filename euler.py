def is_euler_possible_not_directed(graph_dict: dict) -> bool:
    """
    Checks whether a not directed graph has Eulerian circuit or not
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Returns:
        bool: True if the graph_dict has Eulerian circuit False if not
    >>> is_euler_possible_not_directed({1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]})
    False
    >>> is_euler_possible_not_directed({1: [2, 3], 2: [1, 3], 3: [1, 2]})
    True
    """
    multiplicity = []

    for _, item in graph_dict.items():
        multiplicity.append(len(item))
    num_of_odd = 0

    for i in range(len(multiplicity)):
        if multiplicity[i] % 2 == 1:
            num_of_odd += 1

    if num_of_odd > 0:
        return False
    return True


def euler_circuit_not_directed(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit in not directed graph
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Retuns:
        list: list of vertices whiсh form Euler circuit
        str: message that graph_dict is not connected
    >>> euler_circuit_not_directed({1: [4, 2], \
    2: [1, 3, 6, 5], \
    3: [2,4], \
    4: [1, 3], \
    5: [2, 6], \
    6: [2, 5]})
    [1, 4, 3, 2, 6, 5, 2, 1]
    """
    if is_euler_possible_not_directed(graph_dict) is False:
        return "Graph has no Eulerial circuit"

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

        for key in graph_dict:
            if key not in circuit:
                return "Graph is not connected"
    return circuit


def is_euler_possible_directed(graph_dict: dict) -> bool:
    """
    Checks whether a directed graph has Eulerian circuit or not
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Returns:
        bool: True if the graph_dict has Eulerian circuit False if not
    >>> is_euler_possible_directed({1: [2], 2: [3], 3: [1]})
    True
    >>> is_euler_possible_directed({1: [2], 2: [3], 3: [1, 2]})
    False
    """
    counter_of_bad_vertices = 0

    for key in graph_dict:
        enter = list(value for value in graph_dict.values()).count([key])
        exit = len(graph_dict[key])

        if enter != exit:
            counter_of_bad_vertices += 1

    if counter_of_bad_vertices > 0:
        return False
    return True


def euler_circuit_directed(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit in a directed graph
    Args:
        graph_dict: dictionary where keys are vertices
        and keys are lists of connected vertices
    Retuns:
        list: list of vertices whiсh form Euler circuit
        str: message that graph_dict is not connected
    >>> euler_circuit_not_directed({1: [4, 2],\
    2: [1, 3, 6, 5], \
    3: [2,4], \
    4: [1, 3], \
    5: [2, 6], \
    6: [2, 5]})
    [1, 4, 3, 2, 6, 5, 2, 1]
    """
    if is_euler_possible_directed(graph_dict) is False:
        return "Graph has no Eulerial circuit"

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
                stack.append(random_edge)
    
        for key in graph_dict:
            if key not in circuit:
                return "Graph is not connected"
    
    return circuit


if __name__ == "__main__":
    import random
    euler_circuit_directed(read_data(path_to_file)[0])
    euler_circuit_not_directed(read_data(path_to_file)[1])
