def solution(A, B):

    n = max(A)
    p = max(B)

    m = 1 << p
    m -= 1

    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 2):
        tmp = (fib[i - 1] + fib[i - 2])
        tmp = tmp & m
        fib[i] = tmp
    
    res = [0] * len(A)

    for i in range(len(A)):
        m = 1 << B[i]
        m -= 1
        res[i] = fib[A[i] + 1] & m
        
    return res

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]

print(solution(A, B))