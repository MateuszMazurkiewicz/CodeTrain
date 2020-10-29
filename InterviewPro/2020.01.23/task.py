"""
Given a directed graph, reverse the directed graph so all directed edges are reversed.

Example:
Input:
A -> B, B -> C, A ->C

Output:
B->A, C -> B, C -> A
"""

from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

def reverse_graph(graph):
    # Fill this in.
    reversed_graph = {}
    for key, val in graph.items():
        if key not in reversed_graph:
            reversed_graph[key] = Node(key)
        for neighbor in val.adjacent:
            if neighbor.value not in reversed_graph:
                reversed_graph[neighbor.value] = Node(neighbor.value)
            reversed_graph[neighbor.value].adjacent += [val]

    return reversed_graph

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

r = reverse_graph(graph)

for key, val in r.items():
    print(key + ": ", [x.value for x in val.adjacent])
    
# []
# ['a', 'b']
# ['a']