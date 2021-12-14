
def is_euler_possible(graph_dict: dict) -> bool:
    """
    Returns True if the graph_dict can have an Eulerian circuit or only path or nothing
    and False if not
    Args:
        graph_dict: dict of vertices
    Returns:
        bool: whether the graph_dict has Eulerial circuit or not
    >>> is_euler_possible({1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]})
    False
    """
    multiplicity = []
    for key, item in graph_dict.items():
        multiplicity.append(len(item))
    num_of_odd = 0
    for i in range(len(multiplicity)):
        if multiplicity[i] % 2 == 1:
            num_of_odd += 1
    if num_of_odd > 2 or num_of_odd == 1: 
        print("Graph has no Eulerial circuit or Eulerial path") 
        return False
    elif num_of_odd == 2:
        print("Graph has only Eulerian path")
        return False
    else:
        return True


def euler_circuit(graph_dict: dict) -> list:
    """
    Returns Eulerian circuit
    Args:
        graph_dict: dict of vertices
    Retuns:
        list: list of vertices with form Euler circuit
    >>> euler_circuit({1: [4, 2], 2: [1, 3, 6, 5], 3: [2,4], 4: [1, 3], 5: [2, 6], 6: [2, 5]})
    [1, 4, 3, 2, 6, 5, 2, 1]
    """
    if is_euler_possible(graph_dict):
        st = [list(graph_dict.keys())[0]]
        answer = []
        while st != []:
            v = st[-1]
            if len(graph_dict[v]) == 0:
                answer.append(v)
                st.pop(-1)
            else:
                random_m = random.choice(graph_dict[v])
                graph_dict[v].remove(random_m)
                graph_dict[random_m].remove(v)
                st.append(random_m)
        print(answer)
        return answer 
if __name__ == "__main__":
    import random
    G1 = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [4]
    }
    G2 = {
        1: [2, 3, 4, 5],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [1, 4]
    }
    G3 = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2],
        4: [1, 2, 5],
        5: [4]
    }
    G4 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
    }
    G5 = {
        1: [],
        2: []
    }
    G6 = {1: [4, 2], 2: [1, 3, 6, 5], 3: [2,4], 4: [1, 3], 5: [2, 6], 6: [2, 5]}
# print(euler_circuit(G1))
# print(euler_circuit(G2))
# print(euler_circuit(G3))
# print(euler_circuit(G4))
# print(euler_circuit(G5))
# print(euler_circuit(G6))
# import doctest
# doctest.testmod()
(euler_circuit(G1))
(euler_circuit(G2))
(euler_circuit(G3))
(euler_circuit(G4))
(euler_circuit(G5))
(euler_circuit(G6))