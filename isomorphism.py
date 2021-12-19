"""5th function"""
import time
from itertools import permutations


def vertices_check_not_directed(vertice_1: str, vertice_2: str, graph_1: dict, graph_2: dict) -> bool:
    """
    Check whether two vertices have same degree and \
    are connected with vertices which have same degrees.
    """
    if len(graph_1[vertice_1]) != len(graph_2[vertice_2]):
        return False
    vertice_1_deg = {}
    vertice_2_deg = {}
    for vertice in graph_1[vertice_1]:
        deg = len(graph_1[vertice])
        if deg not in vertice_1_deg.keys():
            vertice_1_deg[deg] = 1
        else:
            vertice_1_deg[deg] += 1
    for vertice in graph_2[vertice_2]:
        deg = len(graph_2[vertice])
        if deg not in vertice_2_deg.keys():
            vertice_2_deg[deg] = 1
        else:
            vertice_2_deg[deg] += 1
    if vertice_1_deg == vertice_2_deg:
        return True
    else:
        return False


# # Python3 program to print all the cycles
# # in an undirected graph
# N = 100000

# # variables to be used
# # in both functions
# graph = [[] for i in range(N)]
# cycles = [[] for i in range(N)]


# # Function to mark the vertex with
# # different colors for different cycles
# def dfs_cycle(u, p, color: list,
# 			mark: list, par: list):
# 	global cyclenumber

# 	# already (completely) visited vertex.
# 	if color[u] == 2:
# 		return

# 	# seen vertex, but was not
# 	# completely visited -> cycle detected.
# 	# backtrack based on parents to
# 	# find the complete cycle.
# 	if color[u] == 1:
# 		cyclenumber += 1
# 		cur = p
# 		mark[cur] = cyclenumber

# 		# backtrack the vertex which are
# 		# in the current cycle thats found
# 		while cur != u:
# 			cur = par[cur]
# 			mark[cur] = cyclenumber

# 		return

# 	par[u] = p

# 	# partially visited.
# 	color[u] = 1

# 	# simple dfs on graph
# 	for v in graph[u]:

# 		# if it has not been visited previously
# 		if v == par[u]:
# 			continue
# 		dfs_cycle(v, u, color, mark, par)

# 	# completely visited.
# 	color[u] = 2

# # add the edges to the graph
# def addEdge(u, v):
# 	graph[u].append(v)
# 	graph[v].append(u)

# # Function to print the cycles
# def printCycles(edges, mark: list):

# 	# push the edges that into the
# 	# cycle adjacency list
# 	for i in range(1, edges + 1):
# 		if mark[i] != 0:
# 			cycles[mark[i]].append(i)

# 	# print all the vertex with same cycle
# 	for i in range(1, cyclenumber + 1):

# 		# Print the i-th cycle
# 		print("Cycle Number %d:" % i, end = " ")
# 		for x in cycles[i]:
# 			print(x, end = " ")
# 		print()

# # Driver Code
# if __name__ == "__main__":

# 	# add edges
# 	addEdge(1, 2)
# 	addEdge(2, 3)
# 	addEdge(3, 4)
# 	addEdge(4, 6)
# 	addEdge(4, 7)
# 	addEdge(5, 6)
# 	addEdge(3, 5)
# 	addEdge(7, 8)
# 	addEdge(6, 10)
# 	addEdge(5, 9)
# 	addEdge(10, 11)
# 	addEdge(11, 12)
# 	addEdge(11, 13)
# 	addEdge(12, 13)

# 	# arrays required to color the
# 	# graph, store the parent of node
# 	color = [0] * N
# 	par = [0] * N

# 	# mark with unique numbers
# 	mark = [0] * N

# 	# store the numbers of cycle
# 	cyclenumber = 0
# 	edges = 13

# 	# call DFS to mark the cycles
# 	dfs_cycle(1, 0, color, mark, par)

# 	# function to print the cycles
# 	printCycles(edges, mark)

# # This code is contributed by
# # sanjeev2552


def isomorphism_of_not_directed_graphs(graph_1: dict, graph_2: dict) -> bool:
    """
    Checks whether graphs are isomorphic.
    Returns True if they are, False if they don't.
    """
    # інваріант_1: кількість вершин
    if len(graph_1.keys()) != len(graph_2.keys()):
        return False

    # інваріант_2 і 3: кількість ребер і кількість вершин конкретного степеня
    edges_1 = 0
    edges_2 = 0
    deg_graph_1 = {}
    deg_graph_2 = {}

    for vertice in graph_1.values():
        deg = len(vertice)
        edges_1 += deg
        if deg not in deg_graph_1.keys():
            deg_graph_1[deg] = 1
        else:
            deg_graph_1[deg] += 1

    for vertice in graph_2.values():
        deg = len(vertice)
        edges_2 += deg
        if deg not in deg_graph_2.keys():
            deg_graph_2[deg] = 1
        else:
            deg_graph_2[deg] += 1

    if edges_1 != edges_2 or deg_graph_1 != deg_graph_2:
        return False

    # графи все-таки ізоморфні?
    #!!!спочатку брати вершину з найбільшим степенем!!!
    all_variants = tuple(permutations(graph_2.keys()))
    vertices_1 = [vertice for vertice in graph_1.keys()]
    for variant in all_variants:
        for index, vertice_2 in enumerate(variant):
            if vertices_check_not_directed(vertices_1[index], vertice_2, graph_1, graph_2) is False:
                break
            else:
                if index == len(variant) - 1:
                    return True
    return False


