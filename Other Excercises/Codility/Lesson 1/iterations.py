def solution(N):
    # write your code in Python 3.6
    counter = 0
    tmp_counter = 0
    started = False
    previous = 0
    
    while N > 0:
        if not N & 1 :
            if previous == 0 and started:
                tmp_counter += 1
            elif previous == 1 and not started:
                started = True
                tmp_counter += 1
                
        elif N & 1 and previous == 0 and started:
            started = False
            if tmp_counter > counter:
                counter = tmp_counter
            tmp_counter = 0
        
        previous = N & 1
        N = N // 2
                    
    return counter