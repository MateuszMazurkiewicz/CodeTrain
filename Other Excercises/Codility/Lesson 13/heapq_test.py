import heapq

class Node():
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val
        
h = []

heapq.heappush(h, Node(1))

heapq.heappush(h, Node(2))

heapq.heappush(h, Node(0))

print(h)