def vertices_check_directed(connected_vert_1: list, connected_vert_2: list,
                            deg_graph_1: dict, deg_graph_2: dict) -> bool:
    """
    Check whether two vertices have same degree and \
    are connected with vertices which have same degrees.
    """
    deg_connected_1 = {}
    deg_connected_2 = {}

    for vert in connected_vert_1:
        if tuple(deg_graph_1[vert]) not in deg_connected_1.keys():
            deg_connected_1[tuple(deg_graph_1[vert])] = 1
        else:
            deg_connected_1[tuple(deg_graph_1[vert])] += 1

    for vert in connected_vert_2:
        if tuple(deg_graph_2[vert]) not in deg_connected_2.keys():
            deg_connected_2[tuple(deg_graph_2[vert])] = 1
        else:
            deg_connected_2[tuple(deg_graph_2[vert])] += 1

    if deg_connected_1 == deg_connected_2:
        return True
    else:
        return False


def isomorphism_of_directed_graphs(graph_1: dict, graph_2: dict,
                                   vert_connected_1: dict, vert_connected_2: dict) -> bool:
    """
    Checks whether graphs are isomorphic.
    Returns True if they are, False if they don't.
    """
    # інваріанти: кількість вершин, степені входу і виходу
    degs_graph_1 = {}
    degs_graph_2 = {}

    for vertice, edges in graph_1.items():
        if vertice not in degs_graph_1.keys():
            degs_graph_1[vertice] = [0, 0]
        degs_graph_1[vertice][0] = len(edges)
        for edge in edges:
            if edge not in degs_graph_1.keys():
                degs_graph_1[edge] = [0, 0]
            degs_graph_1[edge][1] += 1

    for vertice, edges in graph_2.items():
        if vertice not in degs_graph_2.keys():
            degs_graph_2[vertice] = [0, 0]
        degs_graph_2[vertice][0] = len(edges)
        for edge in edges:
            if edge not in degs_graph_2.keys():
                degs_graph_2[edge] = [0, 0]
            degs_graph_2[edge][1] += 1

    # кількість вершин
    if len(degs_graph_1.keys()) != len(degs_graph_2.keys()):
        return False

    # степені входу, виходу
    degs_check = {}
    for degs in degs_graph_1.values():
        if tuple(degs) not in degs_check.keys():
            degs_check[tuple(degs)] = 1
        else:
            degs_check[tuple(degs)] += 1

    for degs in degs_graph_2.values():
        if tuple(degs) not in degs_check.keys():
            return False
        else:
            degs_check[tuple(degs)] -= 1

    for vertices_number in degs_check.values():
        if vertices_number != 0:
            return False

    # графи все-таки ізоморфні?
    all_variants = tuple(permutations(degs_graph_2.keys()))

    vertices_1 = [vertice for vertice in degs_graph_1]
    for variant in all_variants:
        for index, vertice_2 in enumerate(variant):
            vertice_1 = vertices_1[index]
            if degs_graph_1[vertice_1] != degs_graph_2[vertice_2]:
                break
            if not vertices_check_directed(vert_connected_1[vertice_1],
                                           vert_connected_2[vertice_2], degs_graph_1, degs_graph_2):
                break
            if index == len(variant) - 1:
                return True
    return False


start = time.time()
print(isomorphism_of_directed_graphs({'a': ['c', 'd'], 'c': [
      'b'], 'd': ['b']}, {'a': ['b'], 'b': ['d'], 'c': ['a', 'd']}, {'a':['c','d'], 'c':['a','b'], 'd':['a','b'], 'b':['c','d']},{'a':['b','c'], 'c':['a','d'], 'd':['c','b'], 'b':['a','d']}))
# print(isomorphism_of_not_directed_graphs({'1': ['2', '5', '4'], '2': ['1', '5', '3'], '3': [
#       '2', '6', '4'], '4': ['3', '6', '1'], '5': ['2', '1', '6'], '6': ['5', '3', '4']}, {'a': ['b','f','d'],'b': ['a','e','c'],'c': ['b','f','d'],'d': ['a','c','e'],'e': ['b','f','d'],'f': ['e','c','a']}))
finish = time.time()
print(finish-start)
