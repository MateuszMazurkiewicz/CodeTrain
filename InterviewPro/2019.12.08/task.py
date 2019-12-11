'''You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("

Here's a start:
'''

def count_invalid_parenthesis(string):
    stack = []
    wrong_counter = 0
    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                wrong_counter += 1

    wrong_counter += len(stack)
    return wrong_counter

print(count_invalid_parenthesis("()())()"))
# 1
