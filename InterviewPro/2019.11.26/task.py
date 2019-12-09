'''
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
'''

def say_sequence(k):
    number = '1'

    for _ in range(k - 1):
        tmp = []
        index = 0
        while index < len(number):
            current = number[index]
            counter = 0
           
            while index < len(number) and number[index] == current:
                counter += 1
                index += 1
            tmp.append(str(counter))
            tmp.append(current)

        number = ''.join(tmp)
        
    return number

print(say_sequence(5))
