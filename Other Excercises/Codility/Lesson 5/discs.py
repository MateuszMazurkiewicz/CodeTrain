def solution(A):
    # write your code in Python 3.6
    start = []
    end = []
    
    for i in range(len(A)):
        start.append(i - A[i])
        end.append(i + A[i])
        
    counter = 0    
        
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if start[i] <= end[j] and end[i] >= start[j]:
                counter += 1
                if counter > 10000000:
                    return -1
                
                
    return counter