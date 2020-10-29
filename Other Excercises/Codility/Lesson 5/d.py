def solution(A):
    # write your code in Python 3.6
    
    points = []
    for i in range(len(A)):
        points.append((i - A[i], 'b'))
        points.append((i + A[i], 'e'))
        
        
    points.sort(key=lambda x: (x[0], x[1]))
    
    opened = 0
    result = 0
    
    for x in points:
        if x[1] == 'b':
            result += opened
            opened += 1
            if result >  10000000:
                return -1
        else:
            opened -= 1
            
    return result

print(solution( [1, 5, 2, 1, 4, 0]))