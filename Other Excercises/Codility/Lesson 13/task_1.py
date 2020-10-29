import heapq
import math

class Node():
    def __init__(self):
        self.val = -1
        self.prev_node = None
        self.next_node = None

    def __lt__(self, other):
        return self.val < other.val

    def remove(self):
        if self.prev_node:
            self.prev_node.next_node = self.next_node
        if self.next_node:
            self.next_node.prev_node = self.prev_node


def fib_s(k):

    fib = [0] * (k + 2)
    fib[1] = 1
    i = 2
    while fib[i - 1] <= k:
        fib[i] = (fib[i - 1] + fib[i - 2])
        i += 1

    return set(fib)

def solution(A):
    # write your code in Python 3.6

    min_steps = math.inf

    val_index = {}

    val_step = {}

    indexes = []
    indexes.append(0)
    for i in range(len(A)):
        if A[i] == 1:
            indexes.append(i + 1)

    indexes.append(len(A) + 1)


    for i in range(len(indexes)):
        val_index[indexes[i]] = i
        val_step[indexes[i]] = 0

    head = Node()

    head.val = indexes[0]
    head.index = 0

    current = head

    for i in range(1, len(indexes)):
        node = Node()
        node.val = indexes[i]
        node.prev_node = current
        current.next_node = node
        current = node

    tail = current
    tail_val = tail.val

    fib_set = fib_s(tail_val)

    priority_queue = []

    head
    heapq.heappush(priority_queue, head)
    

    while len(priority_queue) > 0:
        current_node = heapq.heappop(priority_queue)
        current_val = current_node.val
        # next_value = priority_queue[0].val if len(priority_queue) > 0 else -1
        if tail_val - current_val in fib_set:
            steps = val_step[current_val] + 1
            min_steps = min(min_steps, steps)

        
        next_node = current_node.next_node
        while next_node and next_node.val != tail_val:
            if next_node.val - current_val in fib_set:
                val_step[next_node.val] = val_step[current_val] +  1
                next_node.remove()
                heapq.heappush(priority_queue, next_node)

            #elif next_node.val < next_value:                
            #    next_node.remove()

            next_node = next_node.next_node


    if min_steps != math.inf:
        return min_steps

    return -1






A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]

print(solution(A))

