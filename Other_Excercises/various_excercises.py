import math
import random

# Write a function that adds the corresponding items in two numeric lists (element-wise), i.e., 
# for given x,y return r such that ri=xi+yi. If vectors are of unequal lengths, the shorter one should be recycled,
# e.g.,[1,2,3,4,5,6]+[7,8]==[1,2,3,4,5,6]+[7,8,7,8,7,8].

def add_vectors(a, b):
    greater = max(len(a),len(b))
    res = []
    for i in range(0, greater):
        res.append(a[i % len(a)] + b[i % len(b)])
    return res

# Write a function which checks whether a given natural number is prime.

def is_prime(k):
    for i in range(2, math.floor(math.sqrt(k))):
        if(k % i == 0):
            return False

    return True

# Write a function that counts the number of primes in the set{a, a+ 1, . . . , b}, for given a < b. Hint: implement the Eratosthenes sieve.

def erasthotenes_sieve(n):
    sieve = list(range(2,n))
    for i in range(0, len(sieve)) :
        if sieve[i] == -1:
            continue

        step = sieve[i]
        tmp_index = i + step
        while tmp_index < len(sieve):
            sieve[tmp_index] = -1
            tmp_index +=step    

    return [x for x in sieve if x != -1]

def primes_count(a, b):
    primes = erasthotenes_sieve(b + 1)
    count = 0
    for prime in primes:
        if prime >= a and prime <= b:
            count +=1

        if prime > b:
            break

    return count

# Write a function that finds k least elements.

def find_least_elements(input_list, k):
    res = input_list[0:k]
    max_value = max(res)
    for i in input_list[k:]:
        if i < max_value:
            res.remove(max_value)
            res.append(i)
            max_value = max(res)

    return res

# Implement the bucket sort algorithm.

def bucket_sort(input_list):
    max_value = max(input_list)
    count_list = [0] * (max_value + 1)
    for i in input_list:
        count_list[i] +=1
        res = []

    for i in range(0, len(count_list)):
        res += count_list[i]*[i]

    return res

# Implement selection sort algorithm.

def selection_sort(input_list):   
    x = input_list.copy() 
    for i in range(0, len(x)):        
        index = i 
        for j in range(i + 1, len(x)):
            if x[index] > x[j]:
                index = j

        tmp = x[index]
        x[index] = x[i]
        x[i] = tmp

    return x

# Implement insertion sort algorithm.

def insertion_sort(input_list):   
    x = input_list.copy() 
    for i in range(1, len(x)):
        tmp = x[i]
        j = i - 1
        while j >= 0 and x[j] > tmp:
            x[j + 1] = x[j]
            x[j] = tmp
            j-=1

    return x

# Implement binary search algorithm.

def binary_search(k, x):
    lower = 0
    upper = len(x)
    while lower != upper:
        middle = (upper - lower) // 2 + lower
        if x[middle] == k:
            return True

        elif x[middle] < k:
            lower = middle +1

        elif x[middle] > k:
            upper = middle

    return False

# Write a function that merges two sorted listst.

def merge_sorted_lists(x, y):
    res = []
    y_index = 0
    for i in range(0, len(x)):        
        while y_index < len(y) and y[y_index] <= x[i]:
            res.append(y[y_index])
            y_index+=1

        res.append(x[i])

    for i in range(y_index, len(y)):
        res.append(y[i])

    return res

# Write a function that determines union of two (strictly) increasingly sorted lists.

def union(x, y):
    res = []
    y_index = 0
    for i in range(0, len(x)):
        while y[y_index] <= x[i]:
            if y[y_index] == x[i]:
                y_index+=1
            else:
                res.append(y[y_index])
                y_index+=1

        res.append(x[i])

    for i in range(y_index, len(y)):
        res.append(y[i])

    return res

# Write a function that determines intersection of two (strictly) increasingly sorted lists.

def intersection(x, y):
    res = []
    y_index = 0
    for i in range(0, len(x)):
        while y[y_index] <= x[i]:
            if y[y_index] == x[i]:
                res.append(y[y_index])

            y_index+=1       

    return res

# Implement merge sort algorithm

def merge_sort(x):
    if len(x) == 1:
        return x

    middle = len(x) // 2
    left = merge_sort(x[:middle])
    right = merge_sort(x[middle:])

    return merge_sorted_lists(left, right)

# Write a function that rearranges the elements in a numeric list in such a way that the elements less than or equal to a given v are followed by the elements greater than v.

def split(v, x):
    start_index = 0
    for i in range(0, len(x)):
        if x[i] > v:
            start_index = max(i, start_index)
            while start_index < len(x) and x[start_index] > v:
                start_index+=1

            if start_index == len(x):
                break

            tmp = x[start_index]
            x[start_index] = x[i]
            x[i] = tmp 

# Implement quick sort algorithm

def quick_sort(x):
    if len(x) <=1:
        return x

    index = random.randint(0, len(x) -1)  
    tmp = x[0]
    x[0] = x[index]
    x[index] = tmp
    left = [i for i in x[1:] if i <= x[0]]
    right = [i for i in x[1:] if i > x[0]]

    return quick_sort(left) + [x[0]] + quick_sort(right)

# Implement the quick-select algorithm for finding the k-th smallest value in an unsorted list (for a given k, indexing from 1).

def k_quick_sort(k, x):
    if len(x) <=0:
        return x

    index = random.randint(0, len(x) -1) 
    tmp = x[0]
    x[0] = x[index]
    x[index] = tmp

    left = [i for i in x[1:] if i <= x[0]]

    if len(left) == k - 1:
        return x[0]

    if len(left) >= k:
        return k_quick_sort(k, left)
    

    right = [i for i in x[1:] if i > x[0]]

    return k_quick_sort(k - len(left) - 1, right)

# Implement a partial quick sort algorithm that guarantees that the k smallest values are in order (for a given k, indexing from 1).

def partial_quick_sort(k, x):

    if len(x) <=0:
        return x

    index = random.randint(0, len(x) -1)   

    tmp = x[0]
    x[0] = x[index]
    x[index] = tmp

    left = [i for i in x[1:] if i <= x[0]]

    right = [i for i in x[1:] if i > x[0]]

    if len(left) == k or len(left) == k - 1:
        return quick_sort(left) + [x[0]] + right    

    if len(left) > k:
        return partial_quick_sort(k, left) + [x[0]] + right    

    return quick_sort(left) + [x[0]] + partial_quick_sort(k - len(left) -1, right)

# Four men want to cross a bridge. But at most 2 people may cross it at a time. 
# For man A it takes 10minutes to cross, for B – 5 minutes, C – 2 minutes, and D – 1 minute. 
# If two people cross the bridgetogether, they must walk at the pace of the slower one. 
# Also, it is night. Each trip requires a flashlight.There is only one flashlight. 
# The men are not allowed to toss the light over the river. How fast can you get all 4 men over the bridge? 
# Examine all the 108 possible solutions and determine the optimal one(the optimal time is < 19).

class BridgeProblemSolution():    

    def move(self, people, torch, time):
        if self.count(people, 'A') == 2 and torch =='A':
            return time + max([p['time'] for p in people if p['side'] == 'A'])

        res = []

        if torch == 'A':
            sideA = [p for p in people if p['side'] == 'A']
            for p1 in range(0, len(sideA)):
                sideA[p1]['side'] = 'B'
                for p2 in range(p1 + 1, len(sideA)):
                    sideA[p2]['side'] = 'B'
                    res.append(self.move(people, 'B', time + max(sideA[p1]['time'], sideA[p2]['time'])))
                    sideA[p2]['side'] = 'A'

                sideA[p1]['side'] = 'A'

        if torch =='B':       
            for p in [p for p in people if p['side'] == 'B']:
                p['side'] = 'A'
                res.append(self.move(people, 'A', time + p['time']))
                p['side'] = 'B'

        return min(res)

    def count(self, people, side):
        counter = 0
        for p in people:
            if p['side'] == side:
                counter+=1

        return counter

    def solve(self):
        people = [{'side':'A', 'time':5}, {'side':'A', 'time':10}, {'side':'A', 'time':2}, {'side':'A', 'time':1}]
        return self.move(people, 'A', 0)
