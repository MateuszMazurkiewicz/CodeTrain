'''
You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.
'''

def is_shifted(a, b):
    a = list(a)
    b = list(b)
    for _ in range(len(a)):
        if a == b:
            return True

        x = a.pop(0)
        a.append(x)

    return False
  
  
print(is_shifted('abcde', 'cdeab'))
# True
