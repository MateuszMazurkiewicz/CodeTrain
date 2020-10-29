def mean(A):
    return sum(A) / len(A)

def solution(A):
    # write your code in Python 3.6
    #min_slice = A[0:2]
    min_index = 0
    min_mean = mean(A[0:2])
    
    #min_last = A[0:2]
    min_last_index = 0
    last_mean = min_mean
    last_len = 2
    
    for i in range(2, len(A)):
        new_pair = A[i - 1: i + 1]
        
        last_mean = (last_mean * last_len + A[i]) / (last_len + 1)
        last_len += 1
        m = mean(new_pair)
        
        if last_mean > m:
            min_last_index = i - 1
            last_len = 2
            last_mean = m
            
        if min_mean >  last_mean:
            min_mean =  last_mean
            min_index = min_last_index
            
    return min_index


print(solution([4, 5, 1, 5, 8, 2, 2, 9]))