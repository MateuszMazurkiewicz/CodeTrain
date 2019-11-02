# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
# Assume the expression is properly formed.

# Example:

# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4

# Here's the function signature:

def is_opening_bracket(s):
    return s == '('

def is_closin_bracket(s):
    return s == ')'

def is_sign(s):
    return s in ['+', '-']

def is_digit(s):
    return s in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def find_matching_bracket(expression, opening_bracket_index, end):    
    brackets_number = 0    

    for i in range(opening_bracket_index, end):   
        s = expression[i]      
        if is_opening_bracket(s):
            brackets_number += 1

        if is_closin_bracket(s):
            brackets_number -= 1

        if brackets_number == 0:
            return i

    return -1

def operation(digit, sign, previous):
    x = digit
    if sign == '-':
        return previous - x
    if sign == '+':
        return previous + x



def eval(expression, start=0, end=-1):
  # Fill this in.
    expression = expression.replace(" ", "")
    if end == -1:
        end = len(expression)

    index = start
    result = 0
    sign = '+'
    while index < end:
        s = expression[index]
        if is_sign(s):
            sign = s
        elif is_digit(s):
            result = operation(int(s), sign, result)
        elif is_opening_bracket(s):
            matching_index = find_matching_bracket(expression, index, end)            
            tmp_evaluation = eval(expression, index + 1, matching_index)
            result = operation(tmp_evaluation, sign, result)
            index = matching_index + 2
            continue

        index += 1

    return result

print(eval('-1 + (1 + 2 + 3 - 1)'))
# 4

print(eval('- (3 + ( 2 - 1 ) )'))
# -4