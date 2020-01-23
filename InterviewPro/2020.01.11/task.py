'''
You are given an array of integers, and an integer K. Return the subarray which sums to K. You can assume that a solution will always exist.
'''

def find_continuous_k(l, k):
    cumulative = [l[0]]

    for i in range(1, len(l)):
        cumulative.append(cumulative[-1] + l[i])

    start = 0
    end = 0

    tmp = 0

    while end < len(l) and tmp < k:
        end += 1
        tmp = cumulative[end] - cumulative[start]

        while start <= end and tmp > k:
            start += 1
            tmp = cumulative[end] - cumulative[start]

        if tmp == k:
            return l[start + 1:end + 1]

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]