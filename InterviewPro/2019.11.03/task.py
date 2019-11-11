#Given an undirected graph, determine if a cycle exists in the graph.

#Here is a function signature:

def find_cycle(graph):    
    to_visit = []
    visited = set()
    to_visit.append(0)

    while len(to_visit) > 0:
        node = to_visit.pop()
        for n in graph[node]:
            if n in visited:
                return True
            visited.add(n)
            to_visit.insert(0, n)
    return False

    


graph_1 = {0: [1, 2], 1: [3, 4], 2: [], 3: [], 4: []}

graph_2 = {0: [1, 2], 1: [3, 4], 2: [], 3: [0], 4: []}

print(find_cycle(graph_1))
# False

print(find_cycle(graph_2))
# True
