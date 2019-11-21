'''
You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

Here's the function signature:
'''

def word_search(matrix, word):
  # Fill this in.
    m = len(matrix)
    n = len(matrix[0])    
    k = len(word)

    if m < k or n < k:
        return False

    for x in range(m - k + 1):
        for y in range(n - k + 1):
            if search_vertical(matrix, word, x, y):
                return True
            if search_horizontal(matrix, word, x, y):
                return True

    return False

def search_vertical(matrix, word, x, y):
    for i in range(len(word)):
        if matrix[x][y + i] != word[i]:
            return False
    return True

def search_horizontal(matrix, word, x, y):
    for i in range(len(word)):
        if matrix[x + i][y] != word[i]:
            return False
    return True

  
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True