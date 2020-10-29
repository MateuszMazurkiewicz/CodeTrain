import math

def solution(A):
    # find peaks
    peaks = []
   
    for i in range(1, len(A) - 1):
       if A[i - 1] < A[i] and A[i + 1] < A[i]:
           peaks.append(i)
    # find distances

    distances = []

    for i in range(1, len(peaks)):
        distances.append(peaks[i] - peaks[i - 1])

    a = len(A)

    #if distances:
    #    a -= distances[0] - len(A) - distances[-1] + 1

    n = min(len(peaks), 1 + int(math.sqrt(a)))
    for k in range(n, 0, -1):
        t = check_peaks(k, peaks)
        if t:
            return k

    '''
    for k in range(n, 0, -1):
        t = check(k, distances, len(A))
        #print(k, t)

        if t:
            return k
    '''
    return 0



def check_peaks(k, peaks):
    counter = 1    
    current = peaks[0]
    for i in range(1, len(peaks)):
        if peaks[i] - current >= k:
            counter += 1
            current = peaks[i]

        if counter >= k:
            break

    return counter >= k



print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))

print(solution([5]))

print(solution([1,5,2]))

def check(k, distances, N):
    counter = 1

    i = 0
    tmp_distance = 0

    total_distance = 0
    while i < len(distances):
        if distances[i] + tmp_distance >= k:
            counter += 1
            tmp_distance = 0            
        else:
            tmp_distance += distances[i]

        total_distance += distances[i]

        i += 1

    return counter >= k