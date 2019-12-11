'''
You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

Here's a starting point:
'''

def running_median(stream):
    median_index = 0
    for i in range(0, len(stream)):
        j = i
        while j > 0 and stream[j] < stream[j - 1]:
            tmp = stream[j]
            stream[j] = stream[j - 1]
            stream[j - 1] = tmp
            j -= 1

        median_index = i // 2
        if i % 2 == 1:            
            print((stream[median_index] + stream[median_index + 1])/2, end = ' ')
        else:
            print(stream[median_index], end = ' ', )

running_median([2, 1, 4, 7, 2, 0, 5])

# 2 1.5 2 3.0 2 2.0 2