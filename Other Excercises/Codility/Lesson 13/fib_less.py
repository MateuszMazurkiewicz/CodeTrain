def fib_set(k):

    fib = [0] * (k + 2)
    fib[1] = 1
    i = 2
    while fib[i - 1] <= k:
        fib[i] = (fib[i - 1] + fib[i - 2])
        i += 1

    return set(fib)



print(fib_set(20))

