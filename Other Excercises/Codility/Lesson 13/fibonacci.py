def fibonacci(k):
    first = 0
    second = 1

    for _ in range(k):
        tmp = first
        first = second
        second += tmp

    return first


#for i in range(6):
#    print(i, fibonacci(i))

def fibonacci_modulo(a, b):
    m = 1 << b
    m -= 1

    first = 0
    second = 1

    for _ in range(a + 1):
        tmp = first
        first = second
        second += tmp
        second = second & m
        

    return first 


#print(fibonacci(4))

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]

for a, b in zip(A, B):
    print(fibonacci_modulo(a, b))