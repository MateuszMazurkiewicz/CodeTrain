# Given a string with the initial condition of dominoes, where:

#. represents that the domino is standing still
#L represents that the domino is falling to the left side
#R represents that the domino is falling to the right side

#Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

#Example:

#Input:  ..R...L..R.
#Output: ..RR.LL..RR

#Here is your starting point:

class Solution(object):
  def pushDominoes(self, dominoes):
    # Fill this in.
    res = list(dominoes)
    
    for i in range(1, len(dominoes)):
        if dominoes[i - 1] == 'R' and dominoes[i] == '.':
            res[i] = 'R'
        elif dominoes[i - 1] == '.' and dominoes[i] == 'L':
            res[i - 1] = 'L'

    return "".join(res)
    
print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR