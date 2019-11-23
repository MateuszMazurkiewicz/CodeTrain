'''
You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.

       X               
   X███XX█X              
 X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]

Here's your starting pont:
'''

def capacity(arr):
    # Fill this in.
    index = 0
    puddles = []
    while index < len(arr):
        left, right, index = find_puddle(index, arr)
        puddles.append((left, right))    

    amount_of_water = 0
    for puddle in puddles:
        amount_of_water += find_puddle_volume(puddle, arr)

    return amount_of_water

def find_puddle_volume(indexes, arr):   
   
    left = indexes[0]
    right = indexes[1]

    min_height = min(arr[left], arr[right])
    volume = 0

    for i in range(left + 1, right):
        volume += min_height - arr[i]    

    return volume


def find_puddle(index, arr):
    left = arr[index]
    right = -1
    rigth_index = index

    i = index + 1 

    while i < len(arr) and arr[i] <= left:
        current_height = arr[i]
        
        if current_height >= right:
            right = current_height
            rigth_index = i
        i += 1

    if i < len(arr) and arr[i] > right:
        right = arr[i] 
        rigth_index = i

    return index, rigth_index, i



print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6