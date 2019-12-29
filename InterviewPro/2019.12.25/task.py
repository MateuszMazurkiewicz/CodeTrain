'''
Daily Interview Pro
Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times. 
So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

Your starting point:
'''

import string

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
str_digits = [str(x) for x in digits]

def is_digit(c):
    return c in str_digits

def is_letter(c):
    return c in string.ascii_lowercase

def find_matching_parenthesis(s):
    stack = []

    for i, c in enumerate(s):
        if c == '[':
            stack.append(c)

        elif c == ']':
            stack.pop()

        else:
            continue

        if len(stack) == 0:
            return i

    return -1

def find_number(s):
    n = 0
    index = -1
    for i, c in enumerate(s):
        if is_digit(c):
            n *= 10
            n += int(c)
        else:
            index = i
            break            
    
    return n, index


def evaluate(s):
    res = ''

    n = 0
    start_index = 0
    
    index = 0

    while index < len(s):
        c = s[index]
        if is_letter(c):
            res += c
            index += 1
        elif is_digit(c):
            
            # get n
            n, start_index = find_number(s[index:])
            start_index += index
            # find parenthesis
            final_index = find_matching_parenthesis(s[start_index:])
            final_index += start_index # add offset
            # evaluate inner string
            inner_string = evaluate(s[start_index + 1:final_index])
            # multiply and add
            res += inner_string * n
            # update index
            index = final_index + 1
        else:
            print("ERROR!")
   
    return res

def decodeString(s):
    # Fill this in.
    return evaluate(s)

print(decodeString('2[a2[b]c]'))
# abbcabbc