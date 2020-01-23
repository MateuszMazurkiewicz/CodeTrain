'''
Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), return the shortest possible file path (Eliminate all the '..' and '.').

Example

Input: '/Users/Joma/Documents/../Desktop/./../'
Output: '/Users/Joma/'
'''

def shortest_path(file_path):
    folders = file_path.split('/')
    folders = [folder for folder in folders if folder != '.']

    indexes_to_remove = [i for i in range(len(folders)) if folders[i] == '..']
    parents = [x - 1 for x in indexes_to_remove]
    indexes_to_remove += parents
    indexes_to_remove = set(indexes_to_remove)


    res = [folders[i] for i in range(len(folders)) if i not in indexes_to_remove]

    res_str = '/'.join(res)
    return res_str



print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/