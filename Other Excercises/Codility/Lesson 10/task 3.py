import math

def check(k, peaks, N):
    
    index = 0    
    i = 0
    
    while i * k < N:
        if index >= len(peaks) or peaks[index] >= (i + 1) * k:
            return False
            
        while index < len(peaks) and peaks[index] < (i + 1) * k:
            index += 1

        i += 1            
    return True
    

def solution(A):
    # write your code in Python 3.6
    peaks = []
   
    for i in range(1, len(A) - 1):
       if A[i - 1] < A[i] and A[i + 1] < A[i]:
           peaks.append(i)

    if len(peaks) == 0:
        return 0
           
    divisors = []
    
    n = len(A)
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)

    divisors.sort()

    for k in divisors:
        t = check(k, peaks, len(A))
        print(n // k, t)
        if t:
            return n // k
                
                
                
                
    
            
print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))

print(solution([5]))

print(solution([1, 4, 3]))