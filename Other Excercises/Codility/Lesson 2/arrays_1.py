def solution(A):
    # write your code in Python 3.6
    new_a = sorted(A)
    for i in range(0, len(new_a), 2):
        if i + 1 >= len(new_a) or new_a[i] != new_a[i+1]:
            return new_a[i]


print(solution([42]))