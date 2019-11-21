'''
You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

Here's a starting point:
'''

def merge(intervals):
    # Fill this in. 
    res = []
    while len(intervals) > 0:
        stack = []              
        stack.append(intervals[0])
        tmp = [intervals[0][0], intervals[0][1]]
        
        while len(stack) > 0:
            interval = stack.pop()
            intervals.remove(interval)
            if interval[0] < tmp[0]:
                tmp[0] = interval[0]
            if interval[1] > tmp[1]:
                tmp[1] = interval[1]

            for it in intervals:
                if intersects(tmp, it):
                    stack.append(it)

        res.append((tmp[0], tmp[1]))

    return res





def intersects(a, b):
    return (b[0] >= a[0] and b[0] <= a[1]) or (b[1] >= a[0]and b[1] <= a[1]) or (a[0] >= b[0] and a[1] <= b[1])

print(intersects((5, 8), (4, 10)))
print(intersects((5, 8), (6, 10)))
print(intersects((5, 8), (2, 7)))
print(intersects((5, 8), (11, 20)))

print(merge([(1, 3), (5, 8), (0, 2), (4, 10), (20, 25), (9, 12), (11, 13)]))
# [(0, 3), (4, 13), (20, 25)]